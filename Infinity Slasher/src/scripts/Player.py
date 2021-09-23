from godot import exposed, export
from godot import *
from enum import Enum


class State(Enum):
	RUNNING		= 0
	JUMPING		= 1
	MID_AIR		= 2
	FALLING		= 3
	ATTACKING	= 4


@exposed
class Player(KinematicBody2D):
	
	GRAVITY = 30
	
	velocity = Vector2.ZERO
	jump_force = Vector2(0, -550)
	state = State.RUNNING
	attackable_bodies = []
	
	
	def _ready(self):
		self.animated_sprite = self.get_node("AnimatedSprite")
		self.magic_particles = self.get_node("MagicParticles")
		self.attack_timer = self.get_node("AttackTimer")
		
	
	def _process_input(self):
		# Detect input here because _input function crashes game
		
		if Input.is_action_just_pressed("move_platform_up") and self.position.y > 256:
			self.move_to_platform(-1)
		elif Input.is_action_just_pressed("move_platform_down") and self.position.y < 512:
			self.move_to_platform(1)
		
		if Input.is_action_just_pressed("attack"):
			self.attack()
			
		
	def state_machine(self):
		if self.state == State.RUNNING:
			self.animated_sprite.play("run")
			
			self.velocity.x = (Input.get_action_strength("move_right") - Input.get_action_strength("move_left")) * 150
			
			if Input.is_action_just_pressed("jump"):
				self.jump()
		
		elif self.state == State.JUMPING:
			self.animated_sprite.play("jump")
			
		elif self.state == State.MID_AIR:
			self.animated_sprite.play("mid air")
			
			if self.velocity.y > 0:
				self.state = State.FALLING
			
		elif self.state == State.FALLING:
			self.animated_sprite.play("fall")
			
			if self.is_on_floor():
				self.state = State.RUNNING
				
		elif self.state == State.ATTACKING:
			self.animated_sprite.play("attack")
		
		
	def _physics_process(self, delta):
		self._process_input()
		self.state_machine()
		
		# Apply gravity
		if not self.is_on_floor() and self.state != State.ATTACKING:
			self.velocity.y += self.GRAVITY
		
		self.velocity = self.move_and_slide(self.velocity, Vector2.UP)
	
	
	def jump(self):
		self.velocity += self.jump_force
		self.state = State.JUMPING
		
		
	def attack(self):
		if self.state != State.ATTACKING:
			self.attack_timer.start()
			self.velocity.y = 0
			self.state = State.ATTACKING
		
		
	def move_to_platform(self, y_direction):
		self.position += Vector2(0, y_direction * 256)
		self.magic_particles.restart()
		
		
	def _on_AnimatedSprite_animation_finished(self):
		if self.state == State.JUMPING:
			self.animated_sprite.play("mid air")  # to prevent animation glitches
			self.state = State.MID_AIR
			
		elif self.state == State.ATTACKING:
			self.state = State.FALLING
			
			
	def _on_AttackDetector_body_entered(self, body):
		if body.is_in_group("Attackable"):
			self.attackable_bodies.append(body)
			
			
	def _on_AttackDetector_body_exited(self, body):
		if body.is_in_group("Attackable"):
			self.attackable_bodies.remove(body)
			
			
	def _on_AttackTimer_timeout(self):
		for body in self.attackable_bodies:
			self.get_tree().call_group("World", "remove_orb", body)

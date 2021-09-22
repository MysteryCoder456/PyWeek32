from godot import exposed, export
from godot import *
from enum import Enum


class State(Enum):
	RUNNING	= 0
	JUMPING	= 1
	MID_AIR	= 2
	FALLING	= 3


@exposed
class Player(KinematicBody2D):
	
	GRAVITY = 30
	
	velocity = Vector2.ZERO
	jump_force = Vector2(0, -500)
	was_on_floor = False
	state = State.RUNNING
	
	
	def jump(self):
		self.velocity += self.jump_force
		self.state = State.JUMPING
	
	
	def _ready(self):
		self.animated_sprite = self.get_node("AnimatedSprite")
		
		
	def _physics_process(self, delta):
		# State machine
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
		
		# Apply gravity
		if not self.is_on_floor():
			self.velocity.y += self.GRAVITY
		
		self.velocity = self.move_and_slide(self.velocity, Vector2.UP)
		self.was_on_floor = self.is_on_floor()
		
		
	def _on_AnimatedSprite_animation_finished(self):
		if self.state == State.JUMPING:
			self.animated_sprite.play("mid air")  # to prevent animation glitches
			self.state = State.MID_AIR

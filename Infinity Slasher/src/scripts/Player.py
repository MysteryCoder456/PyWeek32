from godot import exposed, export
from godot import *


@exposed
class Player(KinematicBody2D):
	
	GRAVITY = 40
	
	velocity = Vector2.ZERO
	jump_force = Vector2(0, -640)
	
	
	def _ready(self):
		self.animated_sprite = self.get_node("AnimatedSprite")
		self.animated_sprite.play("run")
		
		
	def _physics_process(self, delta):
		if Input.is_action_just_pressed("jump") and self.is_on_floor():
			self.velocity += self.jump_force
		else:
			# Apply gravity
			self.velocity.y += self.GRAVITY
		
		self.velocity = self.move_and_slide(self.velocity, Vector2.UP)

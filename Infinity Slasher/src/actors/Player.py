from godot import exposed, export
from godot import *


@exposed
class Player(KinematicBody2D):
	
	velocity = Vector2.ZERO
#	GRAVITY = 
	
	def _ready(self):
		self.animated_sprite = self.get_node("AnimatedSprite")
		self.animated_sprite.play("run")

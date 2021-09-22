from godot import exposed, export
from godot import *


@exposed
class Orb(RigidBody2D):

	def _ready(self):
		self.animated_sprite = self.get_node("AnimatedSprite")
		self.animated_sprite.play("default")
		self.set_bounce(1)

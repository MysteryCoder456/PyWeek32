from godot import exposed, export
from godot import *


@exposed
class Laser(KinematicBody2D):
	
	velocity = export(Vector2)
	
	
	def _physics_process(self, delta):
		self.velocity = self.move_and_slide(self.velocity)
		self.look_at(self.global_position + self.velocity)

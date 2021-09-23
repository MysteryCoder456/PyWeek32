from godot import exposed, export
from godot import *
from random import randint


@exposed
class Laser(KinematicBody2D):
	
	velocity = export(Vector2)
	damage = randint(5, 15)
	_game_over = False
	
	
	def _physics_process(self, delta):
		if not self._game_over:
			self.velocity = self.move_and_slide(self.velocity)
			self.look_at(self.global_position + self.velocity)
		
		
	def _on_CollisionDetector_body_entered(self, body):
		if body.is_in_group("Player"):
			self.get_tree().call_group("World", "damage_player", self.damage)
			
		self.get_parent().remove_child(self)
		self.queue_free()
		
		
	def game_over(self):
		self._game_over = True

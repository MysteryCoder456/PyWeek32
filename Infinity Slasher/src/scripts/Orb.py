from godot import exposed, export
from godot import *

LASER_SCENE = ResourceLoader.load("res://src/actors/Laser.tscn")


@exposed
class Orb(RigidBody2D):
	
	def _ready(self):
		self.animated_sprite = self.get_node("AnimatedSprite")
		self.animated_sprite.play("default")
		
		
	def _on_ShootTimer_timeout(self):
		target = self.find_parent("World").get_node("Player")
		
		if target.global_position.distance_to(self.global_position) > 150:
			laser_position = self.position
			laser_velocity = (target.global_position - self.global_position).normalized() * 300
			
			new_laser = LASER_SCENE.instance()
			new_laser.position = laser_position
			new_laser.velocity = laser_velocity
			self.get_parent().add_child(new_laser)

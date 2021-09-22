from godot import exposed, export
from godot import *

LASER_SCENE = ResourceLoader.load("res://src/actors/Laser.tscn")


@exposed
class Orb(RigidBody2D):
	
	def _ready(self):
		self.animated_sprite = self.get_node("AnimatedSprite")
		self.animated_sprite.play("default")
		
		
	def _on_ShootTimer_timeout(self):
		world = self.find_parent("World")
		target = world.get_node("Player")
		
		if target.global_position.distance_to(self.global_position) > 200:
			laser_position = self.position
			laser_velocity = (target.global_position - self.global_position).normalized() * 350
			
			new_laser = LASER_SCENE.instance()
			new_laser.position = laser_position
			new_laser.velocity = laser_velocity
			world.get_node("Lasers").add_child(new_laser)

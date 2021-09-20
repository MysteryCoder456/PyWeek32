from godot import exposed, export
from godot import *


@exposed
class World(Node2D):

	platforms_velocity = Vector2(-200, 0)
	platforms_acceleration = Vector2(-0.05, 0)
	
	
	def _ready(self):
		self.platforms = self.get_node("Platforms")
	
	
	def _physics_process(self, delta):
		self.platforms_velocity += self.platforms_acceleration
		self.platforms.position += self.platforms_velocity * delta
		
		if self.platforms.position.x <= -32 * self.platforms.cell_size.x:
			self.platforms.position += Vector2(32 * self.platforms.cell_size.x, 0)

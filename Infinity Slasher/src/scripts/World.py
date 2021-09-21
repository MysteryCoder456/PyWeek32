from godot import exposed, export
from godot import *


@exposed
class World(Node2D):

	platforms_velocity = Vector2(-250, 0)
	platforms_acceleration = Vector2(-0.05, 0)
	
	bg_velocity = platforms_velocity / 15
	bg_acceleration = platforms_acceleration / 15
	
	
	def _ready(self):
		self.background = self.get_node("Background")
		self.platforms = self.get_node("Platforms")
	
	
	def _physics_process(self, delta):
		self.move_background(delta)
		self.move_platforms(delta)
		
		
	def move_background(self, delta):
		self.bg_velocity += self.bg_acceleration
		self.background.position += self.bg_velocity * delta
		
		if self.background.position.x <= -1000:
			self.background.position += Vector2(1000, 0)
		
		
	def move_platforms(self, delta):
		self.platforms_velocity += self.platforms_acceleration
		self.platforms.position += self.platforms_velocity * delta
		
		if self.platforms.position.x <= -32 * self.platforms.cell_size.x:
			self.platforms.position += Vector2(32 * self.platforms.cell_size.x, 0)

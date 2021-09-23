from godot import exposed, export
from godot import *
from random import randint

ORB_SCENE = ResourceLoader.load("res://src/actors/Orb.tscn")
ORB_DEATH_PARTICLES_SCENE = ResourceLoader.load("res://src/particles/OrbDeathParticles.tscn")


@exposed
class World(Node2D):

	platforms_velocity = Vector2(-250, 0)
	platforms_acceleration = Vector2(-0.05, 0)
	
	bg_velocity = platforms_velocity / 15
	bg_acceleration = platforms_acceleration / 15
	
	orb_limit = 6
	
	player_health = 100
	player_score = 0
	
	
	def _ready(self):
		self.background = self.get_node("Background")
		self.platforms = self.get_node("Platforms")
		self.orbs = self.get_node("Orbs")
		self.orb_spawn = self.get_node("OrbSpawn")
		self.orb_spawn_timer = self.get_node("OrbSpawnTimer")
		self.hud = self.get_node("HUD")
		
		
	def _physics_process(self, delta):
		self.move_background(delta)
		self.move_platforms(delta)
		self.orb_spawn_timer.wait_time *= 0.99999
		self.orb_limit += 0.0001
		
		
	def _on_OrbSpawnTimer_timeout(self):
		if self.orbs.get_child_count() < int(self.orb_limit):
			orb_position = self.orb_spawn.position
			orb_velocity = Vector2(
				randint(-150, -50),
				randint(-150, 150)
			)
			
			new_orb = ORB_SCENE.instance()
			new_orb.position = orb_position
			new_orb.linear_velocity = orb_velocity
			self.orbs.add_child(new_orb)
			
			
	def remove_orb(self, orb):
		self.orbs.remove_child(orb)
		orb.queue_free()
		
		death_particles = ORB_DEATH_PARTICLES_SCENE.instance()
		self.add_child(death_particles)
		death_particles.global_position = orb.global_position
		death_particles.restart()
		
		self.player_score += 1
		self.hud.set_score(self.player_score)
			
			
	def damage_player(self, damage):
		self.player_health -= damage
		self.hud.set_health(self.player_health)
		
		
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

from godot import exposed, export
from godot import *


@exposed
class HUD(CanvasLayer):
	
	def _ready(self):
		self.health_bar = self.get_node("HUD/V/HealthBar")
		self.score_label = self.get_node("HUD/V/ScoreLabel")
		self.game_over_label = self.get_node("HUD/GameOverLabel")
		
		self.game_over_label.visible = False
		
		
	def set_health(self, value):
		self.health_bar.value = value
		
		
	def set_score(self, value):
		self.score_label.text = f"Score: {value}"
		
		
	def game_over(self):
		self.game_over_label.visible = True
		self.health_bar.visible = False
		self.score_label.visible = False

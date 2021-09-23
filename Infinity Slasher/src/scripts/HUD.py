from godot import exposed, export
from godot import *


@exposed
class HUD(CanvasLayer):
	
	def _ready(self):
		self.stats_box = self.get_node("HUD/H")
		self.health_bar = self.get_node("HUD/H/HealthBar")
		self.score_label = self.get_node("HUD/H/ScoreLabel")
		
		self.game_over_box = self.get_node("HUD/V")
		self.game_over_label = self.get_node("HUD/V/GameOverLabel")
		self.final_score_label = self.get_node("HUD/V/FinalScoreLabel")
		
		self.stats_box.visible = True
		self.game_over_box.visible = False
		
		
	def set_health(self, value):
		self.health_bar.value = value
		
		
	def set_score(self, value):
		self.score_label.text = f"Score: {value}"
		
		
	def game_over(self, final_score):
		self.final_score_label.text = f"Final Score: {final_score}"
		
		self.stats_box.visible = False
		self.game_over_box.visible = True

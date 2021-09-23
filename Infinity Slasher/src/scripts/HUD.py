from godot import exposed, export
from godot import *


@exposed
class HUD(CanvasLayer):
	
	def _ready(self):
		self.health_bar = self.get_node("HUD/V/HealthBar")
		self.score_label = self.get_node("HUD/V/ScoreLabel")
		
		
	def set_health(self, value):
		self.health_bar.value = value
		
		
	def set_score(self, value):
		self.score_label.text = f"Score: {value}"

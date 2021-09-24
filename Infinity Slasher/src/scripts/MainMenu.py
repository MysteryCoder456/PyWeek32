from godot import exposed, export
from godot import *


@exposed
class MainMenu(Control):
	
	game_scene_path = "res://src/scenes/World.tscn"
	
	
	def _ready(self):
		self.animation_player = self.get_node("AnimationPlayer")
	
	
	def _on_PlayButton_pressed(self):
		self.animation_player.play("Fade")
		
		
	def _on_AnimationPlayer_animation_finished(self, animation):
		self.get_tree().change_scene(self.game_scene_path)

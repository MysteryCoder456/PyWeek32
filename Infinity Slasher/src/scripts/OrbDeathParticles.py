from godot import exposed, export
from godot import *


@exposed
class OrbDeathParticles(CPUParticles2D):

	def _on_DespawnTimer_timeout(self):
		self.get_parent().remove_child(self)
		self.queue_free()

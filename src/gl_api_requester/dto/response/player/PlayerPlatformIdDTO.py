from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class PlayerPlatformIdDTO(DTO):
	"""
	Contains the platform ID of a Galaxy Life player.
	"""

	PlatforId: str
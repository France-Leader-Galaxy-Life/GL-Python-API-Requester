from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class LeaderboardWarpointsPlayerDTO(DTO):
	"""
	Contains player warpoints.
	"""

	Warpoints: int
	AllianceName: int
	Id: int
	Name: str
	Avatar: str

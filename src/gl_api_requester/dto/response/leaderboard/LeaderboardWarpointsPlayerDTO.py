from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class LeaderboardWarpointsPlayerDTO(DTO):
	"""
	Contains player warpoints.
	"""

	Warpoints: int
	AllianceName: str
	Id: str
	Name: str
	Avatar: str

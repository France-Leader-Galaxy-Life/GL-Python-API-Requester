from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class LeaderboardRivalsWonPlayerDTO(DTO):
	"""
	Contains player rivals won.
	"""

	RivalsWon: int
	Id: str
	Name: str
	Avatar: str

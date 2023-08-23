from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class LeaderboardXpFromAttackPlayerDTO(DTO):
	"""
	Contains player xp from attacks.
	"""

	Level: int
	ExperienceFromAttacks: int
	Id: str
	Name: str
	Avatar: str

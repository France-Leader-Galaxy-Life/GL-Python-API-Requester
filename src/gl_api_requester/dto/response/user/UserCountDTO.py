from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class UserCountDTO(DTO):
	"""
	Total number of Galaxy Life players.
	"""

	count: int

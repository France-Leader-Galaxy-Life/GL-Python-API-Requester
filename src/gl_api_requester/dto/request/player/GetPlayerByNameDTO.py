from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class GetPlayerByNameDTO(DTO):
	"""
	An player name request.
	"""

	name: str
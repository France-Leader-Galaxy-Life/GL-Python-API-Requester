from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class GetPlayerByIdDTO(DTO):
	"""
	An player Id request.
	"""

	Id: int
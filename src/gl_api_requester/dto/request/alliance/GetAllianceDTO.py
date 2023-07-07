from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class GetAllianceDTO(DTO):
	"""
	An alliance request.
	"""

	name: str
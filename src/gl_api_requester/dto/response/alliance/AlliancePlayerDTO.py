from dataclasses import dataclass
from ...DTO import DTO



@dataclass
class AlliancePlayerDTO(DTO):
	"""
	Contains a player of alliance.
	"""

	Id: str
	Name: str
	Avatar: str
	AllianceRole: int
	TotalWarPoints: int

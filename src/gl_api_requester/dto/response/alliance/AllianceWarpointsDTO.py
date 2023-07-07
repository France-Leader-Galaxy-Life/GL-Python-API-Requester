from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class AllianceWarpointsDTO(DTO):
	"""
	Contains warpoints of alliance.
	"""

	Id: str
	Name: str
	Warpoints: int
	MemberCount: int

from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class ServerDTO(DTO):
	"""
	Contains stat of a Galaxy Life Server .
	"""

	Name: str
	IsOnline: bool
	Ping: int

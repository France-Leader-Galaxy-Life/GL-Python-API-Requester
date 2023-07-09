from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class ServerStatusDTO(DTO):
	"""
	Contains stat of a Galaxy Life Server .
	"""

	Name: str
	IsOnline: bool
	Ping: int

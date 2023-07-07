from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class PlanetDTO(DTO):
	"""
	Contains the data of a Galaxy Life planet.
	"""

	OwnerId: str
	HQLevel: int

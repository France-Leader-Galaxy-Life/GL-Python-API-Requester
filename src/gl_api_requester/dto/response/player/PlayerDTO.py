from dataclasses import dataclass
from typing import List
from ...DTO import DTO
from ...response.planet.PlanetDTO import PlanetDTO

@dataclass
class PlayerDTO(DTO):
	"""
	Contains the data of a Galaxy Life player.
	"""

	Id: str
	Name: str
	Avatar: str
	Level: int
	Experience: int
	AllianceId: str
	Planets: List[PlanetDTO]
from dataclasses import dataclass
from typing import List
from ...DTO import DTO
from ...response.alliance.AlliancePlayerDTO import AlliancePlayerDTO
from ...response.alliance.AllianceEmblemDTO import AllianceEmblemDTO



@dataclass
class AllianceDTO(DTO):
	"""
	Contains an alliance.
	"""

	Id: str
	Name: str
	Description: str
	Emblem: AllianceEmblemDTO
	AllianceLevel:int
	WarPoints:int
	WarsWon:int
	WarsLost:int
	InWar:bool
	OpponentAllianceId:str
	Members: List[AlliancePlayerDTO]
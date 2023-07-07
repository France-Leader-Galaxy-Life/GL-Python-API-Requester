from dataclasses import dataclass
from typing import List
from ...DTO import DTO
from ...response.status.ServerDTO import ServerDTO

@dataclass
class StatusDTO(DTO):
	"""
	Contains the status of all Galaxy Life server.
	"""

	Server: List[ServerDTO]
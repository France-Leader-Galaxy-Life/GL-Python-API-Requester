from dataclasses import dataclass
from ...DTO import DTO


@dataclass
class AllianceEmblemDTO(DTO):
	"""
	Contains an alliance emblem.
	"""

	Shape: int
	Pattern: int
	Icon: int
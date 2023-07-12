from typing import Dict, Any

class APIErrorException(Exception):
	"""
	Exception thrown when an API error occurs.
	"""

	def __init__(self, message: str, api_error: Any) -> None:
		"""
		Parameters
		----------
		- message: `str`
			The exception message.
		- api_error: `str`
			The API error JSON.
		"""
		super().__init__(message)
		self.api_error = api_error

	def get_api_error(self) -> Any:
		"""
		Returns the API error message.
		"""
		return self.api_error
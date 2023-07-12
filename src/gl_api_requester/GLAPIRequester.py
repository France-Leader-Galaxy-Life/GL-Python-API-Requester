from typing import Dict, List, Any
from dacite import from_dict
import json
import requests

from .dto.DTO import DTO
from .dto.response.alliance.AllianceDTO import AllianceDTO
from .dto.response.alliance.AllianceWarpointsDTO import AllianceWarpointsDTO

from .dto.response.player.PlayerDTO import PlayerDTO
from .dto.response.player.PlayerStatsDTO import PlayerStatsDTO

from .dto.response.leaderboard.LeaderboardXpFromAttackPlayerDTO import LeaderboardXpFromAttackPlayerDTO
from .dto.response.leaderboard.LeaderboardRivalsWonPlayerDTO import LeaderboardRivalsWonPlayerDTO
from .dto.response.leaderboard.LeaderboardWarpointsPlayerDTO import LeaderboardWarpointsPlayerDTO

from .dto.response.status.ServerStatusDTO import ServerStatusDTO

from .dto.request.alliance.GetAllianceDTO import GetAllianceDTO
from .dto.request.player.GetPlayerByIdDTO import GetPlayerByIdDTO
from .dto.request.player.GetPlayerByNameDTO import GetPlayerByNameDTO

from .exception.APIErrorException import APIErrorException


class GLAPIRequester:
	"""
	The Galaxy Life API requester.
	"""

	def __init__(self) -> None:
		self.uri = "https://api.galaxylifegame.net"

	############
	# Alliance #
	############

	def get_alliance(self, name: GetAllianceDTO) -> AllianceDTO:
		return from_dict(AllianceDTO, self.__send_request(f"/Alliances/get?name={name}"))
	
	def get_alliance_warpoint_leaderboard(self) -> List[AllianceWarpointsDTO]:
		return [
			from_dict(AllianceWarpointsDTO, alliance)
			for alliance in self.__send_request("/Alliances/warpointLb")
		]

	###############
	# Leaderboard #
	###############

	def get_leaderboard_xp(self) -> List[PlayerDTO]:
		return [
			from_dict(PlayerDTO, player)
			for player in self.__send_request("/Leaderboard/xp")
		]

	def get_leaderboard_xp_from_attack(self) -> List[LeaderboardXpFromAttackPlayerDTO]:
		return [
			from_dict(LeaderboardXpFromAttackPlayerDTO, player)
			for player in self.__send_request("/Leaderboard/xpFromAttack")
		]

	def get_leaderboard_rivals_wons(self) -> List[LeaderboardRivalsWonPlayerDTO]:
		return [
			from_dict(LeaderboardRivalsWonPlayerDTO, player)
			for player in self.__send_request("/Leaderboard/rivalsWon")
		]

	def get_leaderboard_warpoint(self) -> List[LeaderboardWarpointsPlayerDTO]:
		return [
			from_dict(LeaderboardWarpointsPlayerDTO, player)
			for player in self.__send_request("/Leaderboard/warpoints")
		]

	##########
	# Status #
	##########

	def get_status(self) -> List[ServerStatusDTO]:
		return [
			from_dict(ServerStatusDTO, server)
			for server in self.__send_request("/status")
		]

	#########
	# Users #
	#########

	def get_user_from_id(self, player_id: GetPlayerByIdDTO) -> PlayerDTO:
		return from_dict(PlayerDTO, self.__send_request(f"/Users/get?id={player_id}"))

	def get_user_from_name(self, player_name: GetPlayerByNameDTO) -> PlayerDTO:
		return from_dict(PlayerDTO, self.__send_request(f"/Users/name?name={player_name}"))
	
	def get_search_user_by_name(self, player_name: GetPlayerByNameDTO) -> List[PlayerDTO]:
		return [
			from_dict(PlayerDTO, player)
			for player in self.__send_request(f"/Users/search?name={player_name}")
		]

	def get_user_steam_account(self, player_id: GetPlayerByIdDTO) -> PlayerDTO:
		return from_dict(PlayerDTO, self.__send_request(f"/Users/steam?steamId={player_id}"))

	def get_user_platform_id(self, player_id: GetPlayerByIdDTO) -> Any:
		return self.__send_request(f"/Users/platformId?userId={player_id}")

	def get_user_stats(self, player_id: GetPlayerByIdDTO) -> PlayerStatsDTO:
		return from_dict(PlayerStatsDTO, self.__send_request(f"/Users/stats?id={player_id}"))

	def get_user_count(self) -> Any:
		return self.__send_request(f"/Users/count")
		

	###################
	# Private methods #
	###################

	def __send_request(self, endpoint: str) -> Dict:
		
		# Send the request
		response = requests.get(self.uri+endpoint)
		if response.status_code >= 400:
			raise APIErrorException("An API error occured : "+response.text, response.text)

		try:
			return response.json()
		except:
			raise APIErrorException("An API error occured : "+response.text, response.text)
from typing import Dict, List
from dacite import from_dict
import requests

from .dto.DTO import DTO
from .dto.response.alliance.AllianceDTO import AllianceDTO
from .dto.response.alliance.AllianceWarpointsDTO import AllianceWarpointsDTO

from .dto.response.player.PlayerDTO import PlayerDTO
from .dto.response.player.PlayerPlatformIdDTO import PlayerPlatformIdDTO
from .dto.response.player.PlayerStatsDTO import PlayerStatsDTO

from .dto.response.leaderboard.LeaderboardXpFromAttackPlayerDTO import LeaderboardXpFromAttackPlayerDTO
from .dto.response.leaderboard.LeaderboardRivalsWonPlayerDTO import LeaderboardRivalsWonPlayerDTO
from .dto.response.leaderboard.LeaderboardWarpointsPlayerDTO import LeaderboardWarpointsPlayerDTO

from .dto.response.status.StatusDTO import StatusDTO

from .dto.request.alliance.GetAllianceDTO import GetAllianceDTO
from .dto.request.player.GetPlayerByIdDTO import GetPlayerByIdDTO
from .dto.request.player.GetPlayerByNameDTO import GetPlayerByNameDTO

from.dto.response.user.UserCountDTO import UserCountDTO
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
		return from_dict(List[AllianceWarpointsDTO], self.__send_request("/Alliances/warpointLb"))

	###############
	# Leaderboard #
	###############

	def get_leaderboard_xp(self) -> List[PlayerDTO]:
		return from_dict(List[PlayerDTO], self.__send_request("/Leaderboard/xp"))

	def get_leaderboard_xp_from_attack(self) -> List[LeaderboardXpFromAttackPlayerDTO]:
		return from_dict(List[LeaderboardXpFromAttackPlayerDTO], self.__send_request("/Leaderboard/xpFromAttack"))

	def get_leaderboard_rivals_wons(self) -> List[LeaderboardRivalsWonPlayerDTO]:
		return from_dict(List[LeaderboardRivalsWonPlayerDTO], self.__send_request("/Leaderboard/rivalsWon"))

	def get_leaderboard_warpoint(self) -> List[LeaderboardWarpointsPlayerDTO]:
		return from_dict(List[LeaderboardWarpointsPlayerDTO], self.__send_request("/Leaderboard/warpoints"))

	##########
	# Status #
	##########

	def get_status(self) -> StatusDTO:
		return from_dict(StatusDTO, self.__send_request("/status"))

	#########
	# Users #
	#########

	def get_user_from_id(self, player_id: GetPlayerByIdDTO) -> PlayerDTO:
		return from_dict(PlayerDTO, self.__send_request(f"/Users/get?id={player_id}"))

	def get_user_from_name(self, player_name: GetPlayerByNameDTO) -> PlayerDTO:
		return from_dict(PlayerDTO, self.__send_request(f"/Users/name?name={player_name}"))
	
	def get_search_user_by_name(self, player_name: GetPlayerByNameDTO) -> List[PlayerDTO]:
		return from_dict(List[PlayerDTO], self.__send_request(f"/Users/search?name={player_name}"))

	def get_user_steam_account(self, player_id: GetPlayerByIdDTO) -> List[PlayerDTO]:
		return from_dict(List[PlayerDTO], self.__send_request(f"/Users/steam?steamId={player_id}"))

	def get_user_platform_id(self, player_id: GetPlayerByIdDTO) -> PlayerPlatformIdDTO:
		return from_dict(PlayerPlatformIdDTO, self.__send_request(f"/Users/steam?userId={player_id}"))

	def get_user_stats(self, player_id: GetPlayerByIdDTO) -> PlayerStatsDTO:
		return from_dict(PlayerStatsDTO, self.__send_request(f"/Users/stats?id={player_id}"))

	def get_user_count(self) -> UserCountDTO:
		return from_dict(UserCountDTO, self.__send_request(f"/Users/count"))
		

	###################
	# Private methods #
	###################

	def __send_request(self, endpoint: str) -> Dict:
		
		# Send the request
		response = requests.get(self.uri+endpoint)
		json_response = response.json() 

		# Check the error
		if response.status_code >= 400 :
			raise APIErrorException("An API error occured.", json_response)

		# Parse the JSON dictionnary to an object
		return json_response
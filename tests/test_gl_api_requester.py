import pytest
from gl_api_requester import GLAPIRequester, APIErrorException

@pytest.fixture
def api_requester():
	return GLAPIRequester()

def test_get_alliance_PASSED(api_requester):
	response = api_requester.get_alliance(name="France Leader")
	assert response is not None

def test_get_alliance_FAILED(api_requester):
	try:
		response = api_requester.get_alliance(name="France Leader XXX")
	except APIErrorException as e:
		assert e is not APIErrorException


def test_get_alliance_warpoint_leaderboard(api_requester):
	response = api_requester.get_alliance_warpoint_leaderboard()
	assert response is not None

def test_get_leaderboard_xp(api_requester):
	response = api_requester.get_leaderboard_xp()
	assert response is not None

def test_get_leaderboard_xp_from_attack(api_requester):
	response = api_requester.get_leaderboard_xp_from_attack()
	assert response is not None

def test_get_leaderboard_rivals_wons(api_requester):
	response = api_requester.get_leaderboard_rivals_wons()
	assert response is not None

def test_get_leaderboard_warpoint(api_requester):
	response = api_requester.get_leaderboard_warpoint()
	assert response is not None

def test_get_status(api_requester):
	response = api_requester.get_status()
	assert response is not None


def test_get_user_from_name_PASSED(api_requester):
	response = api_requester.get_user_from_name('vadeledav')
	assert response is not None

def test_get_user_from_name_FAILED(api_requester):
	try:
		response = api_requester.get_user_from_name('ajfnazofn')
	except APIErrorException as e:
		assert e is not APIErrorException


def test_get_user_from_id_PASSED(api_requester):
	response = api_requester.get_user_from_id(player_id="268172")
	assert response is not None

def test_get_user_from_id_FAILED(api_requester):
	try:
		response = api_requester.get_user_from_id(player_id="666666")
	except APIErrorException as e:
		assert e is not APIErrorException



def test_get_search_user_by_name_PASSED(api_requester):
	response = api_requester.get_search_user_by_name(player_name="vadeledav")
	assert response is not None

def test_get_search_user_by_name_FAILED(api_requester):
	try:
		response = api_requester.get_search_user_by_name(player_name="fkazfapzfkazpofk")
	except APIErrorException as e:
		assert e is not APIErrorException



def test_get_user_steam_account_PASSED(api_requester):
	response = api_requester.get_user_steam_account(player_id=76561198403360223)
	assert response is not None

def test_get_user_steam_account_FAILED(api_requester):
	try:
		response = api_requester.get_user_steam_account(player_id=32197984561321322)
	except APIErrorException as e:
		assert e is not APIErrorException


def test_get_user_platform_id_PASSED(api_requester):
	response = api_requester.get_user_platform_id(player_id=268172)
	assert response is not None

def test_get_user_platform_id_FAILED(api_requester):
	try:
		response = api_requester.get_user_platform_id(player_id=666666)
	except APIErrorException as e:
		assert e is not APIErrorException



def test_get_user_stats_PASSED(api_requester):
	response = api_requester.get_user_stats(player_id=268172)
	assert response is not None

def test_get_user_stats_FAILED(api_requester):
	try:
		response = api_requester.get_user_stats(player_id=666666)
	except APIErrorException as e:
		assert e is not APIErrorException




def test_get_user_count(api_requester):
	response = api_requester.get_user_count()
	assert response is not None


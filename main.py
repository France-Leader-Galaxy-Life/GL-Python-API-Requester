from src.gl_api_requester.GLAPIRequester import *

def main():
	requester = GLAPIRequester()
	print(requester.get_user_from_name('vadeledav'))
	print(requester.get_alliance(name="France Leader"))
	print(requester.get_alliance_warpoint_leaderboard())
	print(requester.get_leaderboard_xp())
	print(requester.get_leaderboard_xp_from_attack())
	print(requester.get_leaderboard_rivals_wons())
	print(requester.get_leaderboard_warpoint())
	print(requester.get_status())
	print(requester.get_user_from_id(player_id="268172"))
	print(requester.get_user_from_name(player_name="vadeledav"))
	print(requester.get_search_user_by_name(player_name="vadeledav"))
	print(requester.get_user_steam_account(player_id=76561198403360223))
	print(requester.get_user_platform_id(player_id=268172))
	print(requester.get_user_stats(player_id="268172"))
	print(requester.get_user_count())

if __name__ == "__main__":
	main()

# Installation

```
pip install gl-api-requester
```

# Usage

```python
from gl_api_requester import *

try:
	api_requester = GLAPIRequester()

	# Alliance request
	requester.get_alliance(name="France Leader")
	requester.get_alliance_warpoint_leaderboard()

	# Leaderboard request
	requester.get_leaderboard_xp()
	requester.get_leaderboard_xp_from_attack()
	requester.get_leaderboard_rivals_wons()
	requester.get_leaderboard_warpoint()

	# Status request
	requester.get_status()

	# Users request
	requester.get_user_from_name('vadeledav')
	requester.get_user_from_id(player_id="268172")
	requester.get_user_from_name(player_name="vadeledav")
	requester.get_search_user_by_name(player_name="vadeledav")
	requester.get_user_steam_account(player_id=76561198403360223)
	requester.get_user_platform_id(player_id=268172)
	requester.get_user_stats(player_id="268172")
	requester.get_user_count()

except APIErrorException as e:
	print(e.api_error)
```


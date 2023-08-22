<!-- PROJECT LOGO -->
<p align="center">
  <a href="https://discord.com/invite/bJexbUhWFA">
   <img src="https://avatars.githubusercontent.com/u/133906616?s=200&v=4" alt="Logo">
  </a>

  <h3 align="center">France Leader</h3>

  <p align="center">
    A Galaxy Life API requester in Python 
</p>

<p align="center">
	
  <a href="https://discord.com/invite/bJexbUhWFA"><img src="https://img.shields.io/badge/Discord-France%20Leader-red?logo=Discord&logoColor=%235865F2&color=%235865F2" alt="Join Discord of France Leader"></a>
  <a href="https://discord.com/invite/vqRyN6WUsN"><img src="https://img.shields.io/badge/Discord-Galaxy%20Life-red?logo=Discord&logoColor=%235865F2&color=%235865F2" alt="Join Discord of Galaxy Life"></a>
  <a><img src="https://github.com/France-Leader-Galaxy-Life/GL-Python-API-Requester/actions/workflows/tests.yml/badge.svg" alt="Galaxy Life API python requester"></a>
</p>


# Galaxy Life Python Api Requester

A simple pip package to make request on the Galaxy Life game API.


# Installation

```
pip install gl-api-requester
```

# Usage

```python
from gl_api_requester import *

try:
	requester = GLAPIRequester()

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
	requester.get_search_user_by_name(player_name="vadeledav")
	requester.get_user_steam_account(player_id=76561198403360223)
	requester.get_user_platform_id(player_id=268172)
	requester.get_user_stats(player_id="268172")
	requester.get_user_count()

except APIErrorException as e:
	print(e.api_error)
```


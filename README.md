# Installation

```
pip install fl-api-requester
```

# Usage

```python
from fl_api_requester import *

connection_data = FLAPIConnectionData()
connection_data.api_uri = "http://localhost:8080"
connection_data.set_credentials("username", "password")

try:
    api_requester = FLAPIRequester(connection_data)

    # Login
    api_requester.login()

    # Get some data
    player = api_requester.get_player("Galactifer")
    alliance = api_requester.get_alliance("France Leader")

    print(player)
    print(alliance)
    print(len(alliance.players))

    # Get a War attack
    attack = api_requester.get_player_attacks("Galactifer")

    print(f"Galactifer attacked on {attack[0].timestamp_to_datetime():%d/%m/%Y at %H:%M:%S}")
except APIErrorException as e:
    print(e.api_error)
```


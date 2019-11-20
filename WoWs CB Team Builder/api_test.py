# a file for test Wargaming API functionality

# WG API key stored here
import api_keys

import json
import requests

key = api_keys.wg_api_key

# from API reference...to get detailed clan info
# https://api.worldofwarships.com/wows/clans/info/?application_id=cdcbc9fdb2ee0eb2f701d4622deb485c&clan_id=1000044409

# from MM discord...unlisted clan info. what does this provide? 
# https://clans.worldofwarships.eu/clans/wows/1000044409/api/claninfo/

response = requests.get("https://api.worldofwarships.com/wows/encyclopedia/ships/?application_id=cdcbc9fdb2ee0eb2f701d4622deb485c&fields=name")
todos = json.loads(response.text)
print(todos)
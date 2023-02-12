import json
import requests

import mysecrets
import sats

response = requests.get("https://api.n2yo.com/rest/v1/satellite/tle/" + sats.sats['SO-50'] + "&apiKey=" + mysecrets.API_KEY)
print(response.json()['info'])

passes = requests.get("https://api.n2yo.com/rest/v1/satellite/radiopasses/" + sats.sats['SO-50'] + "/" +
                      mysecrets.MY_LAT + "/" + mysecrets.MY_LON + "/" + mysecrets.MY_ALT + "/1/5/&apiKey=" + mysecrets.API_KEY)
passinfo = passes.json()
print(passinfo)
import requests
import datetime

params = {}
params["api_key"] = MBTA_API_KEY
params["stop"] = "place-rugg"

request = requests.get("http://realtime.mbta.com/developer/api/v2/predictionsbystop", params=params)
data = request.json()

output = ""
for x in range(len(data["mode"])-1):
  arrival = data["mode"][0]["route"][0]["direction"][0]["trip"][0]["pre_dt"]
  arrival_formatted = datetime.datetime.fromtimestamp(int(arrival)).strftime('%-I:%M %p')

  wait = int(data["mode"][0]["route"][0]["direction"][0]["trip"][0]["pre_away"])
  wait_formatted = str(wait/60) + " minutes " + str(wait%60) + " seconds"

  direction = data["mode"][0]["route"][0]["direction"][0]["direction_name"]
  output += direction + "\n" + arrival_formatted + "\n" + wait_formatted + "\n"

print output

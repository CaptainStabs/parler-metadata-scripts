import json
import glob
import os

with open("./metadata/meta-55OCK244tKGX.json", 'r', encoding='utf=8') as f:
	data = json.loads(f.read())
	gps_lat = data[0]["GPSLatitude"]
	print(gps_lat)
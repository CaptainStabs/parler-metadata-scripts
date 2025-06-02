import json
import glob

geo_output = open("geo_output.txt", 'a')
no_geo = open("no_geo.txt", "a")

def extract_geo():
	data = json.loads(f.read())
	try:
		gps_lat = data[0]["GPSLatitude"]
		gps_lat = gps_lat.split(" ")
		gps_lat.pop(1)
		gps_lat = [i.replace('"', '') for i in gps_lat] # Because I don't know regex yet
		gps_lat = [i.replace('\'', '') for i in gps_lat]  # Because I don't know regex yet
		gps_lat = ' '.join(gps_lat)

		gps_lon = data[0]["GPSLongitude"]
		gps_lon = gps_lon.split(" ")
		gps_lon.pop(1)
		gps_lon = [i.replace('"', '') for i in gps_lon] # Because I don't know regex yet
		gps_lon = [i.replace('\'', '') for i in gps_lon]  # Because I don't know regex yet
		gps_lon = ' '.join(gps_lon)

		print(str(gps_lat) + "," + str(gps_lon), file=geo_output)

	except KeyError:
		print(fn, file=no_geo)

for fn in glob.glob('metadata/*.json'):
	with open(fn, 'r', encoding='utf=8') as f:
		extract_geo()
		

		

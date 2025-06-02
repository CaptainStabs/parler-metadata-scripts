import json
import glob
import os
import time


if os.path.exists("total_items.py") == False:
	total_items = open("total_items.py", "w")
	print("Counting items... Please wait...")
	items = len(os.listdir('./metadata'))
	print("Total files in directory: " + str(items))
	print("items = " + str(items), file=total_items)
else:
	print("Items already counted, if you have removed or added files, please delete total_items.txt and rerun the script")
	from total_items import items
print("Opening files...")
geo_output = open("geo_output.txt", 'a')
no_geo = open("no_geo.txt", "a")
check_geo = open("geo_output.txt", 'r')
check_no_geo = open("no_geo.txt", 'r')
x = 0

def extract_geo():
	data = json.loads(f.read())
	try:
		dict = data[0]
		gps_lat = data[0]["GPSLatitude"]
		if dict.get("GPSPosition") !=None:
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
			print(fn + ", " + str(gps_lat) + ", " + str(gps_lon), file=geo_output)
			#print("saving")


	except KeyError:
		for line in check_no_geo:
			if str(f) not in line:
				print(f, file=no_geo)
				print(KeyError)

	except IndexError:
		print("I thought you fixed this dumbass")		
		print(IndexError)
		
			


for fn in glob.glob('metadata/*.json'):
	with open(fn, 'r', encoding='utf=8') as f:
		start = time.time()
		extract_geo()
		x += 1 
		if x != 0 and x % 10000 == 0:
				#print(x)
				percent = round((x / int(items))*100, 4)
				print(str(percent) + "%")
				stop = time.time()
				duration = stop-start
				print(duration)
				print(duration/10000)
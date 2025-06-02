import glob
import json

output = open("geo.txt", "a")

def extract():
	data = json.loads(f.read())
	try:
		gps = data[0]["GPSPosition"]
		#print(vendor)
		print(gps, file=output)
	except KeyError:
		#print("N/A")
		print("No location")


for fn in glob.glob('metadata/*.json'):
	with open(fn, 'r', encoding="utf=8") as f:
		#print("File decoded")
		extract()
print("Done")
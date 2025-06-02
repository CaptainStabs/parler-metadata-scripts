import glob
import json
import os

x=0
output = open("devices.txt", "a")
if os.path.exists("total_items.py") == False:
	total_items = open("total_items.py", "w")
	print("Counting items... Please wait...")
	items = len(os.listdir('./metadata'))
	print("Total files in directory: " + str(items))
	print("items = " + str(items), file=total_items)
else:
	print("Items already counted, if you have removed or added files, please delete total_items.txt and rerun the script")
	from total_items import items


def extract():
	#print("Reading file")
	data = json.loads(f.read())
	#print("File read")
	try:
		make = data[0]["Make"]
		model = data[0]["Model"]
		#print(vendor)
		extracted = [make, model]
		print(extracted, file=output)
	except KeyError:
		#print("N/A")
		print("N/A", file=output)

def count():
	file_in = open("vendor_data.txt", 'r')
	outfile = open("output2.txt", "a")
	text = file_in.read()
	apple_count = text.count("Apple")
	other_count = text.count("N/A")
	print("Apple: " + str(apple_count),file=outfile)
	print("Apple: " + str(apple_count))
	print("Other: " + str(other_count), file=outfile)
	print("Other: " + str(other_count))
	for line in file_in:
		if not ("Apple" or "N/A") in line:
			print(line, file=outfile)
			print(line)

for fn in glob.glob('metadata/*.json'):
	with open(fn, 'r', encoding="utf=8") as f:
		#print("File decoded")
		extract()
		x += 1 
		if x != 0 and x % 10000 == 0:
				percent = round((x / int(items))*100, 4)
				print(str(percent) + "%")
print("Done")
#count()
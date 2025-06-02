import glob
import json

output = open("vendor_data.txt", "a")
def extract():
	#print("Reading file")
	data = json.loads(f.read())
	#print("File read")
	try:
		vendor = data[0]["HandlerVendorID"]
		#print(vendor)
		print(vendor, file=output)
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
print("Done")
#count()
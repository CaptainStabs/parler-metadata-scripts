import glob
import json
output = open("vendor_data.txt", "a")
def extract():
	data = json.loads(f.read())
	try:
		vendor = data[0]['HandlerVendorID']
		#print(vendor)
		print(vendor, file=output)
	except KeyError:
		#print("N/A")
		print("N/A", file=output)

def count():
	in_file = open("vendor_data.txt", 'r')
	outfile = open("output2.txt", "a")
	text = in_file.read()
	apple_count = text.count("Apple")
	other_count = text.count("N/A")
	print("Apple: " + str(apple_count), file=outfile)
	print("Apple: " + str(apple_count))
	print("Other: " + str(other_count), file=outfile)
	print("Other: " + str(other_count))
	for line in in_file:
		if not ("Apple" or "N/A") in line:
			print(line, file=outfile)
			print(line)

for fn in glob.glob('metadata/*.json'):
	with open(fn, 'r', encoding="utf=8") as f:
		extract()
print("Done")
#count()
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
count()
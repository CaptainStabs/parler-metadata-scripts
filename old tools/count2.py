data_dict = {
		"Brand":{
			"Apple":{

			}
		}
		



	}
print(data_dict)
def count():
	brand = data_dict["Brand"]
	#outfile = open("device_data.txt", "a")
	with open("devices.txt", "r") as file_in:
		file = file_in.readlines()
		for line in file:
			res = line.strip('][').split(', ') 
			if not "Apple" in res[0]:
				#brand = res[0]
				brand[res[0]] = {res[1]} 
			elif res[0] in data_dict["Brand"]:
				if brand.has_key(res[1]):
					brand[res[0]][res[1]] += 1
				elif not brand.has_key(res[1]):
					brand[res[0]][res[1]] = 1
			elif "Apple" in res[0]:
				brand["Apple"] = res[1]
		file_in.close()
outfile = open("device_data.txt", "a")
count()
print(data_dict, file=outfile)
print("Done")
outfile.close()
	

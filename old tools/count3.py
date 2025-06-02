data_dict = {
        "Brand":{
        }
    }
    
print(data_dict)                               # Just for testing purposes

def count():
	brand = data_dict["Brand"]                 
    #outfile = open("device_data.txt", "a")
	with open("devices.txt", "r") as file_in:  
		file = file_in.readlines()             
		for line in file:                     
			res = line.strip('][').split(', ') # Converts the string "lists" into actual strings
			brand_dict = res[0]
			model = res[1]
			if brand_dict not in brand:            
				brand[brand_dict] = {model:1}      # Add the brand and it's model + initiate count val
			elif brand_dict in brand:             
				brand[brand_dict][model] = brand.get(model,0) + 1 # This should increment the value
		file_in.close()

outfile = open("device_data.txt", "a")
count()                                      
print(data_dict, file=outfile)
print("Done")
outfile.close()
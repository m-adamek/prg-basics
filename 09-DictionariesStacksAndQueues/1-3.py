# Create a dictionary describing your mobile phone. Use 6 key-value pairs of data. Then, using for loop,
# display the contents of the dictionary. To read a key and value, use the items() method. Sample result:

mobile = {
"OS":"Android",
"RAM": "6GB",
"Memory": "256GB",
"Price": "900zł",
"Brand": "Huawei",
"Year": "2019"
}

for key,value in mobile.items():
   print(f"{key} : {value}")
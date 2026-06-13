import json
# import requests


# import json file  "json_data_demo.json" data into this program
# Store the content in "json_data"

try:
    with open("json_data_demo.json", "r", encoding="utf-8") as json_file:
        json_data = json.load(json_file)
        print(json_data)
except Exception as e:
    print(e)

# print the type of the content
print(type(json_data))

for key in json_data.keys():
    print("Key : ", type(key))


for value in json_data.values():
    print("Value : ", type(value))


data_p = json_data.get("data", {})
# print(data_p)

data_status_code = json_data.get("statusCode")

print("-"*40)
print(data_status_code)
print("-"*40)

data_list = json_data.get("data", {}).get("data", [])

print("-"*40)
# get list
for item in data_list:
    # get dictiionary
    height = item.get("height", {})
    for key, value in height.items():
        print(key, value)

print("-"*40)

print(type(data_list))

import requests

url = "https://bit.ly/2OU9LQb"

response = requests.get(url)

print (response.status_code)

record = response.headers
print (record)

data = response.json()
print (data["success"])
print (data["result"])


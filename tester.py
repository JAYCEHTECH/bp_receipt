import requests
import datetime

today = datetime.datetime.now()

url = f"https://r.bestpaygh.com/generate/3654943/Momo/0242442147/Michael Gyamfi/40000MB Big Time Data/300/{today}"

response = requests.request("GET", url=url)

data = response.json()
short_url = data["short_url"]
print(short_url)

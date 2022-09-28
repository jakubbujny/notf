import requests
import os


url = "https://api.apilayer.com/fixer/convert?to=PLN&from=USD&amount=1"

payload = {}
headers = {
    "apikey": os.environ['KEY']
}

response = requests.request("GET", url, headers=headers, data=payload)
result = response.json()

with open('/opt/currency.txt') as f:
    lines = f.readlines()

currentRate = result["info"]["rate"]
rateFromFile = float(lines)

if currentRate > rateFromFile:
    os.system(f"cd /opt/notf; echo '{currentRate}' > rate; git add rate; git commit -m 'mamy nowy rekord mordeczki: {currentRate}'; git push origin main")

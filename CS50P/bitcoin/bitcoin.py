import sys
import os
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
    print(n)
except ValueError:
    sys.exit("Command-line argument is not a number")

API_KEY = os.getenv("COINCAP_API_KEY")

if not API_KEY:
    sys.exit("Missing COINCAP_API_KEY environment variable")


response = requests.get(
    "https://rest.coincap.io/v3/assets/bitcoin",
    headers={
        "Authorization": f"Bearer {API_KEY}"
    }
)

data = response.json()
price = float(data["data"]["priceUsd"])

total = n * price

print(f"${total:,.4f}")

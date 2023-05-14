import requests
import json
import os.path

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
}

# Set the filename to store the list of listings
filename = "listings.txt"

params = {
    "start": "1",
    "limit": "5000",
    "convert": "USD"
}

response = requests.get(url, headers=headers, params=params)

# Check if the response was successful
if response.status_code != 200:
    print("Failed to get listings from CoinMarketCap API")
    exit()

# Parse the response data as JSON
data = json.loads(response.text)

# Check if the file exists
if os.path.exists(filename):
    # If the file exists, open it and read the contents into a list
    with open(filename, "r") as f:
        existing_listings = f.read().splitlines()
else:
    # If the file doesn't exist, create an empty list
    existing_listings = []

# Loop through the new listings and check if they are already in the existing list
new_listings = []
for listing in data["data"]:
    if listing["name"] not in existing_listings:
        # If the listing is new, add it to the new listings list and print its name
        new_listings.append(listing["name"])
        print(f"New listing added: {listing['name']}")
    # Append the new listings to the existing list and write them to the file
existing_listings += new_listings
with open(filename, "w") as f:
    for listing in existing_listings:
        f.write(listing + "\n")

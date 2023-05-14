import requests
import json
import os.path
from prettytable import PrettyTable

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
# print(data)

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
new_data = []
# print(data)
for listing in data['data']:
    if listing['name'] not in existing_listings:
        # If the listing is new, add it to the new listings list and print its name
        new_listings.append(listing['name'])       

        circulating_supply = listing['circulating_supply']
        circulating_supply_round = round(circulating_supply, 8)
        
        total_supply = listing['total_supply']
        total_supply_round = round(total_supply, 8)

        max_supply = listing['max_supply']
        max_supply_round = round(max_supply, 8)
        
        price = listing['quote']['USD']['price']
        price_round = round(price, 8)

        market_cap = listing['quote']['USD']['market_cap']
        market_cap_round = round(market_cap, 8)

        fully_diluted_market_cap = listing['quote']['USD']['fully_diluted_market_cap']
        market_cap_round = round(market_cap, 8)

        volume_24h = listing['quote']['USD']['volume_24h']
        volume_24h_round = round(volume_24h, 8)

        volume_change_24h = listing['quote']['USD']['volume_change_24h']
        volume_change_24h_round = round(volume_change_24h, 8)

        percent_change_1h = listing['quote']['USD']['percent_change_1h']
        percent_change_1h_round = round(percent_change_1h, 8)

        percent_change_24h = listing['quote']['USD']['percent_change_24h']
        percent_change_24h_round = round(percent_change_24h, 8)

        percent_change_7d = listing['quote']['USD']['percent_change_7d']
        percent_change_7d_round = round(percent_change_7d, 8)

        infinite_supply = listing['infinite_supply']             

        
        # print(f"New listing added: {listing['name'], listing['quote']}")
        print(f"New listing added: {listing['name']}, price {price_round}, market_cap {market_cap_round}, circulating_supply {circulating_supply_round}, total_supply {total_supply_round}, max_supply {max_supply}, infinite_supply {infinite_supply}, volume_24h {volume_24h_round}, volume_change_24h {volume_change_24h_round}, percent_change_1h {percent_change_1h_round}, percent_change_24h {percent_change_24h_round}, percent_change_7d {percent_change_7d_round}  ")

        
        # print(test)

        # others ##
        # circulating_supply = listing['quote']['USD']['circulating_supply']
        # total_supply = listing['quote']['USD']['total_supply']
        # max_supply = listing['quote']['USD']['max_supply']
        # infinite_supply = listing['quote']['USD']['infinite_supply']

        # print(listing['quote']['USD'])
    # Append the new listings to the existing list and write them to the file
existing_listings += new_listings
with open(filename, "w") as f:
    for listing in existing_listings:
        f.write(listing + "\n")

recently_appended = existing_listings[-20:]
print(f"20 most recently appended listings: {recently_appended}")
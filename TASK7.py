#1.

import requests

class CountryData:
    def __init__(self, url):
        self.url = url
        self.data = self.fetch_data()

    # Method to fetch data from the given URL
    def fetch_data(self):
        response = requests.get(self.url)
        return response.json()

    # Method to display countries with Dollar as currency
    def countries_with_dollar(self):
        countries = []
        for country in self.data:
            if 'USD' in country.get('currencies', {}):
                countries.append(country['name']['common'])
        return countries

    # Method to display countries with Euro as currency
    def countries_with_euro(self):
        countries = []
        for country in self.data:
            if 'EUR' in country.get('currencies', {}):
                countries.append(country['name']['common'])
        return countries

# URL for the API
url = "https://restcountries.com/v3.1/all"

# Instantiate the class with the provided URL
country_data = CountryData(url)

# Display countries with Dollar as currency
print("Countries with Dollar as currency:")
for country in country_data.countries_with_dollar():
    print(country)

# Display countries with Euro as currency
print("\nCountries with Euro as currency:")
for country in country_data.countries_with_euro():
    print(country)


#2.


import requests

# Define the states you are interested in
states = ['Alaska', 'Maine', 'New York']

# Base URL for Open Brewery DB API
url = "https://api.openbrewerydb.org/breweries"

# Function to get breweries in a state
def get_breweries(state):
    response = requests.get(f"{url}?by_state={state}")
    return response.json()

# 1. List the names of all breweries in Alaska, Maine, and New York
breweries = {}
for state in states:
    breweries[state] = [brewery['name'] for brewery in get_breweries(state)]

# Print the breweries
for state, names in breweries.items():
    print(f"\nBreweries in {state}:")
    for name in names:
        print(name)

# 2. Count the number of breweries in each state
for state in states:
    print(f"\nNumber of breweries in {state}: {len(breweries[state])}")

# 3. Count the number of types of breweries in each city
from collections import defaultdict

city_breweries = defaultdict(lambda: defaultdict(int))

for state in states:
    for brewery in get_breweries(state):
        city_breweries[brewery['city']][brewery['brewery_type']] += 1

# Print the brewery types in each city
for state in states:
    print(f"\nBrewery types in cities in {state}:")
    for city, types in city_breweries.items():
        print(f"City: {city}")
        for type_, count in types.items():
            print(f"  {type_}: {count}")

# 4. Count how many breweries have websites
breweries_with_websites = {state: 0 for state in states}

for state in states:
    for brewery in get_breweries(state):
        if brewery['website_url']:
            breweries_with_websites[state] += 1

# Print the count of breweries with websites
for state, count in breweries_with_websites.items():
    print(f"\nNumber of breweries with websites in {state}: {count}")

#!/usr/bin/env python3
import requests
import json
from geodatahelper import get_geodata_for_country

corona_api_url2 = "https://corona.lmao.ninja/countries"
corona_api_url = "https://coronavirus-19-api.herokuapp.com/countries"
country_codes_url = "http://country.io/names.json"

raw_corona_data = requests.get(corona_api_url).json()

if bool(raw_corona_data) == False:
    raw_corona_data = requests.get(corona_api_url2).json()

updated_corona_data = []

for country in raw_corona_data:
    country_name = country['country']
    
    if country_name == "Diamond Princess":
        continue

    country['country_code'] = get_geodata_for_country(country_name)
    updated_corona_data.append(country)

output = json.dumps(updated_corona_data, indent=2, ensure_ascii=False)

with open("./coronadata.json", "w") as file:
    file.write(output)

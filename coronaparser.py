#!/usr/bin/env python3
import pycountry
import requests
import json

corona_api_url2 = "https://corona.lmao.ninja/countries"
corona_api_url = "https://coronavirus-19-api.herokuapp.com/countries"
country_codes_url = "http://country.io/names.json"

raw_corona_data = requests.get(corona_api_url).json()

if bool(raw_corona_data) == False:
    raw_corona_data = requests.get(corona_api_url2).json()

updated_corona_data = []

for country in raw_corona_data:
    country_name = country['country']

    if country_name == 'UK':
        country['country_code'] = 'GBR'
        continue

    if country_name == 'S. Korea':
        country['country_code'] = 'KOR'
        continue

    if country_name == 'St. Barth':
        country_name = 'Saint Barthelemy'

    if country_name == 'Diamond Princess':
        continue

    if country_name == 'UAE':
        country['country_code'] = 'UAE'
        continue

    if country_name == 'Faeroe Islands':
        country['country_code'] = 'FRO'
        continue

    if country_name == 'Ivory Coast':
        country['country_code'] = 'CIV'
        continue

    if country_name == 'Channel Islands':
        country['country_code'] = 'GSY'
        continue

    if country_name == 'DRC':
        country['country_code'] = 'DRC'
        continue

    if country_name == 'St. Vincent Grenadines':
        country['country_code'] = 'VCT'
        continue

    if country_name == 'U.S. Virgin Islands':
        country['country_code'] = 'VIR'
        continue

    country['country_code'] = pycountry.countries.search_fuzzy(country_name)[0].alpha_3
    updated_corona_data.append(country)

print(json.dumps(updated_corona_data))


import json

# import geodata
with open("./AT-GeoData.json") as json_file:
    at_geodata = json.load(json_file)

with open("./WORLD-GeoData.json") as json_file:
    world_geodata = json.load(json_file)

def get_geodata_for_district(key):
    for district in at_geodata:
        if district['name'] == key:
            return district['geodata']

def get_geodata_for_country(key):
    for country in world_geodata:
        if country['country_name'] == key:
            return country['country_code']

print(get_geodata_for_country("UK"))

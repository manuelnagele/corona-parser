import json

# import geodata
with open("AT-GeoData.json") as json_file:
        geodata = json.load(json_file)

def get_geodata_for_district(key):
    for district in geodata:
        if district['name'] == key:
            return district['geodata']


print(get_geodata_for_district('Wien 23., Liesing'))

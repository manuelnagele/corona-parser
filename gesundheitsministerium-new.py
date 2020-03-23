#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
from jsonpath_ng import jsonpath, parse
from datetime import date
import ast
import codecs

ministerium_url = "https://info.gesundheitsministerium.at/data/"

trend_query = "Trend"
gender_distribution_query = "Geschlechtsverteilung"
age_distribution_query = "Altersverteilung"
districts_query = "Bezirke"
provinces_query = "Bundesland"
simpledata_query = "SimpleData"

json_queries = [trend_query, gender_distribution_query, age_distribution_query, districts_query, provinces_query]

def get_ministerium_data(query):
    print("Current Query: " + query)
    response = requests.get(ministerium_url + query + ".js").text
    raw_data = response[response.find("= [")+3:response.find("];")]
    return raw_data

def build_json(raw_data):
    data_dict = ast.literal_eval(raw_data)
    export_json = {}

    for datapoint in data_dict:
        new_point = {datapoint['label']:datapoint['y']}
        export_json.update(new_point)

    return export_json

def parse_simple_data(raw_data):
    print("Parsing Simple data...")
    erkrankungen = raw_data[raw_data.find("gen = ")+6:raw_data.find(";")]
    hospitalisiert = raw_data[raw_data.find("ert = ")+6:raw_data.find(";\nvar Int")]
    intensiv = raw_data[raw_data.find("ion = ")+6:raw_data.find(";\nvar Le")]
    
    return {"Erkrankungen":erkrankungen,"Hospitalisiert":hospitalisiert,"Intensiv":intensiv}

def build_output():
    output = parse_simple_data(get_ministerium_data(simpledata_query))

    for query in json_queries:
        current_data = {query:{}}
        current_data[query].update(build_json(get_ministerium_data(query)))
        
        output.update(current_data)
    return json.dumps(output, ensure_ascii=False)

print(build_output())

#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import ast
import codecs

ministerium_url = "https://info.gesundheitsministerium.at/data/"

gender_distribution_query = {"query" : "Geschlechtsverteilung", "label": "gender"}
age_distribution_query = {"query" : "Altersverteilung", "label":"age_group"}
districts_query = {"query" : "Bezirke", "label": "district"}
provinces_query = {"query" : "Bundesland", "label" : "province"}
simpledata_query = "SimpleData"

json_queries = [gender_distribution_query, age_distribution_query, districts_query, provinces_query]


def get_ministerium_data(query):
    response = requests.get(ministerium_url + query + ".js").text
    raw_data = response[response.find("= [")+3:response.find("];")]
    return raw_data

def build_metric(raw_data, label):
    data_dict = ast.literal_eval(raw_data)
    export_json = []

    for datapoint in data_dict:
        new_point = {label: datapoint['label'], "value": datapoint['y']}
        export_json.append(new_point.copy())
   
    return json.dumps(export_json, ensure_ascii=False)

def parse_simple_data(raw_data):
    erkrankungen = raw_data[raw_data.find("gen = ")+6:raw_data.find(";")]
    hospitalisiert = raw_data[raw_data.find("ert = ")+6:raw_data.find(";\nvar Int")]
    intensiv = raw_data[raw_data.find("ion = ")+6:raw_data.find(";\nvar Le")]

    return {"Erkrankungen":erkrankungen,"Hospitalisiert":hospitalisiert,"Intensiv":intensiv}

def build_output():
    metrics = parse_simple_data(get_ministerium_data(simpledata_query))

    for query in json_queries:
        label = query['label']
        query = query['query']
        
        current_data = ast.literal_eval(build_metric(get_ministerium_data(query), label))
        metrics[query] = current_data

    print(json.dumps(metrics, ensure_ascii=False))

build_output()

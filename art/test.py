# -*- coding: utf-8 -*-
'''
This function get a string as input if input is one digit add a zero
:param input_string: input digit az string
:type input_string:str
:return: modified output as str
>>> from csv2yaml import *
>>> import coverage
>>> import json
>>> import yaml
>>> import pickle
>>> cov = coverage.Coverage(omit=['*/home/travis/virtualenv/python3.5.3/lib/python3.5/site-packages/yaml/*'])
>>> cov.start()
>>> convert_bytes(200)
'200.0 bytes'
>>> convert_bytes(6000)
'5.9 KB'
>>> convert_bytes(80000)
'78.1 KB'
>>> zero_insert("22")
'22'
>>> zero_insert("320")
'320'
>>> zero_insert("2")
'02'
>>> zero_insert(22)
Traceback (most recent call last):
        ...
TypeError: object of type 'int' has no len()
>>> time_convert('33')
'00 days, 00 hour, 00 minutes, 33 seconds'
>>> time_convert("15000")
'00 days, 04 hour, 10 minutes, 00 seconds'
>>> time_convert("sadasdasd")
Traceback (most recent call last):
        ...
ValueError: could not convert string to float: 'sadasdasd'
>>> json_size=json_convert("test.csv")
>>> file=open("test.json","r")
>>> testfile_1=json.load(file)
>>> testfile_1["test"]["data"][1]["Node1"]
'1'
>>> testfile_1["test"]["data"][1]["Node2"]
'5'
>>> yaml_size=json_to_yaml("test.json")
>>> file=open("test.yaml","r")
>>> testfile_1_yaml=yaml.load(file)
>>> testfile_1_yaml["test"]["data"][1]["Node1"]
'1'
>>> testfile_1_yaml["test"]["data"][1]["Node2"]
'5'
>>> pickle_size=json_to_pickle("test.json")
>>> testfile_1_p=pickle.load( open( "test.p", "rb" ) )
>>> testfile_1_p["test"]["data"][1]["Node1"]
'1'
>>> testfile_1_p["test"]["data"][1]["Node2"]
'5'
>>> json_size=json_convert("test.csv","header_test")
>>> file=open("test.json","r")
>>> testfile_1=json.load(file)
>>> testfile_1["header_test"]["data"][1]["Node1"]
'1'
>>> testfile_1["header_test"]["data"][1]["Node2"]
'5'
>>> yaml_size=json_to_yaml("test.json")
>>> file=open("test.yaml","r")
>>> testfile_1_yaml=yaml.load(file)
>>> testfile_1_yaml["header_test"]["data"][1]["Node1"]
'1'
>>> testfile_1_yaml["header_test"]["data"][1]["Node2"]
'5'
>>> pickle_size=json_to_pickle("test.json")
>>> testfile_1_p=pickle.load( open( "test.p", "rb" ) )
>>> testfile_1_p["header_test"]["data"][1]["Node1"]
'1'
>>> testfile_1_p["header_test"]["data"][1]["Node2"]
'5'
>>> cov.stop()
>>> cov.save()

'''
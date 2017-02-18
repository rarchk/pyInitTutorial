#!/usr/bin/env python3
__author__ = 'Ronak Kogta<rixor786@gmail.com>'
__description__ = \
''' Compute distance between two places '''

_GOOGLE_MAPS_API_KEY_ = 'AIzaSyBue7-3iFFTNsWJjIPrlSVNm1i9HRvrkoA'

import argparse;  
import requests;
import json; 

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = __description__);
	parser.add_argument('-s','--source', help='multiple space entry should be inserted within quotes', required=True);
	parser.add_argument('-d','--destination', help='multiple space entry should be inserted within quotes', required=True);
	args = parser.parse_args();

	Query = "https://maps.googleapis.com/maps/api/distancematrix/json?units=si&origins="
	Query += "+".join(args.source.split(" "));
	Query += "&destinations=" + "+".join(args.destination.split(" "))
	Query += ";&key=" + _GOOGLE_MAPS_API_KEY_
	
	with requests.Session() as s:
		response = s.get(Query);
		
		jsonData = json.loads(response.text);
		try:
			print(jsonData['rows'][0]['elements'][0]['distance']['text']);
			print(jsonData['rows'][0]['elements'][0]['duration']['text']);
		except Exception as e:
			print ("Cannot find distance/time betwen two, as two places can be in different countries");

			







import requests
import json
from globals import cacheDictIndex
from utils import *
import datetime
import time
from draw import *

def getData(inputCountryISO,dataType, lastNDays, dayChoosen):
	lastNDays = int(lastNDays)
	dataTypeLegend = dataType
	dataType = dataTypeValues[dataType]
	json_data = ""
	if inputCountryISO in cacheDictIndex:
		# data cached
		with open(f'../data/cache/{inputCountryISO}.json') as fp:
		    r = json.load(fp)
		timeline = r['data']['timeline']
		countryName = r['data']['name']
	else:
		cacheDictIndex.append(inputCountryISO)
		r = requests.get(f'https://corona-api.com/countries/{inputCountryISO}')

		# save data to cache
		json_data = r.json()
		with open(f'../data/cache/{inputCountryISO}.json', 'w') as f:
			json.dump(json_data, f)
		f.close()

		countryName = json_data['data']['name']
		timeline = json_data['data']['timeline']

	dataTypeList = []
	dateList = []

	fecha = datetime.datetime.today().weekday()
	fecha = datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)
	datetime.datetime.today().weekday()

	if(dayChoosen == "NO"):
		allDays = True

	for i in range(0, len(timeline)):
		rawDate = formatMyDate(timeline[i]['date'])		
		dayOfWeek = datetime.datetime(int(timeline[i]['date'][0:4]), int(rawDate[3:5]), int(rawDate[0:2]), 1, 1, 1, 173504).weekday()
		if( (dayChoosen != "NO") and (dayOfWeek != customIndex(dayChoosen, weekDict)) ):
			continue
		else:
			dataTypeList.insert(0, timeline[i][dataType])
			dateList.insert(0, rawDate)

	# Data for plotting
	s = dateList[-lastNDays:]
	t = dataTypeList[-lastNDays:]
	drawFigure(s,t,dayChoosen,lastNDays, countryName, dataTypeLegend)
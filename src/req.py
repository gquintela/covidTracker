import requests
import json
from globals import cacheDict
from utils import formatMyDate, weekDict, dataTypeValues, customIndex
import datetime
import time
from draw import drawFigure

def getData(inputCountryISO,dataType, lastNDays, dayChoosen):
	lastNDays = int(lastNDays)
	dataTypeLegend = dataType
	dataType = dataTypeValues[dataType]
	json_data = ""
	if inputCountryISO not in cacheDict:
		r = requests.get(f'https://corona-api.com/countries/{inputCountryISO}')

		# save data to cache
		cacheDict[inputCountryISO] = r.json()

	countryName = cacheDict[inputCountryISO]['data']['name']
	timeline = cacheDict[inputCountryISO]['data']['timeline']

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
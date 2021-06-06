def formatMyDate(date):
	return date[8] + date[9] + date[7] + date[5] + date[6]

weekDict = ['Mondays',
			'Tuesdays',
			'Wednesdays',
			'Thursdays',
			'Fridays',
			'Saturdays',
			'Sundays']
			
dataTypeValues = {"Deaths": "deaths" ,
				"Confirmed": "confirmed",
				"Recovered": "recovered",
				"New confirmed": "new_confirmed",
				"New Recovered": "new_recovered",
				"New Deaths": "new_deaths",
				"Active": "active"}

def customIndex(e, list):
	i = 0
	for element in list:
		if(e == element):
			return i
		i += 1
	return -1
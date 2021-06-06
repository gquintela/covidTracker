import json

def getCountries():
	countries = []
	f = open('../data/countriesISO.json', 'r')
	data = json.load(f)
	for country in data:
		countries.append(country["Name"])
	f.close()
	return countries

def getISO(inputCountry):
	f = open('../data/countriesISO.json', 'r')
	data = json.load(f)
	for country in data:
		if(inputCountry == country["Name"]):
			f.close()
			return country["Code"]
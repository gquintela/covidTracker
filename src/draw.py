import matplotlib.pyplot as plt
import numpy as np

def drawFigure(s,t,dayChoosen,lastNDays, countryName, dataTypeLegend):
	fig, ax = plt.subplots()
	ax.plot(s, t, color='green')

	if(dayChoosen != "NO"):
		title = f'Coronavirus: last {lastNDays} {dayChoosen} in {countryName}'
	else:
		title = f'Coronavirus: last {lastNDays} days in {countryName}'

	ax.set(xlabel='day(s)', ylabel=dataTypeLegend,
		title=title)
	ax.grid()
	plt.xticks(rotation = 90)

	plt.show(block=False)

def drawDualFigure(queryCountryParams, argParams):
	s,t,dayChoosen,lastNDays, countryName, dataTypeLegend = queryCountryParams
	u, v, _,_, countryNameAr, _ = argParams

	fig, ax = plt.subplots()
	ax.plot(s, t, color='green')
	ax.plot(u,v, color ='blue')

	if(dayChoosen != "NO"):
		title = f'Coronavirus: last {lastNDays} {dayChoosen} in {countryName}'
	else:
		title = f'Coronavirus: last {lastNDays} days in {countryName}'
	if(dataTypeLegend == "Confirmed per 100.000"):
		title = title + " (green) vs Argentina (blue)"

	ax.set(xlabel='day(s)', ylabel=dataTypeLegend,
		title=title)
	ax.grid()
	plt.xticks(rotation = 90)

	plt.show(block=False)

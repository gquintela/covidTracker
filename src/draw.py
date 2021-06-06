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


	# fig.savefig("test.png")
	plt.show(block=False)
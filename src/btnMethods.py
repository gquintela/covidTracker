from inputChecks import isInputValidated
from req import getData
from countryMethods import getISO
from tkinter import messagebox
import os
from draw import drawFigure, drawDualFigure


def reset(countryMenu, dataTypeMenu, days, weekdayMenu, infoLbl):
	countryMenu.selection_clear()
	countryMenu.set("Select a country")
	dataTypeMenu.selection_clear()
	dataTypeMenu.set("Select a data type")
	days.set("")
	weekdayMenu.selection_clear()
	weekdayMenu.set("NO")
	infoLbl['text'] = ""
	countryMenu.focus()


def run(countryMenu, dataTypeMenu, days, weekdayMenu, infoLbl):
	if (not isInputValidated(countryMenu.get(),dataTypeMenu.get(), days)):
		# reset(countryMenu, dataTypeMenu, days, weekdayMenu, infoLbl)
		infoLbl['text'] = "Please check the input"
	else:
		infoLbl['text'] = "Proccessing..."
		s,t,dayChoosen,lastNDays, countryName, dataTypeLegend = getData(getISO(countryMenu.get()),dataTypeMenu.get(), days.get(), weekdayMenu.get())
		if(dataTypeMenu.get() != "Confirmed per 100.000"):
			drawFigure(s,t,dayChoosen,lastNDays, countryName, dataTypeLegend)
		else:
			queryCountryParams = [s,t,dayChoosen,lastNDays, countryName, dataTypeLegend]
			u,v,dayChoosenAr,lastNDaysAr, countryNameAr, dataTypeLegendAr = getData("AR",dataTypeMenu.get(), days.get(), weekdayMenu.get())
			argParams = [u,v,dayChoosenAr,lastNDaysAr, countryNameAr, dataTypeLegendAr]
			drawDualFigure(queryCountryParams, argParams)

		infoLbl['text'] = ""

def changeDaysLabel(window, label):
	label = "LAST N WEEKS:"
	window.update()
from inputChecks import isInputValidated
from req import getData
from countryMethods import getISO
from tkinter import messagebox
import os

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
		getData(getISO(countryMenu.get()),dataTypeMenu.get(), days.get(), weekdayMenu.get())
		infoLbl['text'] = ""

def changeDaysLabel(window, label):
	label = "LAST N WEEKS:"
	window.update()
	print("cambiose")
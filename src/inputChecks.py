def isInputValidated(country,dataType, days):
	return isCountrySelected(country) and isDataTypeSelected(dataType) and isDaysOk(days)

def isCountrySelected(country):
	return country != "Select a country"

def isDataTypeSelected(dataType):
	return dataType != "Select a data type"

def isDaysOk(days):
	return days.get().isnumeric() and (int(days.get()) > 0) and (int(days.get()) < 181) 
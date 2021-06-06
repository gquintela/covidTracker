import json
import sys
from tkinter import *
from btnMethods import *
from countryMethods import *
from globals import *
from tkinter import ttk
from utils import *

window = Tk()
window.title("Corona tracking API")
# window.geometry('400x200')
# background_image = PhotoImage(file="../data/background.png")
# background_label = Label(window, image=background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)

backgroundColor = "#41B3A3"
backgroundBoxColor = "#52C4B4"

window.configure(bg=backgroundColor)
combostyle = ttk.Style()
combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': 'teal',
                                       'fieldbackground': 'teal',
                                       'font': mainFont
                                       }}}
                                    )
combostyle.theme_use('combostyle')

# variables
cacheDict = {}
country = StringVar(window)
country.set("Select a country")
days = StringVar(window)
days.set("")
getOneDay = False
dayChoosen = StringVar(window)
dayChoosen.set("NO")
dataType = StringVar(window)
dataType.set("Select a data type")


###labels
countryLbl = Label(window, text="COUNTRY:", font=(mainFont + " Bold", mainFontSize), bg = backgroundColor)
dataTypeLbl = Label(window, text="DATA TYPE:", font=(mainFont + " Bold", mainFontSize), bg = backgroundColor)
daysLbl = Label(window, text="LAST N DAYS:", font=(mainFont + " Bold", mainFontSize), bg = backgroundColor)
weekDayLbl = Label(window, text="ONLY WEEK DAY?", font=(mainFont + " Bold", mainFontSize), bg = backgroundColor)
infoLbl = Label(window, text="", font=(mainFont + " Bold", mainFontSize), bg = backgroundColor)



###input

#country
options = getCountries()

countryMenu_width = len(max(options,"Choose a country",  key=len)) 
countryMenu = ttk.Combobox(window,textvariable=country, state='readonly', 
                            values = options, justify='center')

#days
daysEntry = Entry(window,textvariable = days, font=(mainFont,mainFontSize),
                    width=10, justify='center')

daysEntry.config({"background": "teal"})


#weekday
weekdayMenu = ttk.Combobox(window,textvariable=dayChoosen, state='readonly',
                            values = weekDict, justify='center')
weekdayMenu.bind("<<ComboboxSelected>>",lambda e: window.focus())

#dataType
dataTypeMenu = ttk.Combobox(window,textvariable=dataType, state='readonly',
                            values = list(dataTypeValues.keys()), justify='center')

###Buttons

runBtn = Button(window, text="RUN", font=(mainFont,mainFontSize), width= 14,
                command=lambda: run(countryMenu, dataTypeMenu, days,weekdayMenu, infoLbl))
resetBtn = Button(window, text="RESET", font=(mainFont,mainFontSize),
                command= lambda: reset(countryMenu, dataTypeMenu, days, weekdayMenu, infoLbl))

runBtn.config({"background": "MediumSeaGreen"})
resetBtn.config({"background": "MediumSeaGreen"})


### grid

Grid.rowconfigure(window, 0, weight=1)
Grid.columnconfigure(window, 0, weight=1)


countryLbl.grid(
    column=0,
    row=1,
    sticky='nsew',
    padx=padx, pady=pady,    
)

countryMenu.grid(
    column=2,
    row=1,
    padx=padx, pady=pady,
    sticky='nsew',
    )

dataTypeLbl.grid(
    column=0,
    row=2,
    sticky='nsew',
    padx=padx, pady=pady,    
)

dataTypeMenu.grid(
    column=2,
    row=2,
    sticky='nsew',
    padx=padx, pady=pady
)

daysLbl.grid(
    column=0,
    row=3,
    sticky='nsew',
    padx=padx, pady=pady
)

daysEntry.grid(
	column=2,
    sticky='nsew',
    padx=padx, pady=pady,    
	row=3)

weekDayLbl.grid(
    column=0,
    row=4,
    sticky='nsew',
    padx=padx, pady=pady,    
)

weekdayMenu.grid(
    column=2,
    row=4,
    sticky='nsew',
    padx=padx, pady=pady
)

resetBtn.grid(
	column=0,
    sticky='nsew',
    padx=padx, pady=pady,    
	row=5)

runBtn.grid(
	column=1,
    sticky='nsew',
    padx=padx, pady=pady,    
    columnspan=2,
	row=5)

infoLbl.grid(
    column=0,
    sticky='nsew',
    padx=padx, pady=pady,   
    columnspan=4,
    row=6)

window.protocol('WM_DELETE_WINDOW', lambda: deleteCache(window))
window.mainloop()


mainFontSize = 15
mainFont = "Cambria"
padx = 5
pady = 5
cacheDict = {}

def get_list_of_days():
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    out = []
    for i in range(0, len(month_days)):
        for j in range(1, month_days[i]+1):
            day = str(j)
            month = str(i+1)
            if len(day) != 2:
                day = "0" + day
            if len(month) != 2:
                month = "0" + month
            out.append(day + "-" + month)
    return out

list_of_days = get_list_of_days()

print(list_of_days)

def get_corrected_date(bad_date):
    if bad_date == "01-01":
        return "31-12"
    index = list_of_days.index(bad_date)
    index -= 1
    return list_of_days[index]

import tkinter as tk
import requests
from urllib import request
import csv


root = tk.Tk()
root.geometry("%dx%d+%d+%d" % (1200, 800, 0, 0))
root.title("Data sets for Research")


def select():
    sf = "https://www.alphavantage.co/query?function=%s&symbol=%s&interval=%s&outputsize=%s&apikey=D2SIPR22CQB0&datatype=%s" % (TimeS.get(),Equity.get(),Interval.get(),OS.get(), DataT.get())
    print(sf)
    return sf



Equity = tk.StringVar(root)
Equity.set('AMZN')
choices = ['IBM', 'FB', 'AMZN', 'MSFT','AAPL']
option = tk.OptionMenu(root, Equity, *choices)
option.pack(side='left', padx=10, pady=10)

TimeS= tk.StringVar(root)
TimeS.set('TIME_SERIES_INTRADAY')
choices = ['TIME_SERIES_INTRADAY', 'TIME_SERIES_DAILY', 'TIME_SERIES_DAILY_ADJUSTED', 'TIME_SERIES_WEEKLY', 'TIME_SERIES_WEEKLY_ADJUSTED', 'TIME_SERIES_MONTHLY', 'TIME_SERIES_MONTHLY_ADJUSTED']
option = tk.OptionMenu(root, TimeS, *choices)
option.pack(side='left', padx=10, pady=10)

Interval = tk.StringVar(root)
Interval.set('1min')
choices = ['1min', '5min', '15min', '30min', '60min']
option = tk.OptionMenu(root, Interval, *choices)
option.pack(side='left', padx=10, pady=10)

OS = tk.StringVar(root)
OS.set('compact')
choices = ['compact', 'full']
option = tk.OptionMenu(root,OS, *choices)
option.pack(side='left', padx=10 , pady=10)

DataT = tk.StringVar(root)
DataT.set('csv')
choices = ['csv', 'json']
option = tk.OptionMenu(root, DataT, *choices)
option.pack(side='left',padx=10, pady=10)

T = tk.Text(root, height=150,width=200)


Response = requests.get(select())
def printWindow():
    T.insert('end',"Data sets for equity ::: "+ Equity.get()+"\n\n")
    T.insert('end', select())
    T.insert('end', '\n\n')

    csv =Response.text
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    for line in lines:
        T.insert('end',line)
    T.insert('end','\n')



button = tk.Button(root, text="Get DataSets!", command=printWindow)
button.pack(side='left', padx=10, pady=10)

S=tk.Scrollbar(root)
T.pack(side='bottom')



root.mainloop()




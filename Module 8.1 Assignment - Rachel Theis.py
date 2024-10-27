#Rachel Theis
#CSD 200
#9/29/24

#This program will use a dictionary to look up stock values as prompted by user input.

stock_data = {
    "XOM" : "115.82",
    "GE" : "185.38",
    "MSFT" : "428.02",
    "BP" : "31.42",
    "C" : "61.87",
    "PG" : "173.55",
    "WMT" : "79.78",
    "PFE" : "29.09",
    "TM" : "182.82",
    "JNJ" : "161.40",
    "BAC" : "39.40",
    "AIG" : "73.34",
    "NVS" : "121.35"
}

stock_query = input("Enter stock symbol here: ").upper()
#added .upper() to mitigate case sensitivity issue

try:
    print(f"{stock_query} is currently valued at: ${stock_data[stock_query]}")
except KeyError:
    print("Sorry, this stock symbol is not in the dictionary yet.")
    
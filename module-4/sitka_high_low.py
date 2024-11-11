#Rachel Theis
#Module 4.2 Assignment
#CSD 325
#11.10.24

#This program will use weather data to display a line graph of high or low temperatures in Sitka, AK (2018). 

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt
filename = 'sitka_weather_2018_simple.csv'

def read_file(filename):
#encapsulating reading the file in a function
    dates, highs, lows = [], [], []
    #initializing lows 
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)
            low = int(row[6])
            lows.append(low)
            #appending lows from csv
    return dates, highs, lows
    #adding return command to function
    
def high_temperatures(dates, highs):
#adding a function to create a plot for high temps
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    plt.title("Daily high temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
    
def low_temperatures(dates, lows):
#adding a similar function for low temps
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')
    #changing line color to blue
    plt.title("Daily low temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
    
def main():
    #adding a main function to take user input and call a function based on input
    while True:
    #adding a while loop 
        dates, highs, lows = read_file(filename)  
        temp_selection = input(
            'Welcome to the weather program! \nTo see high temperatures, enter "high:".\nTo see low temperatures, enter "low".\nTo exit the program, enter "exit".\n').lower()
        #adding welcome message and .lower() to mitigate capitalization errors
        if temp_selection == 'high':
            high_temperatures(dates, highs)
        #calling high_temperature function responsive to user input
        elif temp_selection == 'low':
            low_temperatures(dates, lows)
        #calling low_temperature function responsive to user input 
        elif temp_selection == 'exit':
            print("Thank you for using the weather program!")
        #ending program if user prompts to end
            sys.exit(0)
        #end processes
        else:
            print("Invalid input. Please try again.")
            #adding error handling 
            
if __name__ == "__main__":   
    main()
#calling main function
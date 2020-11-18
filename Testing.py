import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join("PyBank","Resources","budget_data.csv")

# Define the function and have it accept the 'wrestlerData' as its sole parameter
#def print_percentages(wrestler_data):
    #name = str(wrestler_data[0])
   # wins = int(wrestler_data[1])
    #losses = int(wrestler_data[2])
    #draws = int(wrestler_data[3])
    #total = (wins + losses + draws)
    #percentwon = (wins / total) * 100
    #percentloss = (loss / total) * 100
    #percentdrawn = draws / total) * 100

    #if percent_loss > 50
        #type of wrestler = "Jobber"
    #else
        #type of wrestler = "Superstar"
   

# Read in the CSV file
with open(budget_data, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    lines = len(list(csvreader))
    #print(lines)
    count = 0
    maxnum = 0
    # Loop through the data
    for row in csvreader:
        if row[1] > maxnum:
            maxnum == row[1]


            print(maxnum)

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        #count = count + 1
        

    #print(count)
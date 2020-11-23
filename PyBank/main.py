import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join("Resources","budget_data.csv")

# Initial Lists and variable setup
MonthTot = []
ProfitLoss = 0
ProfitTot = []
OldProfitLoss = 0
LossChange = 0
ProfitLoss_change_list = []
Change_Month = []

# Read the CSV and split at the commas
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Month and Profit totals gathering loop.
    for row in csvreader:
        MonthTot.append(row[0])
        ProfitTot.append(int(row[1]))

    # Setting calculation variables
    i = 1
    j = 0
    Count = len(MonthTot)

    ChangeDiff = (ProfitTot[1] - ProfitTot[0])

    Change_List = []

    SubCount = Count -1
    # Profit Difference Calculation Loop 
    for month in range(SubCount):
        ChangeDiff = (ProfitTot[i] - ProfitTot[j])
        Change_List.append(int(ChangeDiff))
        i += 1
        j += 1

    Change_Month = round(sum(Change_List)/(SubCount),2)

    # Setting Max/Min change variables
    MaxNum = max(Change_List)
    MinNum = min(Change_List)

    MinChange = Change_List.index(MinNum)
    MaxChange = Change_List.index(MaxNum)

    MonthMaxChange = MonthTot[MaxChange + 1]
    MonthMinChange = MonthTot[MinChange + 1]

# Printing Financial Output
print("Financial Analysis")
print("------------------")
print(f"Total Months: {len(MonthTot)}")
print(f"Total: ${sum(ProfitTot)}")
print(f"Average Change: ${Change_Month}")
print(f"Greatest Increase In Profits: {MonthMaxChange} (${MaxNum})")
print(f"Greatest Decrease In Profits: {MonthMinChange} (${MinNum})")

#  Set variable for output file
output_file = os.path.join("analysis","analysis.txt")

#  Output files
with open(output_file, "w", newline="") as text:
    text.write("Financial Analysis\n")
    text.write("------------------------------\n")
    text.write(f"Total Months: {len(MonthTot)}\n")
    text.write(f"Total : ${sum(ProfitTot)}\n")
    text.write(f"Average Change: ${Change_Month}\n")
    text.write(f"Greatest Increase In Profits: {MonthMaxChange} (${MaxNum})\n")
    text.write(f"Greatest Increase In Profits: {MonthMinChange} (${MinNum})\n")

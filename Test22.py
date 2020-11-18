import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join("PyBank","Resources","budget_data.csv")

MonthTot = 0
ProfitLoss = 0
OldProfitLoss = 0
LossChange = 0
ProfitLoss_change_list = []
Change_Month = []

with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        MonthTot = MonthTot + 1
        ProfitLoss = ProfitLoss + int(row["Profit/Losses"])
        LossChange = int(row["Profit/Losses"]) - OldProfitLoss
        OldProfitLoss = int(row["Profit/Losses"])
        Change_Month = Change_Month + [row["Date"]]

    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {MonthTot}")
    print(f"Total Profit/Losses: ${ProfitLoss}")
        

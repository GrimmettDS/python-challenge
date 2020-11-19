import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join("Resources","budget_data.csv")

MonthTot = []
ProfitLoss = 0
ProfitTot = []
OldProfitLoss = 0
LossChange = 0
ProfitLoss_change_list = []
Change_Month = []

with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        MonthTot.append(row[0])
        ProfitTot.append(int(row[1]))

    i = 1
    j = 0
    month_count = len(MonthTot)

    ChangeDiff = (ProfitTot[1] - ProfitTot[0])

    Change_List = []

    for month in range(month_count-1):
        ChangeDiff = (ProfitTot[i] - ProfitTot[j])
        Change_List.append(int(ChangeDiff))

    Change_Month = round(sum(Change_List)/(month_count -1),2)

    MaxNum = max(Change_List)
    MinNum = min(Change_List)

    MinChange = Change_List.index(MinNum)
    MaxChange = Change_List.index(MaxNum)

print(f"{Change_Month}")
print(f"{MaxNum}")
print(f"{MinNum}")
print(f"{MinChange}")
print(f"{MaxChange}")
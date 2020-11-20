import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join("Resources","election_data.csv")

VoteTotal = 0
Candidates = []
VotePercent
EachCanVote

with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        if row[2] in Candidates
            VoteTotal += 1
        else:
            Candidates.append(row[2])
            VoteTotal += 1


print("Election Results")
print("----------------------------")
print(f"{VoteTotal}")

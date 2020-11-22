import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join("Resources","election_data.csv")

# Lists and variable setup
VoteTotal = 0
Votes = {}
VotePercent = []
MainList = []

# Read the CSV and split at the commas
with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        MainList.append(row[2])

VoteTotal = len(MainList)

# Vote Total Output Results
print("Election Results")
print("------------------------------")
print(f"Total Votes: {VoteTotal}")
print("------------------------------")  

# Setting Vote Variables
i = 0  # Current Vote Count
j = 0  # Previous Vote Count
Candidates = []
PerCandidate = []
TotCandidate = []

People = MainList[0]

# Candidate Listing Loop
for Name in MainList:
    if Name not in Candidates: 
        Candidates.append(Name)

# Candidate Vote Amount Loop
for People in Candidates:
    for VoteCount in MainList:
        if People == VoteCount:
            i += 1

    VotePercent = i / len(MainList)        
    PerCandidate.append(VotePercent)
    TotCandidate.append(i)

    if j < i:
        Winner = People

    # Candidates Vote Total Result
    print(f"{People}: {VotePercent:.3%} ({i})")

    j = i
    i = 0

# Vote Winner Results
print("------------------------------")
print(f"Winner: {Winner}")
print("------------------------------")

#  Set variable for output file
output_file = os.path.join("election_results.txt")

#  Output files
with open(output_file, "w", newline="") as text:
    text.write("Election Results\n")
    text.write("------------------------------\n")
    text.write(f"Total Votes: {VoteTotal}\n")
    text.write("------------------------------\n")

    # Loop to set Candidate totals for output
    for People in Candidates:
        Indexer = Candidates.index(People)
        text.write(f"{People}: {PerCandidate[Indexer]:.3%} ({TotCandidate[Indexer]})\n")

    text.write("------------------------------\n")
    text.write(f"Winner: {Winner}\n")


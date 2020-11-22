import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join("Resources","election_data.csv")

VoteTotal = 0
Votes = {}
VotePercent = []
# EachCanVote
# MainList = {}
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

    i = 0
    j = 0

    # Candidates Vote Total Result
    print(f"{People}: {VotePercent:.3%} ({i})")




# Print Testing    
print(Candidates)
print(VotePercent)

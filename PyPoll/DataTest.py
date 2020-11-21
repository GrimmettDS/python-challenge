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

    #for row in csvreader:
        #MainList.append(row[2])

VoteTotal = len(MainList)

    # print(csvreader)

i = 0
J = 0
Candidates = []

    # Candidate Listing and Vote Count loop
    # CandidateUno = row[2]

for Name in MainList:
    if Name not in Candidates: 
        Candidates.append(Name)
        



    VoteTotal = VoteTotal + 1

print(Candidates)

import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join("Resources","election_data.csv")

VoteTotal = 0
Candidates = []
VotePercent = []
EachCanVote

# Read the CSV and split at the commas
with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    i = 0

    # Candidate Listing and Vote Count loop
    for row in csvreader:
        if row[2] in Candidates
            VoteTotal += 1
        else:
            Candidates.append(row[2])
            VoteTotal += 1

    CandidateLength = len(Candidates)
        VoteCount = [0] * CandidateLength

    for i in range(CandidateLength)
        if row[2] == Candidates[i]
            VoteCount[i] += 1


print("Election Results")
print("----------------------------")
print(f"{VoteTotal}")

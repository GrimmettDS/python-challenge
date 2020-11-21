import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join("Resources","election_data.csv")

VoteTotal = 0

VotePercent = []
#EachCanVote

# Read the CSV and split at the commas
with open(election_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    print(csvreader)

    i = 0
    J = 0
    Candidates = []

    # Candidate Listing and Vote Count loop
    for row in csvreader:
        print(row)
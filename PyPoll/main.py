# PyPoll python challenge
# import modules
import os
import csv

file = os.path.join('..', 'PyPoll', 'election_data.csv')

# define percent for candidates
def percent(x,y):
    return (float(x) / float(y) * 100)

# variables 
TotVote = 0
kcount = 0
ccount = 0
lcount = 0
ocount = 0
MaxCount = 0

#open and read file
with open(file) as csvpoll:
    csvreader = csv.reader(csvpoll, delimiter=",") 
    csvheader = next(csvreader)

    for row in csvreader:
        voterid = row[0]
        county = row[1]
        candidate = row[2]
        TotVote = TotVote + 1
        
    # Count khan number o votes 
        if candidate == "Khan":
            kcount = kcount + 1
    # Count Correy number o votes
        if candidate == "Correy":
            ccount = ccount + 1
    # Count Li number o votes 
        if candidate == "Li":
            lcount = lcount + 1
    # Count O'Tooley number o votes  
        if candidate == "O'Tooley":
            ocount = ocount + 1
   # Create a dictionary of candiadtes and their votes  
    candidatevotes = {"Khan": kcount,"Correy":ccount,"Li":lcount,"O'Tooley":ocount}
   
    for candidate, value in candidatevotes.items():
        if value > MaxCount:
            MaxCount = value
            Winner = candidate

# Results

print("Election Results")
print("------------------------")
print(f"Total Votes: {TotVote}")
print("------------------------")
print(f"Khan: {percent(kcount, TotVote):3f}% ({kcount})")
print(f"Correy: {percent(ccount, TotVote):3f}% ({ccount})")
print(f"Li: {percent(lcount, TotVote):3f}% ({lcount})")
print(f"O'Tooley: {percent(ocount, TotVote):3f}% ({ocount})")
print("------------------------")
print(f"Winner: {Winner}")
print("------------------------")

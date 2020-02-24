# import modules
import os
import csv

file = os.path.join(...)

# define percent for candidates
def percent(Candidate_Vote, TotVote)
  return ((Cadidate_Vote / TotVote) * 100)
# variables 
TotVote = 0
kcount = 0
ccount = 0
lcount = 0
ocount = 0
MaxVotes = 0

#open and read file
with open(file) as csvpoll:
  csvreader = csv.reader(csvpoll, delimeter=',')
 
  for row in csvreader:
    voterid = row[0]
    county = row[1]
    candidate = row[2]
    
    #count khan number o votes 
    if candidate == "Khan":
      kcount = kcount + 1
    #count Correy number o votes
    if candidate == "Correy":
      ccount = ccount + 1
    #count Li number o votes 
    if candidate == "Li":
      lcount = lcount + 1
    #count O'Tooley number o votes  
    if candidate == "O'Tooley":
      ocount = ocount + 1
   # Create a dictionary of candiadtes and their votes  
   candidatevotes = ["Khan": kcount,  "Correy": kcount, "Li": lcount, "O'Tooley": ocount]
   
    for candidate, value in candidatevotes.items()
      if value > MaxCount:
        MaxCount = Value
        Winner = candidate
        
# Print results


import os
import csv

file = os.path.join(...)

def percent(Candidate_Vote, TotVote)
  return ((Cadidate_Vote / TotVote) * 100)

TotVote = 0
kcount = 0
ccount = 0
lcount = 0
ocount = 0

with open(file) as csvpoll:
  csvreader = csv.reader(csvpoll, delimeter=',')
  
  for row in csvreader:
    voterid = row[0]
    county = row[1]
    candidate = row[2]
    
    if candidate == "Khan":
      kcount = kcount + 1
    
    if candidate == "Correy":
      ccount = ccount + 1
     
    if candidate == "Li":
      lcount = lcount + 1
      
    if candidate == "O'Tooley":
      ocount = ocount + 1
      
   candidatevotes = ["Khan": kcount,  "Correy": kcount, "Li": lcount, "O'Tooley": ocount]
   
    for candidate, value in candidatevotes.items()
      if value

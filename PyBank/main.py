#python challenge
#import modules
import os 
import csv

# Download the csv file
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

# Variables
MCount = 0
Net_Total = 0
Avg_Change = 0
Max = 0
Min = 0
PreValue = 0

#Read CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    for row in csvreader:
        month = row[0]
        amount = row[1]
        intamount = int(amount)
        diff = intamount - PreValue
        
        # The greatest increase in profits
        if Max < intamount:
            Max = diff
            MaxDate = month
        # The greatest decrease in profits   
        if Min > intamount:
            Min = diff
            MinDate = month
        # How many months are in the CSV file and the sum of all of the "profits/losses"
        PreValue = intamount
        Net_Total += intamount
        MCount = MCount + 1
        print(row)

# Print Results

print("Financial Analysis")
print("-----------------------")
# Total number of months included in the data set
print(f"Total Months: {MCount}")
# Net total amount of "profit/losses" over the entire period
print(f"Total: {Net_Total}")
# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period
print(f"Greatest Increase in Profits: {MaxDate} (${Max})")
# The greatest decrease in losses (date and amount) over the entire period
print(f"Greatest Decrease in Profits: {MinDate} (${Min})")

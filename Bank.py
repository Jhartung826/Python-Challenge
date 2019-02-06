import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join('..', 'Resources', 'budget_data.csv')
#list 
difference_list = []
# Define functions
row_count = 0
total_profit = 0
change = 0
previousrow = 0
averagechange = 0
greatest = 0
least = 0
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        change = int(row[1]) - previousrow
        if previousrow == 0:
            change = 0
        if change > greatest:
            greatest = change
            greatmonth = str(row[0])
        if change < least:
            least = change
            leastmonth = str(row[0])
        difference_list.append(change)
        previousrow = int(row[1])
        # add the number of months
        row_count = row_count + 1
        #add the total profit
        total_profit = int(row[1]) + total_profit
    


# average change
averagechange = sum(difference_list)/(row_count-1)
print("                  Financial Analysis                   ")
print("-------------------------------------------------------")
print(f"total months: {row_count}")
print(f"total: {total_profit}")
print(f"Average Change: {averagechange}")
print(f"Greatest Change: {greatmonth} {greatest}")
print(f"Least Chnage: {leastmonth} {least}")
# writing the file
f = open('financial data','w')
f.write("               Financial Analysis                 "'\n')
f.write("--------------------------------------------------"'\n')
f.write(f"total months: {row_count}"'\n')
f.write(f"total: {total_profit}"'\n')
f.write(f"Average Change: {averagechange}"'\n')
f.write(f"Greatest Change: {greatmonth} {greatest}"'\n')
f.write(f"Least Chnage: {leastmonth} {least}"'\n')
f.close()
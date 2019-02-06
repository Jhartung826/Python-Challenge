import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join('..', 'Resources', 'election_data.csv')
# candidates list 
candidate_count = []
#list 
candidates = []
candidate_results = []
# Define functions
row_count = 0
candidate_number = 0
vote_count = 0
winner = 0
total_votes = 0
with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
     # fetching our candidates
        if str(row[2]) not in candidates:
            candidates.append(row[2])
        candidate_count.append(row[2])
    for x in candidates:
        vote_count = candidate_count.count(x)
        candidate_results.append(vote_count)
        vote_count = 0
    total_votes = sum(candidate_results)
    percentage = [(i/total_votes)*100 for i in candidate_results]
    f = open('election results','w')
    print("    Election Results     ")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"-------------------------")

    for x,y,z in zip(percentage, candidates, candidate_results):
        if  z > winner:
            winner = z
            president = y
        print(f"{y}: {x}% ({z})")
    print("-------------------------"'\n')
    print(f"   winner: {president}  "'\n')
    print("-------------------------"'\n')
 
    f.write("    Election Results     "'\n')
    f.write("-------------------------"'\n')
    f.write(f"Total Votes: {total_votes}"'\n')
    f.write(f"-------------------------"'\n')
    f.write(f"{y}: {x}% ({z})"'\n')
    f.write("-------------------------"'\n')
    f.write(f"   winner: {president}  "'\n')
    f.write("-------------------------"'\n')
 
 #      choice_index = int(row[2])
 #       candidate_count[choice_index] += 1
        # add the number of months
  #      row_count = row_count + 1
        #add the total profit
    
# Loop through the full pie list
 #   for pie_index in range(len(candidates)):
 #       pie_count = str(pie_purchases[pie_index])
 #       pie_name = str(pie_list[pie_index])

    # Gather the count of each pie in the pie list and print them alongside the pies
  #      print(pie_count + " " + pie_name)
  #  print(candidates)
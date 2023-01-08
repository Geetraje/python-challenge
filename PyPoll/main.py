import os
import csv

#Setting the file path
poll_csv = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

#open the file in read mode
with open(poll_csv) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")

	#Read the Header row
	csv_header = next(csv_file)
	#print(f"Header: {csv_header}")	

	
	#Initialising counters and lists
	names = []
	candidate_list = []
	votes = []
	percent= []
	div = 0
	highest = 0
	max_index = 0
	index = 0


	#Looping through the rows, converting columns to lists
	for row in csv_reader:
		votes.append(row[0])
		names.append(row[2])

	#To find individual candidate names
	for x in names:
		if x not in candidate_list:
			candidate_list.append(x)

		

	#To find number of votes for each candidate
	cand_count = len(candidate_list)
	cand_votes = [0] * cand_count
	#print (cand_votes)

	
	#To find number of votes for each candidate
	for n in names:
		for c in range(cand_count):
			if n == candidate_list[c]:
				cand_votes[c] += 1
	#print(cand_votes)
	

	#To find percentage of votes received
	for c in cand_votes:
		div = (c/ len(votes)) * 100
		div = str(round(div,3))
		percent.append(div)
	#print(percent)


	
 	#To find the winner
	highest = max(percent)
	max_index = percent.index(highest)
	#print (max_index)
	

	
	print()
	print("Election Results")
	print("--------------------------")
	print("Total Votes = " + str(len(votes)))
	print("--------------------------")
	

	#To print candidate name, the percentage and the number of votes
	for n in range(len(candidate_list)):
		print(candidate_list[n], percent[n] + "%", cand_votes[n])
		print()
	

	print("--------------------------")
	print (" Winner = " + str(candidate_list[max_index]))

	print("--------------------------")

#Setting output path to txt file	
output_path = os.path.join("..", "Analysis", "Election_results.txt")


#Opening text file to write
with open('Analysis/Election_results.txt', 'w') as f:

	f.write('\n')
	f.write("Election Results")
	f.write('\n')
	f.write('\n')
	f.write("--------------------------")
	f.write('\n')
	f.write('\n')
	f.write("Total Votes = " + str(len(votes)))
	f.write('\n')
	f.write('\n')
	f.write("--------------------------")
	f.write('\n')
	f.write('\n')

	
	for n in range(len(candidate_list)):
		temp = str(candidate_list[n]) + ":" " " + str(percent[n]) + "%" + " " + str(cand_votes[n])
		f.write(temp)
		f.write('\n')
		f.write('\n')

	
	
	f.write("--------------------------")
	f.write('\n')
	f.write('\n')
	f.write (" Winner = " + str(candidate_list[max_index]))
	f.write('\n')
	f.write('\n')
	f.write("--------------------------")

	#Close text file
	f.close()



	
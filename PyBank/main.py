import os
import csv

#Setting the file path
budget_csv = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

#open the file in read mode
with open(budget_csv) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")

	#Read the Header row
	csv_header = next(csv_file)
	#print(f"Header: {csv_header}")

	#Initialising lists and counters
	total = 0
	rowcount = 0
	profit_loss = []
	greatest_inc = 0
	greatest_dec = 0
	date_list = []
	
	
	#Looping through all the rows
	for row in csv_reader:

		date_list.append(row[0])
				
		rowcount+=1
		
		total += int(row[1])
		if row[0] == 'Jan-10':
			temp = int(row[1])
		else: 
			profit_loss.append(int(row[1]) - temp)
			temp = int(row[1])

	#To find average change
	answer = sum(profit_loss)/ len(profit_loss)
	avg_change = round(answer,2)
	#print(avg_change)

	#To find Greatest Increase in Profits and the date
	greatest_inc = max(profit_loss)
	max_index = profit_loss.index(greatest_inc) 
	

	#To find Greatest Decrease in Profits and the gate
	greatest_dec = min(profit_loss)
	min_index = profit_loss.index(greatest_dec)
	
	#Printing results to the terminal in the required format
	print()
	print("Financial Analysis")
	print()
	print("--------------------------------")
			
	print("Total months = " + str(rowcount))
	print()
	print("Total = " + "$" + str(total))
	print()
	print("Average change: " + "$" + str(avg_change))
	print()
	print("Greatest Increase in Profits: " + date_list[max_index + 1] + " " + "(" + "$" + str(greatest_inc)+ ")")
	print()
	print("Greatest Decrease in Profits: " + date_list[min_index + 1] + " " + "(" + "$" + str(greatest_dec)+ ")")

	
#Setting output path for the text file
output_path = os.path.join('../Analysis/Financials.txt')


#Open text file and write
with open('Analysis/Financials.txt', 'w') as f:

	
	#Writing to the text file in the required format
	f.write('\n')
	f.write("Financial Analysis")
	f.write('\n')
	f.write("--------------------------------")
	f.write('\n')
	f.write('\n')		
	f.write("Total months = " + str(rowcount))
	f.write('\n')
	f.write('\n')
	f.write("Total = " + "$" + str(total))
	f.write('\n')
	f.write('\n')
	f.write("Average change: " + "$" + str(avg_change))
	f.write('\n')
	f.write('\n')
	f.write("Greatest Increase in Profits: " + date_list[max_index + 1] + " " + "(" + "$" + str(greatest_inc)+ ")")
	f.write('\n')
	f.write('\n')
	f.write("Greatest Decrease in Profits: " + date_list[min_index + 1] + " " + "(" + "$" + str(greatest_dec)+ ")")

	#close text file
	f.close()

	




	



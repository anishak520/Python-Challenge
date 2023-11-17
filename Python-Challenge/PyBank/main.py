#import budget data 
import os
import csv 

# Open File

csvpath=os.path.join("/Users/anishak98/Desktop/Python-Challenge/PyBank/Resources/budget_data.csv")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# Define my variables 
    csv_header = next(csvreader)
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []
                

#Total Number of months     
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
 # Profit/Losses 
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))

 # Delta 
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
 # add profit_loss
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    monthly_change = Total / len(revenue_change)   
#Greatest Increase
    profit_increase = max(revenue_change)
    k = revenue_change.index(profit_increase)
    month_increase = month[k+1]
    
#Greatest Decrease
    profit_decrease = min(revenue_change)
    j = revenue_change.index(profit_decrease)
    month_decrease = month[j+1]


#Print Statements

print(f'Financial Analysis'+'\n')


print("Total number of months: " + str(len(month)))

print("Total Revenue in period: $ " + str(total_revenue))
      
print("Average monthly change in Revenue : $" + str(monthly_change))

print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")

print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")

#Export a text file with the results
cvspath = os.path.join("/Users/anishak98/Desktop/Python-Challenge/PyBank/Analysis/budget_data.txt")
with open(cvspath, "w") as outfile:

    outfile.write(f'Financial Analysis'+'\n')
    outfile.write("Total number of months: " + str(len(month)))
    outfile.write("Total Revenue in period: $ " + str(total_revenue))
    outfile.write("Average monthly change in Revenue : $" + str(monthly_change))
    outfile.write(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")
    outfile.write(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")
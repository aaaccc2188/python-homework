import csv
from pathlib import Path
import numpy as np

csvpath = Path("Resources/budget_data.csv")

profits_losses = []
dates = []

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
        
    for row in csvreader:
        date = row[0]
        dates.append(date)
        profit_loss = int(row[1])
        profits_losses.append(profit_loss)
     
    a = np.array(profits_losses)
    changes = np.diff(a)
    list_changes = changes.tolist()
      
    average_change = (sum(list_changes)) / len(list_changes)
      
    max_change = max(list_changes)   
    max_index = list_changes.index(max_change)
    max_change_key = dates[max_index+1]
    
    min_change = min(list_changes)
    min_index = list_changes.index(min_change)
    min_change_key = dates[min_index+1]
       
    total_profit_loss = sum(profits_losses)
    
    total_months = len(profits_losses)

print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${round(average_change,2)}")  
print(f"Greatest Increase in Profits: {max_change_key} (${max_change})")
print(f"Greatest Decrease in Profits: {min_change_key} (${min_change})")
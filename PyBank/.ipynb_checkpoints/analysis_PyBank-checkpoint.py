import os
import csv

#path to collect data from resource file
input_file = os.path.join('PyBank', 'Resources', 'budget_data.csv')
output_file = os.path.join('PyBank', 'analysis', 'PyBank_analysis.txt')

# Define variables to track financial data
total_months = 0
total_net = 0
previous_net = None
net_changes = []

#profit/loss variables
greatest_profit = float('-inf')  # Start with the lowest possible value
greatest_loss = float('inf')      # Start with the highest possible value
greatest_profit_month = ''
greatest_loss_month = ''


#open and read CSV
with open(input_file) as financial_data:
    reader = csv.reader(financial_data, delimiter=',')
    
    #skip header
    header = next(reader)
    
    print(f"CSV Header: {header}")

    #process each row of data
    for row in reader:
        total_months += 1
        
        # Parse the net amount from the current row
        current_net = int(row[1])  
        total_net += current_net
        
        #track the net change
        if previous_net is not None:
            net_change = current_net - previous_net
            net_changes.append(net_change)
            
            #greatest increase 
            if net_change > greatest_profit:
                greatest_profit = net_change
                greatest_profit_month = row[0]  
            
            # greatest loss
            if net_change < greatest_loss:
                greatest_loss = net_change
                greatest_loss_month = row[0] 
        
        # Update net amount 
        previous_net = current_net

#calculate net change
average_net_change = sum(net_changes) / len(net_changes) if net_changes else 0

#output results
print(f'Total Months: {total_months}')
print(f'Total Net: ${total_net}')
print(f'Average Change: ${average_net_change:.2f}')
print(f'Greatest Profit: {greatest_profit_month} (${greatest_profit})')
print(f'Greatest Loss: {greatest_loss_month} (${greatest_loss})')

with open(output_file, 'w') as txt_file:
    txt_file.write(f'Total Months: {total_months}\n')
    txt_file.write(f'Total Net: ${total_net}\n')
    txt_file.write(f'Average Change: ${average_net_change:.2f}\n')
    txt_file.write(f'Greatest Increase in Profits: {greatest_profit_month} (${greatest_profit})\n')
    txt_file.write(f'Greatest Decrease in Profits: {greatest_loss_month} (${greatest_loss})\n')

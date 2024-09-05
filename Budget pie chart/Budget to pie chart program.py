# Importing matplotlib and defining it as plt
import matplotlib.pyplot as plt

# Creating two lists
expenses = []
costs = []

# Opening the file in read mode
with open('budget.txt', 'r') as file:
    for line in file:
        expense, amount = line.strip().split(',')  # Unpacking the line correctly
        expenses.append(expense)  # Adding the expense to the list
        costs.append(float(amount))  # Adding the cost to the list, corrected typo
        
# Plotting data in matplotlib with a pie chart
plt.figure(figsize=(7, 7))
plt.pie(costs, labels=expenses, autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title('The pie of expenses')
plt.show()

        

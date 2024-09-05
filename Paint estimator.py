#paint estimator

#Header
print('Thank you for using our paint job quote calculator!')

#variables
laborrate = 25 #how much per hour youre paying
sqfeet = int(input('How many square feet is your home?: '))
gallons = sqfeet / 112
paintcost = gallons * 30
hoursrequired = sqfeet * 60 / 3600 # square feet x 60 seconds / 1 hour in seconds
laborcost = hoursrequired * laborrate 
totalcost = paintcost + laborcost

#output
print(f'You require {gallons:,.2f} gallons of paint, which will cost ${paintcost:,.2f}, it will take {hoursrequired:,.2f} hours to paint your space which will cost ${laborcost:,.2f} in labor.')
print(f'Your grand total for this job is ${totalcost:,.2f}. Thank you for choosing our business!')
#Car calculator
#Header
print('Hello, today I will be calculating your monthly and annual expenses related to your car!')

#Variables
loan = float(input('How much is your monthly loan payment?: '))
insurance = float(input('How much does your monthly insurance cost?: '))
gas = float(input('How much do you pay per month for gas?: '))
maintenance = float(input('How much are your monthly maintenance fees?: '))

#output

totalm = loan + insurance + gas + maintenance

totaly = totalm * 12

print(f'Your vehicle is costing you ${totalm:,.2f} per month and ${totaly:,.2f} per year.')


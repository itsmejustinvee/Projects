def main():
        #read steps
    with open('steps.txt','r') as step_tracker:
        steps_list = [int(line.rstrip('\n')) for line in step_tracker]
        
        #How many days in each month
    days_in_month = {
        'January' : 31,
        'February' : 28,
        'March' : 31,
        'April' : 30,
        'May': 31,
        'June' : 30,
        'July' : 31,
        'August' : 31,
        'September' : 30,
        'October' : 31,
        'November' : 30,
        'December' : 31
        }
    
    #Counter variables to assign step data
    start = 0
    total_over_10thou = 0
    
    #steps for each month
    for month, days in days_in_month.items():
        month_steps = steps_list[start:start + days]
        total_steps = sum(month_steps)
        average_steps = total_steps / days
        
    #days where 10,000 steps happened
        over_10thou = len([steps for steps in month_steps if steps > 10000])
        total_over_10thou += over_10thou
        
    #display results
        print(f'{month}:')
        print(f' Total steps: {total_steps}')
        print(f' Average steps per day: {average_steps:,.2f}')
        print(f' Days over 10,000 steps: {over_10thou}')
        print()
        
    #update start for the next month
        start += days
        
    #print total number of days 10,000 steps in year
    print(f'Total days over 10,000 steps in the year: {total_over_10thou}')
        
main()
        
        

CONVERSION_RATE = 0.6214

def main():
    while True:
        print('This is a Kiometers to Miles conversion calculator')
        miles, km = conversion()
        print(f'{km:,.2f} Kilometers is {miles:,.2f} Miles')
    
        recalc = input('Would you like to make another calculation? Y/N: ').strip().upper()
        if recalc !='Y':
            print("Thank you for using the conversion calculator. Have a great day!")
            break

def conversion():
    km = int(input('Plese enter the KM you wish to convert: '))
    miles = km * CONVERSION_RATE
    return miles, km

main()



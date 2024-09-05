#Hotdogs

#Hotdogs come in packs of 10 and buns come in packs of 8. How many packages of hotdogs and hotdog buns are needed for a cookout
#With the minimum amount of leftovers. Ask for amount of people attending the cookout and the number of hotdogs each person gets.
#The program should display: The number of packages of hotdogs required, the number of bun packages required, dogs leftover, buns leftover.

#Hotdog header
print('Hello, and welcome to my cookout calculator!')

#variables
dogpack = 10
bunpack = 8

#user input
people = int(input('How many people will be attending the cookout?: '))
dogseach = int(input('How many hot dogs will each person get?: '))

mindogs = people * dogseach / dogpack
minbuns = people * dogseach / bunpack

mindogs_rounded = int(-(-mindogs // 1))
minbuns_rounded = int(-(-minbuns // 1))

totaldogs = people * dogseach

dogsleft = mindogs_rounded * 10 - totaldogs
bunsleft = minbuns_rounded * 8 - totaldogs

print(f'You will need to get {mindogs_rounded} packs of hotdogs, {minbuns_rounded} packs of buns.')
print(f'You will have {dogsleft} hotdogs and {bunsleft} buns left over.')
    

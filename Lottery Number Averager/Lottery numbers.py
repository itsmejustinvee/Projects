from collections import defaultdict

#starting a dictionary to store how many times a number pops up
pops = defaultdict(int)

#open the file in read mode
with open('pbnumbers.txt', 'r') as file:
    for line in file:
        numbers = line.strip().split() #splits up the lines into single numbers
        for number in numbers:
            pops[int(number)] += 1 #adds a count for each number
            
#sorting the numbers , sorted will ask python to sort the numbers by frequency, lambda will return the frequency value from
#the dictionary, reverse = true tells it to sort in descending order as opposed to the default ascending order
sorted_numbers = sorted(pops.items(), key=lambda item: item[1], reverse=True)

#displays the most common numbers
print("The 10 most common numbers are: ")
for number, freq in sorted_numbers[:10]:
    print(f"Number: {number}, Frequency:{freq}")
    
#displays least common numbers
print("The 10 least Common numbers are: ")
for number, freq in sorted_numbers[-10:]:
    print(f"Number: {number}, Frequency: {freq}")
    
    
    

    

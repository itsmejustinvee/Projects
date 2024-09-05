
#Function to open the file, process items into a list, remove extra spaces and \n as well as the print statements for search
#result
def count_team_wins(filename, team_name):
        with open(filename, 'r') as file:
            winners = file.readlines() # Reads winners into a list
            
            winners = [winner.strip() for winner in winners] #removes extra spaces and newline junk
            
            win_count = winners.count(team_name) #Counter for how many times they won
            
            # Print statements for result
            if win_count > 0:
                print(f"The {team_name} won the World Series {win_count} times")
            else:
                print(f"The {team_name} has not won the world series.")
       

def main():
    team_name = input("Which team would you like to search for?: ") #gives the name for the other function
    count_team_wins("WorldSeriesWinners.txt", team_name) #gives the list for the other function and then gets the name from previous input


main()
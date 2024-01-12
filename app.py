"""
Data Analysis Techdegree
Project 2 - A Basketball Stats Tool
--------------------------------
"""
# My Grading Expectation:
# I am aiming for an 'Exceeds Expectation' grade -
# If the game does not meet those standards, please reject for corrections

# To Do?:
# Catch all exceptions (menu options) -- What Errors should be raised?
# Way to see a player's individual stats (not required, but cool possible extra feature)

from constants import PLAYERS
from statistics import mean

panthers = []
bandits = []
warriors = []
total_experienced = 0

# func to clean the data
def clean_data(PLAYERS):
    fixed_data = []
    for player in PLAYERS:
        fixed = {}
        fixed['name'] = player['name']
        if " and " in player['guardians']:
            fixed['guardians'] = list(player['guardians'].split(" and ")) # Some players have multiple guardians. This code helps to recognize that in a player profile (dictionary).
        else:
            fixed['guardian'] = player['guardians']
        if player['experience'] == 'YES':
            fixed['experience'] = True
        else:
            fixed['experience'] = False
        fixed['height'] = int(player['height'].split(' ')[0])
        fixed_data.append(fixed)
    return tuple(fixed_data)
clean_team = clean_data(PLAYERS) # contains the result of clean_data func

# func to sort players to each team
def balance_teams(clean_team):
    experienced = []
    inexperienced = []
    all_teams = [panthers, bandits, warriors]

    for player in clean_team:
        if player['experience'] == True:
            experienced.append(player)
        else:
            inexperienced.append(player)
    while experienced:
        for team in all_teams:
            pop_player = experienced.pop(0)
            team.append(pop_player)
    while inexperienced:
        for team in all_teams:
            pop_player = inexperienced.pop(0)
            team.append(pop_player)   
    return all_teams

# the Main (first) menu options display
def main_menu():
    print("***** Basketball Team Stats Tool *****")
    print("""
    ----- MENU OPTIONS -----
        A) DISPLAY TEAM STATS
        B) QUIT
    """)

# the (sub) menu options with team choices
def sub_menu():
    print("""
    ----- CHOOSE A TEAM -----
        A) Panthers
        B) Bandits
        C) Warriors
    
        Enter any other button to exit
    """)

# game stats following completion of the game
def display_stats(team):

    #Creating lists to count player experience type
    experienced = []
    inexperienced = []
    for player in team:
        if player['experience'] == True:
            experienced.append(player)
        else:
            inexperienced.append(player)

    # List of player heights (to take the mean)
    player_heights = []
    for player in team:
        player_heights.append(player['height'])

    # List of player names
    player_names = []
    players_sorter = []
    for player in team:
        player_names.append(player['name'])

    # List of guardians
    guardian_list = []
    for player in team:
        if 'guardians' in player:
            guardian_list.append(', '.join(player['guardians']))
        else:
            guardian_list.append(player['guardian'])

    # Text for displaying stats to the user
    print(f"""----------------------------
    Total Players: {len(team)}
    Total experienced: {len(experienced)}
    Total inexperienced: {len(inexperienced)}
    Average height: {int(mean(player_heights))}
    \nPlayers on Team: 
        {', '.join(player_names)}
    \nTeam Guardians:
        {', '.join(guardian_list)}""")

# Function to run the team stats tool
def run_app():
    clean_data(PLAYERS)
    balance_teams(clean_team)
    while True:
        sub_menu()
        sub_choice = input("Choose an option: ")
        if sub_choice.lower() == 'a':
            print("\nTeam: Panthers Stats")
            display_stats(panthers)

        elif sub_choice.lower() == 'b':
            print("\nTeam: Bandits Stats")
            display_stats(bandits)

        elif sub_choice.lower() == 'c':
            print("\nTeam: Warriors Stats")
            display_stats(warriors)

        else:
            break
    #  NEED TO Write exceptions
    
#Script to run the full code
main_menu()
while True:
    main_choice = input("Enter an Option: ")
    if main_choice.lower() == 'b':
        break
    elif main_choice.lower() == 'a':
        run_app()
        break
"""
Data Analysis Techdegree
Project 2 - A Basketball Stats Tool
--------------------------------
"""
# Grading Expectation:
# I am aiming for an 'Exceeds Expectation' grade -
# If the game does not meet those standards, please reject for corrections

from constants import TEAMS, PLAYERS
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
            fixed['guardians'] = list(player['guardians'].split(" and "))
        else:
            fixed['guardian'] = player['guardians']
        if player['experience'] == 'YES':
            fixed['experience'] = True
        else:
            fixed['experience'] = False
        fixed['height'] = int(player['height'].split(' ')[0])
        fixed_data.append(fixed)
    return fixed_data

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

# the menu options display
def main_menu():
    print("***** Basketball Team Stats Tool *****")
    print("""
    ----- MENU OPTIONS -----
        A) DISPLAY TEAM STATS
        B) QUIT
    """)

# the menu options for team choice
def sub_menu():
    print("""
    ----- CHOOSE A TEAM -----
        A) Panthers
        B) Bandits
        C) Warriors
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
    #player heights loop thru
    player_heights = []
    for player in team:
        player_heights.append(player['height'])

    player_names = []
    for player in team:
        player_names.append(player['name'])
    # Text displaying to the user
    print("----------------------------\n",
        f"Total Players: {len(team)}\n",
        f"Total experienced: {len(experienced)}\n",
        f"Total inexperienced: {len(inexperienced)}\n"
        f"Average height: {mean(player_heights)}\n",
        "\nPlayers on Team:\n ",
        f"{player_names}")
    

def run_app():
    clean_data(PLAYERS)
    balance_teams(clean_team)
    while True:
        sub_menu()
        sub_choice = input("Choose an option:\n")
        if sub_choice.lower() == 'a':
            print("Team: Panthers Stats")
            display_stats(panthers)
        elif sub_choice.lower() == 'b':
            print("Team: Bandits Stats")
            display_stats(bandits)
        elif sub_choice.lower() == 'c':
            print("Team: Warriors Stats")
            display_stats(warriors)
    #  NEED TO FIND A WAY TO BREAK THIS LOOP
    
#run the full code
main_menu()
while True:
    main_choice = input("Enter an Option: ")
    if main_choice.lower() == 'b':
        break
    elif main_choice.lower() == 'a':
        run_app()
        break
     

# To Do: Catch all exceptions (menu options)
# Possible FUTURE todo: Choice to see player's individual stats (possible extra feature)
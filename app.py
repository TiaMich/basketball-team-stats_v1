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
        fixed['height (inches)'] = int(player['height'].split(' ')[0])
        fixed_data.append(fixed)
    return fixed_data

clean_team = clean_data(PLAYERS) # contains the result of clean_data func

# func to sort players to each team... ERROR
def balance_teams(clean_team):
    for player in clean_team: # iterate through cleaned data
        if len(panthers) < 6:
            true_count = panthers.count(True) #count how many times True appears in team
            if player['experience'] == True and true_count < 3:
                panthers.append(player)
            else:
                panthers.append(player)

        if len(bandits) < 6:
            true_count = bandits.count(True)
            if player not in panthers and player['experience'] == True and true_count < 3:
                bandits.append(player)
            else:
                bandits.append(player)

        if len(warriors) < 6:        
            joint_team = bandits + panthers # using to concatenate teams to make code cleaner
            if player not in joint_team:
                warriors.append(player)

    return panthers, bandits, warriors

# the menu options display
def main_menu():
    print("***** Basketball Team Stats Tool *****")
    print("""
    ----- MENU OPTIONS -----
        A) DISPLAY TEAM STATS
        B) QUIT
    """)
    main_choice = input("Enter an Option: ")

# the menu options for team choice
def sub_menu():
    print("""
    ----- CHOOSE A TEAM -----
        A) Panthers
        B) Bandits
        C) Warriors
    """)
    sub_choice = input("Enter an Option: ")

    # game stats following completion of the game
    def display_stats():
        if sub_choice.lower() == 'A':
            for player in panthers:
                print(f"""\nTeam: The Panthers
                    ----------------------------
                    Total Players: {len(panthers)}
                    Total experienced: {3}.
                    Total inexperienced: {3}.
                    Average height: {mean(panthers['height'])}.\n""")
    clean_data(PLAYERS)

# Run code
clean_data(PLAYERS)
panthers, bandits, warriors = balance_teams(clean_team)
print(panthers, "\n")
print(bandits, "\n")
print(warriors)




# To Do:
# Catch all exceptions (menu options)
# Choice to see player's individual stats (possible extra feature)
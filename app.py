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
import copy

# Copy of the teams so that we can manipulate without changing the original information
# Not really sure if I need to use this data or how..
# decided to add, because in a real-life scenario, the teams could change and this would still work
team_choice = copy.deepcopy(TEAMS)

# func to clean the data
def clean_data(PLAYERS):
    cleaned_player = []
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
        cleaned_player.append(fixed)
    return cleaned_player

# func to balance the teams
def bal_teams():
    set(clean_data(PLAYERS))
    # Panthers
    team_choice[0] = set()
    # Bandits
    team_choice[1] = set()
    # Warriors
    team_choice[2] = set()
    # need to somehow, randomly, split up all the players between the teams
    # and each team has to have 6 unique players on it,
    # and the players are also unique to each team.
    # there needs to be a conditional that the teams have to have  equal num of exp vs. inexp

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
    print(f"""
    ----- CHOOSE A TEAM -----
        A) {team_choice[0]}
        B) {team_choice[1]}
        C) {team_choice[2]}
    """)
    sub_choice = input("Enter an Option:")

# game stats following completion of the game
#def team_stats():
    #print(f"""
    #Team: The {}
    #----------------------------
    #Total Players: {}
    #Total experienced: {}.
    #Total inexperienced: {}.
    #Average height: {mean()}.
   #""")
print(len(clean_data(PLAYERS))) #18

# To Do:
# Catch all exceptions
# Clean Data & store properly:
#   * Convert height to integer
#   * Make Experienced string Boolean
#   * Convert guardians string so that it becomes a list of strings
"""
Data Analysis Techdegree
Project 2 - A Basketball Stats Tool
--------------------------------
"""
# Grading Expectation:
# I am aiming for an 'Exceeds Expectation' grade -
# If the game does not meet those standards, please reject for corrections

from constants import TEAMS, PLAYERS

def clean_data(PLAYERS):
    cleaned = []
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
        cleaned.append(fixed)
    return cleaned

def bal_teams(): # team balancing function
    print('none')

# To Do:
# Catch all exceptions
# Clean Data & store properly:
#   * Convert height to integer
#   * Make Experienced string Boolean
#   * Convert guardians string so that it becomes a list of strings
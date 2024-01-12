# Basketball Team Stats Tool
This is the basketball stats tool, which takes data of players, sorts them onto teams, and displays this information to the user in an easy to navagate, readable format.

More specifically, this project takes data from a module file and imports it into my application script file. The module file contains a Dunder Main statement to keep the imported module information from executing inside of the script, unless otherwise commanded to. The aim is to clean the data of all the players in the basketball league (FYI: all players and player information is listed in the constant, "PLAYERS," of the module, which is seperately copied onto the app.py file for altering) to meet the client's requirements, which are as following:
- Player data imported from constants.py (module)
- The experienced string should become boolean (True if 'Yes' or False if 'No')
- The guardians string should become a List of strings. Remove the 'and' between the names and store each guardian in a List together for that player.

This application also has requirements of how to display the data to the user:
- Team's name displayed as a string
- Total players on that team is as an integer
- The player names as strings separated by commas
- number of inexperienced players on that team
- number of experienced players on that team
- the average height of the team
- the guardians of all the players on that team (as a comma-separated string)

My project is aiming to exceed expectation, so it also should meets these requirements:
- The players organized by height (tallest to shortest)
   * The following data points were saved to the team’s data structure *

**NOTE**: Python has no concept of actual constants like some other languages out there. But it is a convention in Python to treat ALL CAPS variables as if they are in-fact constants.
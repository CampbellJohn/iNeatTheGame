# This file is a collection of custom classes written for the game.
# It is imported into ineatvideogame.py
# In ineatvideogame.py, The Main / Host object instantiates an object of class
# 'GameSession'. 

# 80 Characters Maximum Width - 80 Characters Maximum Width - 80 Characters ###

class Area:
    # The __init__ launches automatically when the object is instantiated.
    # http://www.ibiblio.org/g2swap/byteofpython/read/class-init.html
    def __init__(self):
        pass

class DataValidator:
    def __init__(self):
        pass

class GameSession:

    # Define the variables for a game session, and assign initial values
    LoggingLevel = 0
    GameStatus = 'not started'
    PausedState = True
	
    # The __init__ launches automatically when the object is instantiated.
    def __init__(self):
        # Begin setting up the Game Session
        self.GameStatus = 'initializing'
	
        # Get the logging level and pass it as an argument when calling Logger
        # Instantiate a Logger object to report game logs to.
        Log = Logger(self.LoggingLevel)


class Logger:
    # The __init__ launches automatically when the object is instantiated.
    def __init__(self, args):
        pass

class Menu:
    # The __init__ launches automatically when the object is instantiated.
    def __init__(self):
        # 
        # Initial Menu:
        # 
        # New Game
        # Load Game
        # Options
        # Exit
        # 
        # If 'New Game' is selected...
        # Close the menu dialogue
        # Display loading screen if necessary
        # Instantiate the current World, Area, and Room
		# Instantiate Items, Characters, Quests, etc., other???
        # 
        # Hide loading screen, if any
        # Change the game status to Active
        # Log the event
        # Now listening for user input...
        pass

class Player:
    # The __init__ launches automatically when the object is instantiated.
    def __init__(self, WINHEIGHT, WINWIDTH):
        self.size = 132
        self.x = WINHEIGHT/2
        self.y = WINWIDTH/2

class Room:
    # The __init__ launches automatically when the object is instantiated.
    def __init__(self):
        pass

class World:
    # The __init__ launches automatically when the object is instantiated.
    def __init__(self):
        pass


# Import classes from invg.py (among other things)
import invg, pygame, sys
from pygame.locals import *

# Initialize pygame
pygame.init()

# 80 Characters Maximum Width - 80 Characters Maximum Width - 80 Characters ###

#
# A Host is an object that has a class of "Main".
# I suppose the class could also be named Host, 
# but it hurts my programmer heart not to have a Main().
# 
# In any case...
# Host is, for all intents and purposes, the 'main' object from which all other
# objects are instantiated.
#
# In Alpha we're keeping things simple, and running just one instance
# of the game, on this machine. 
# 
# This machine is the Host, but is also the Client. 
# The Host automatically starts a game.
# 
# In the future, a dedicated Host can allow multiple Clients
# to connect and each start their own game sessions.
# The games would be started and stopped by the Clients.
# The Host could, in emergencies, dump game sessions, or even
# migrate games to other Hosts (load balancing).
#

class Main:
    def __init__(self):
    # The __init__ launches automatically when the object is 
    # instantiated. Documentation:
    # http://www.ibiblio.org/g2swap/byteofpython/read/class-init.html
    

        FPS = 30 # frames per second setting
        FPSCLOCK = pygame.time.Clock()
    
        # Font Info
        BASICFONT = pygame.font.Font('freesansbold.ttf', 32)


        # set up the window
        DISPLAYSURF = pygame.display.set_mode((960, 704), 0, 32)
        pygame.display.set_caption('i neat video game')

        helloSurf = BASICFONT.render('Hello Kip. Nice pants.', True, \
        (255,255,255))
        helloRect = helloSurf.get_rect()
        helloRect.center = (480, 350)



        DISPLAYSURF.blit(helloSurf, helloRect) 


        # Alpha - Automatically launch a game session
        Game = invg.GameSession()

        while True: 
        # The Main Host Loop
            for event in pygame.event.get():
                if event.type == QUIT:
                    # Terminate this Host. End the program (and all running Game Sessions!).
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            FPSCLOCK.tick(FPS)

# Instantiate a Host:

Host = Main()



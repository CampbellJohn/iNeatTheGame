# Import classes from invg.py (among other things)
import invg, pygame, sys
from pygame.locals import *

# Comment Conventions:
# Normal comments are intended as permanent.
# DEL-KIP: Message for Kip. Gen. message or temp info. Delete when you get it.
# ATTENTION-JOHN: Either a to-do or a warning label.


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


# Let's create some global variables here.
WINWIDTH = 960
WINHEIGHT = 704
HALFWIDTH = WINWIDTH/2
HALFHEIGHT = WINHEIGHT/2
MOVERATE = 9

# Designate our font.
# DEL-KIP: Haven't looked into alternate fonts yet. I'm sure Pygame's got a few 
BASICFONT = pygame.font.Font('freesansbold.ttf', 32)

# Color Palette
# DEL-KIP: Gonna add a few more here eventually. Pretty certain these are
# ...RGB values.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Main:
    def __init__(self):
        FPS = 30 # frames per second setting
        FPSCLOCK = pygame.time.Clock()

        # Create player object.
        player = invg.Player(WINHEIGHT, WINWIDTH)
        player.img = pygame.image.load('Braid_132x132.png')

        # set up the window
        DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT), 0, 32)
        pygame.display.set_caption('i neat video game')

        helloSurf = BASICFONT.render('Hello Kip. Nice pants.', True, WHITE)
        helloRect = helloSurf.get_rect()
        helloRect.center = (450, 350)




        # Alpha - Automatically launch a game session
        # Game = invg.GameSession()

        while True: 
        # The Main Host Loop
            for event in pygame.event.get():
                if event.type == QUIT:
                    # Terminate this Host. End the program
                    # (and all running Game Sessions!)
                    pygame.quit()
                    sys.exit()
                
            # Move the Character
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[K_LEFT] or keys_pressed[K_a]:
                player.x -= MOVERATE 
            if keys_pressed[K_RIGHT] or keys_pressed[K_d]:
                player.x += MOVERATE 
            if keys_pressed[K_UP] or keys_pressed[K_w]:
                player.y -= MOVERATE 
            if keys_pressed[K_DOWN] or keys_pressed[K_s]:
                player.y += MOVERATE 
                  
            # Shit gets weird without this.
            DISPLAYSURF.fill(BLACK)
 
            # Draw the welcome message
            DISPLAYSURF.blit(helloSurf, helloRect) 

            # Draw the player here.
            player.rect = pygame.Rect(player.x, player.y, player.size, \
                                                            player.size)
            DISPLAYSURF.blit(player.img, player.rect)

            pygame.display.update()
            FPSCLOCK.tick(FPS)

# Instantiate a Host:
# DEL-KIP: I moved this piece of code down. I think it was at the top before? It
# ...kept trying to instantiate Main() before the definition of Main()
Host = Main()



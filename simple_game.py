# Capstone Project 2
# Henno Fourie, 13/04/2020
# Creating a simple game for an 'one' player object & three 'enemy' objects & a 'prize' opject.

import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.
screen_width = 1040
screen_height = 680
# This creates the screen and gives it the width and height specified.
screen = pygame.display.set_mode((screen_width,screen_height))


# This creates the player/enemy/prize and gives it the image found in this folder.
# Also rescaling images to provide enough moving space in the game.

player1 = pygame.image.load("player.jpg")
player = pygame.transform.scale(player1, (200,153))
enemy1 = pygame.image.load("monster.jpg")
enemyA = pygame.transform.scale(enemy1, (200,175))
enemyB = pygame.transform.scale(enemy1, (150,132))
enemyC = pygame.transform.scale(enemy1, (180,158))
prize = pygame.image.load("prize.jpg")

# Get the width and height of the images in order to do boundary detection.
image_height = player.get_height()
image_width = player.get_width()
enemyA_height = enemyA.get_height()
enemyA_width = enemyA.get_width()
enemyB_height = enemyB.get_height()
enemyB_width = enemyB.get_width()
enemyC_height = enemyC.get_height()
enemyC_width = enemyC.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))


# Store the positions of the player/enemy and prize as variables so that you can change them later. 
playerXPosition = 100
playerYPosition = 50

# Make the enemy & prize start off screen and at a random x/y position.

enemyAXPosition =  screen_width
enemyAYPosition =  random.randint(0, screen_height - enemyA_height)
enemyBXPosition =  screen_width
enemyBYPosition =  random.randint(0, screen_height - enemyB_height)
enemyCXPosition =  screen_width
enemyCYPosition =  random.randint(0, screen_height - enemyC_height)

prizeXPosition = random.randint(0, screen_width - prize_width)
prizeYPosition = screen_height


# This checks if the up, down, left or right key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False. 
keyUp= False
keyDown = False
keyLeft = False
keyRight = False


# This is the game while loop statement.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

while 1:  

    screen.fill(0) # Clears the screen.
    # This draws the player image to the screen at the position specfied.
    screen.blit(player, (playerXPosition, playerYPosition))
    # The enemy & prize image will start off screen as per the position specified.
    screen.blit(enemyA, (enemyAXPosition, enemyAYPosition))
    screen.blit(enemyB, (enemyBXPosition, enemyBYPosition))
    screen.blit(enemyC, (enemyCXPosition, enemyCYPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
        # This event checks if the user press a key down.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN: # pygame.K_DOWN represents a keyboard key constant.
                keyDown = True
            if event.key == pygame.K_LEFT: # pygame.K_LEFT represents a keyboard key constant.
                keyLeft = True
            if event.key == pygame.K_RIGHT: # pygame.K_RIGHT represents a keyboard key constant.
                keyRight = True
                
                
        # This event checks if the key is up(i.e. not pressed by the user).
        if event.type == pygame.KEYUP:      
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
        
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp == True:
        if playerYPosition > 0 :
            # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:
            # This makes sure that the user does not move the player below the window.
            playerYPosition += 1

    # And if you want the player to left right you will have to increase the x position. 
    if keyLeft == True:
        if playerXPosition > 0 :
            # This makes sure that the user does not move the player out of the window to the left.
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_width - image_width:
            # This makes sure that the user does not move the player out of the window to the right.
            playerXPosition += 1

    
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We then need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player.    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box & position for the enemy:
    
    enemyABox = pygame.Rect(enemyA.get_rect())
    enemyABox.top = enemyAYPosition 
    enemyABox.left = enemyAXPosition

    enemyBBox = pygame.Rect(enemyB.get_rect())
    enemyBBox.top = enemyBYPosition 
    enemyBBox.left = enemyBXPosition
    
    enemyCBox = pygame.Rect(enemyC.get_rect())
    enemyCBox.top = enemyCYPosition 
    enemyCBox.left = enemyCXPosition

    # Bounding box & position for the prize.
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    
    # Test collision of the boxes:
    # If the player collision with an enemy, the user loses the game.
    
    if playerBox.colliderect(enemyABox):    
        # Display losing status to the user: 
        print("You lose!")       
        # Quite game and exit window:         
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemyBBox):    
        # Display losing status to the user:         
        print("You lose!")       
        # Quite game and exit window:         
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemyCBox):    
        # Display losing status to the user:         
        print("You lose!")       
        # Quite game and exit window:         
        pygame.quit()
        exit(0)

    # If the player collision with the prize, the user wins the game.

    if playerBox.colliderect(prizeBox):    
        # Display winning status to the user:        
        print("You win!")       
        # Quite game and exit window:         
        pygame.quit()
        exit(0)
        
    # If the enemy is off the screen the user wins the game.
    
    if (enemyAXPosition < 0 - enemyA_width and enemyBXPosition < 0 - enemyB_width
        and enemyCXPosition < 0 - enemyC_width):    
        # Display wining status to the user:
        print("You win!")        
        # Quite game and exit window: 
        pygame.quit()        
        exit(0)
    
     
    # Approach of the enemy & prize to the player.
    enemyAXPosition -= 0.15
    enemyBXPosition -= 0.30
    enemyCXPosition -= 0.25
    prizeYPosition -= 0.30
    
    # ================The game loop logic ends here. =============

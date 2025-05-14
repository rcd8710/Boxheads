import pygame

# Initialize Pygame
pygame.init()

# Create a window with width 800px and height 600px
screen = pygame.display.set_mode((800, 600))

# Set the window title
pygame.display.set_caption("Boxheads")

titlescreen = True
# Main Game loop
maingame = True
while titlescreen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            titlescreen = False
    #backgground of title screen
    screen.fill((255, 255, 255))
    titleFont = pygame.font.Font(None, 72)
    titleText = titleFont.render("Boxheads", True, (0, 0, 0))
    textPos = titleText.get_rect(center=(400,200))
    #draws it 
    screen.blit(titleText,textPos)
    pygame.display.update()
pygame.quit()

while maingame:
    # Check for events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            maingame = False
    
    # Update the display
    pygame.display.update()

# Quit Pygame when the loop ends
pygame.quit()

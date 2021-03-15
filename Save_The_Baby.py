# Import random module
# Import pygame library and initialise it
import random
import pygame
pygame.init()

# Create variables for basic colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Store values for screen width and length in variables "screen_width" and "screen_length" respectively
screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))

# Set an icon and caption for the screen
icon = pygame.image.load("superhero.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Save The Baby!")

# Load the hero image
hero = pygame.image.load("superhero.png")

# Load all alien images
alien = pygame.image.load("alien1.png")
alien2 = pygame.image.load("alien2.png")
alien3 = pygame.image.load("alien3.png")
alien4 = pygame.image.load("alien4.png")
alien5 = pygame.image.load("alien5.png")
alien6 = pygame.image.load("alien6.png")

# Load baby image
baby = pygame.image.load("baby.png")

# Get the height and width for the hero, aliens, and baby
hero_height = hero.get_height()
hero_width = hero.get_width()
alien_height = alien.get_height()
alien_width = alien.get_width()
baby_width = baby.get_width()
baby_height = baby.get_height()

print("\n===== Save The Baby! =====\n")

# Give the hero a starting position - close to the centre of the screen
heroXposition = 450
heroYposition = 300

# Give each alien a starting position - off the screen
alienXposition = screen_width
alienYposition = random.randint(0, screen_height - alien_height)
alien2Xposition = -400
alien2Yposition = random.randint(0, screen_height - alien_height)
alien3Xposition = screen_width + 700
alien3Yposition = random.randint(0, screen_height - alien_height)
alien4Xposition = random.randint(0, screen_width - alien_width)
alien4Yposition = screen_height + 100
alien5Xposition = random.randint(0, screen_width - alien_width)
alien5Yposition = -400
alien6Xposition = random.randint(0, screen_width - alien_width)
alien6Yposition = screen_height + 800

# Give the baby a starting position - off the screen
babyXposition = screen_width + 400
babyYposiion = random.randint(0, screen_height - baby_height)

# Give the hero, alien and baby a speed - amount of pixels by which they move
hero_speed = 10
alien_speed = 8
baby_speed = 6

# Create while loop(the game loop)
gaming = True
while gaming:
    # Use time.delay to set how fast the screen should refresh
    pygame.time.delay(30)
    # Reset the screen after each loop
    screen.fill(black)
    # Blit the hero image on to the screen
    screen.blit(hero, (heroXposition, heroYposition))
    # Blit all alien images on to the screen
    screen.blit(alien, (alienXposition, alienYposition))
    screen.blit(alien2, (alien2Xposition, alien2Yposition))
    screen.blit(alien3, (alien3Xposition, alien3Yposition))
    screen.blit(alien4, (alien4Xposition, alien4Yposition))
    screen.blit(alien5, (alien5Xposition, alien5Yposition))
    screen.blit(alien6, (alien6Xposition, alien6Yposition))
    # Blit the baby image on to the screen
    screen.blit(baby, (babyXposition, babyYposiion))
    # Update the screen after every change that has happened
    pygame.display.update()
    # Create for loop for all events that will happen
    for event in pygame.event.get():
        # If the user clicks on the "X" the screen closes
        if event.type == pygame.QUIT:
            gaming = False
    # Use if statements to control what happens when each arrow is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and heroXposition > 0:
        heroXposition -= hero_speed
    if keys[pygame.K_RIGHT] and heroXposition < (screen_width - hero_width):
        heroXposition += hero_speed
    if keys[pygame.K_UP] and heroYposition > 0:
        heroYposition -= hero_speed
    if keys[pygame.K_DOWN] and heroYposition < (screen_height - hero_height):
        heroYposition += hero_speed
    # Control the direction and speed in which each alien moves across the screen
    alienXposition -= alien_speed
    alien2Xposition += alien_speed
    alien3Xposition -= alien_speed
    alien4Yposition -= alien_speed
    alien5Yposition += alien_speed
    alien6Yposition -= alien_speed
    # Control the direction and speed in which the baby moves across the screen
    babyXposition -= baby_speed
    # Create a "box" around the hero image
    hero_box = pygame.Rect(hero.get_rect())
    hero_box.top = heroYposition
    hero_box.left = heroXposition
    # Create a "box" around each alien image
    # If the hero "box" and "alien" box collide - close screen and print "Killed by aliens."
    alien_box = pygame.Rect(alien.get_rect())
    alien_box.top = alienYposition
    alien_box.left = alienXposition

    if hero_box.colliderect(alien_box):
        print("\n\n>>> Killed by aliens.\n\n")
        pygame.quit()

    alien2_box = pygame.Rect(alien2.get_rect())
    alien2_box.top = alien2Yposition
    alien2_box.left = alien2Xposition

    if hero_box.colliderect(alien2_box):
        print("\n\n>>> Killed by aliens.\n\n")
        pygame.quit()

    alien3_box = pygame.Rect(alien3.get_rect())
    alien3_box.top = alien3Yposition
    alien3_box.left = alien3Xposition

    if hero_box.colliderect(alien3_box):
        print("\n\n>>> Killed by aliens.\n\n")
        pygame.quit()

    alien4_box = pygame.Rect(alien4.get_rect())
    alien4_box.top = alien4Yposition
    alien4_box.left = alien4Xposition

    if hero_box.colliderect(alien4_box):
        print("\n\n>>> Killed by aliens.\n\n")
        pygame.quit()

    alien5_box = pygame.Rect(alien5.get_rect())
    alien5_box.top = alien5Yposition
    alien5_box.left = alien5Xposition

    if hero_box.colliderect(alien5_box):
        print("\n\n>>> Killed by aliens.\n\n")
        pygame.quit()

    alien6_box = pygame.Rect(alien6.get_rect())
    alien6_box.top = alien6Yposition
    alien6_box.left = alien6Xposition

    if hero_box.colliderect(alien6_box):
        print("\n\n>>> Killed by aliens.\n\n")
        pygame.quit()
    # If the hero "box" collides with the baby "box" - close the screen and print "You saved the baby!"
    baby_box = pygame.Rect(baby.get_rect())
    baby_box.top = babyYposiion
    baby_box.left = babyXposition

    if hero_box.colliderect(baby_box):
        print("\n\n>>> You saved the baby!\n\n")
        pygame.quit()
    # If the baby moves off the screen - close screen and print ("The aliens caught the baby")
    if babyXposition < 0 - baby_width:
        print("\n\nThe aliens caught the baby.\n\n")
        pygame.quit()

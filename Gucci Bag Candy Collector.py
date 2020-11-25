import pygame
import random

black = (0,0,0)
white = (255,255,255)

screen_width = 1300
screen_height = 600

class Picture(pygame.sprite.Sprite):
    
    def __init__(self, filename):
        
        super().__init__()
        
        self.image = pygame.image.load(filename).convert()
        
        self.image.set_colorkey(black)

        self.rect = self.image.get_rect()

pygame.init()

screen = pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("Collect your Candy!!!")

background_image = pygame.image.load("wallpaper.jpg").convert()
background_pos = [0,0]

candy_list =pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()


for i in range(50):

    candy = Picture("candy.png")

    candy.rect.x = random.randrange(screen_width)
    candy.rect.y = random.randrange(screen_width)


    candy_list.add(candy)

    all_sprite.add(candy)

bag = Picture("bag.png")



all_sprite_list.add(bag)


running = True
clock = pygame.image.Clock()
score = 0





while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image,background_pos)


    pos = pygame.mouse.get_pos()


    bag.rect.x = pos[0]
    bag.rect.y = pos[1]


    candy_collected_list = pygame.sprite.spritecollide(bag, candy_list, True)
    
    

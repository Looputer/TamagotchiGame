import pygame

WIDTH, HEIGHT = 800, 600

FPS = 60

icon_image = pygame.image.load('images/icon.png')
background_image = pygame.image.load('images/background.png')
button_image = pygame.image.load('images/button.png')

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_icon(icon_image)
    pygame.display.set_caption("拓麻歌子电脑版")
    screen.fill((255, 255, 255))
    screen.blit(background_image, (80, 0))
    screen.blit(button_image, (100, 425))
    screen.blit(button_image, (300, 425))
    screen.blit(button_image, (500, 425))
    done = False
    clock = pygame.time.Clock()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
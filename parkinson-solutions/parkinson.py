import pygame

pygame.init()
WIDTH, HEIGHT = 780, 560
screen = pygame.display.set_mode((WIDTH, HEIGHT))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load('background_start.png')
fps = 1
pygame.display.set_caption("Parkinson Solutions")
start_button = pygame.image.load('start.png')

def draw_intro():
    screen_w, screen_h = screen.get_size()
    background_w, background_h = background.get_size()

    for x in range(0, screen_w, background_w):
        for y in range(0, screen_h, background_h):
                screen.blit(background, (x, y))
       
        pygame.display.flip()      

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_intro()
     
        WIN.blit(start_button, (225, 300))
        
        pygame.display.update()

        if start_button.collidepoint(pos):
                print('clicked on image')  

    pygame.quit()

if __name__ == "__main__":
    main()

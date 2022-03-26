import pygame

pygame.init()

window = pygame.display.set_mode((600,600))
window.fill((0,0,0))
running = True

class Frog:
    def __init__(self):
        self.rect = pygame.rect.Rect(0,0,50,50)

    def update(self):
        self.rect.midtop = pygame.mouse.get_pos()
        pygame.draw.rect(window, (0,0,0), self.rect)

frog = Frog()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((255,255,255))
    frog.update()

    pygame.display.flip()
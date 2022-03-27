import pygame
from random import randint

pygame.init()

window = pygame.display.set_mode((600,600))
window.fill((0,0,0))
running = True

class Frog:
    def __init__(self):
        self.mouse_rect = pygame.rect.Rect(0,0,50,50)
        self.x, self.y = 300, 500
        self.frog_rect = pygame.rect.Rect(self.x, self.y, 50, 50)
        self.move = 5

    def update_mouse(self):
        self.mouse_rect.midtop = pygame.mouse.get_pos()
        pygame.draw.rect(window, (0,255,0), self.mouse_rect)
        pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))

    def move_frog(self, key=None):
        if key == pygame.K_LEFT:
            self.x -= self.move
        if key == pygame.K_RIGHT:
            self.x += self.move
        if key == pygame.K_UP:
            self.y -= self.move
        if key == pygame.K_DOWN:
            self.y += self.move
        if key == None:
            pass
        self.frog_rect.midtop = self.x, self.y

    def draw_frog(self):
        self.frog_rect.midtop = self.x, self.y
        pygame.draw.rect(window, (255,0,0), self.frog_rect)

    def draw_line(self, show=False):
        if show == True:
            pygame.draw.line(window, (0,0,255), self.frog_rect.center, self.mouse_rect.center, width=2)
        else:
            pass

    def positions(self):
        return self.frog_rect[0], self.mouse_rect[0]

class Butterfly:
    def __init__(self):
        self.pos_rect = pygame.rect.Rect(randint(200, 400), randint(200,400), 30, 30)

    def draw_butterfly(self):
        pygame.draw.rect(window, (165, 77, 219), self.pos_rect)

    def detect_collision(self, x1, y1, x2, y2):
        test = self.pos_rect.clipline(x1, y1, x2, y2)
        # pygame.draw.line(window, (0,0,0), (x1, y1), (x2, y2))
        if test != ():
            pygame.draw.rect(window, (20, 17, 38), self.pos_rect)

def butterfly_generator(num=10):
    butterfly_array = []
    for i in range(num):
        butterfly_array.append(Butterfly())
    return butterfly_array

frog = Frog()
# butterfly = Butterfly()
butterflies = butterfly_generator()

while running:
    # Making the keys repeat when pressed
    window.fill((255,255,255))
    pygame.key.set_repeat(1, 10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            frog.move_frog(key=event.key)
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("halo")
            frog.draw_line(show=True)
    for butterfly in butterflies:
        butterfly.draw_butterfly()
        butterfly.detect_collision(frog.frog_rect.center[0], frog.frog_rect.center[1], frog.mouse_rect.center[0], frog.mouse_rect.center[1])
    frog.draw_frog()
    frog.update_mouse()

    pygame.display.flip()
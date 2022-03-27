import pygame
from random import randint

pygame.init()

window = pygame.display.set_mode((600,600))
window.fill((0,0,0))
running = True


class Background:
    def __init__(self):
        self.bg_img = pygame.image.load('images/background.png')
        self.rect_bg_img = self.bg_img.get_rect()

        self.bg_x1 = 0
        self.bg_y1 = 0

        self.bg_x2 = 0
        self.bg_y2 = self.rect_bg_img.height

        self.move_speed = 0.1

    def update(self):
        self.bg_y1 += self.move_speed
        self.bg_y2 += self.move_speed
        if self.bg_y1 >= self.rect_bg_img.height:
            self.bg_y1 = -self.rect_bg_img.height
        if self.bg_y2 >= self.rect_bg_img.height:
            self.bg_y2 = -self.rect_bg_img.height

    def render(self):
        window.blit(self.bg_img, (self.bg_x1, self.bg_y1))
        window.blit(self.bg_img, (self.bg_x2, self.bg_y2))


class Frog:
    def __init__(self):
        self.frog_img = pygame.image.load("images/frog.png")
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
        if key is None:
            pass
        self.frog_rect.midtop = self.x, self.y

    def draw_frog(self):
        self.frog_rect.topleft = self.x, self.y
        window.blit(self.frog_img, (self.x, self.y))
        # pygame.draw.rect(window, (255,0,0), self.frog_rect)

    def draw_line(self, show):
        if show == True:
            pygame.draw.line(window, (0,0,255), self.frog_rect.midtop, self.mouse_rect.midbottom, width=2)
        else:
            pass

    def positions(self):
        return self.frog_rect[0], self.mouse_rect[0]


class Butterfly:
    def __init__(self):
        self.img = pygame.image.load('images/butterfly.png')
        # self.pos_rect = pygame.rect.Rect(randint(100, 500), randint(200,400), 30, 30)
        self.x = randint(50, 500)
        self.y = randint(-20, 100)
        self.pos_rect = pygame.rect.Rect(self.x, self.y, 30,30)

    def fall(self):
        self.y += 0.1

    def draw_butterfly(self):
        self.pos_rect.topleft = (self.x, self.y)
        window.blit(self.img, (self.x, self.y))

    def detect_collision(self, x1, y1, x2, y2):
        test = self.pos_rect.clipline(x1, y1, x2, y2)
        # print(self.pos_rect)
        pygame.draw.line(window, (0,0,0), (x1, y1), (x2, y2))
        if test != ():
            pygame.draw.rect(window, (20, 17, 38), self.pos_rect)

    def is_off_screen(self):
        if self.y > 630:
            return True
        else:
            return False


def butterfly_generator(num=10):
    butterfly_array = []
    for i in range(num):
        butterfly_array.append(Butterfly())
    return butterfly_array


background = Background()
frog = Frog()
# butterfly = Butterfly()
butterflies = butterfly_generator(num=10)

draw = False
while running:
    # Making the keys repeat when pressed
    background.update()
    background.render()
    pygame.key.set_repeat(1, 10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            frog.move_frog(key=event.key)
        elif event.type == pygame.MOUSEBUTTONUP:
            draw = False
        left_button = pygame.mouse.get_pressed()[0]
        if  left_button == True:
            draw = True

    for butterfly in butterflies:
        butterfly.fall()
        butterfly.draw_butterfly()
        if draw:
            butterfly.detect_collision(
                frog.frog_rect.midtop[0],
                frog.frog_rect.midtop[1],
                frog.mouse_rect.midbottom[0],
                frog.mouse_rect.midbottom[1]
            )
        if butterfly.is_off_screen():
            butterflies.remove(butterfly)
            butterflies.append(Butterfly())

    frog.draw_frog()
    frog.update_mouse()
    frog.draw_line(draw)

    pygame.display.flip()
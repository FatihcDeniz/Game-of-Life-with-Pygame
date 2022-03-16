import random
import pygame
from pygame.locals import *
import numpy as np
import pygame

width = 750
height = 750
x = 0
y = 0
size = 5
distance = 5



def draw(surface, x, y, array):
    #Drawing Lines and rectangles
    for row in array:
        for col in row:
            if col == 1:
                box = pygame.Rect(x, y, size, size)
                pygame.draw.rect(surface, (255, 255, 255), box)
                pygame.draw.line(surface, (105, 103, 101), (x, y), (x + 5, y), 1)
                pygame.draw.line(surface, (105, 103, 101), (x, y), (x, y + 5), 1)

                x = x + size + distance
            if col == 0:
                box = pygame.Rect(x, y, size, size)
                pygame.draw.rect(surface, (0, 0, 0), box)
                pygame.draw.line(surface, (105, 103, 101), (x, y), (x + 5, y), 1)
                pygame.draw.line(surface, (105, 103, 101), (x, y), (x, y + 5), 1)
                x = x + size + distance

        y = y + size + distance
        x = 0

    pygame.draw.line(surface, (105, 103, 101), (width / 2 - 3, 0), (width / 2 - 3, height), 3)
    pygame.draw.line(surface, (105, 103, 101), (0, height / 2 - 3), (width, height / 2 - 3), 3)


def get_array(array):
    #Applying Rules of game of life to the array.
    new_array = array.copy()
    for i in range(len(new_array)):
        for j in range(len(new_array)):
            total = array.take(range(i - 1, i + 2), mode='wrap', axis=0).take(range(j - 1, j + 2), mode='wrap',
                                                                              axis=1).sum() - array[i, j]
            if new_array[i, j] == 1:
                if (total < 2) or (total > 3):
                    new_array[i, j] = 0
            else:
                if total == 3:
                    new_array[i, j] = 1
    array = new_array

    return array

#Reset Function
def reset():
    array = np.zeros([width // (size + distance), width // (size + distance)])
    return array

#Generate a random array
def random_array(array):
    array[random.randint(0, len(array)//2):random.randint(len(array)//2, len(array)),
    random.randint(0, len(array)//2):random.randint(len(array)//2, len(array))] = 1
    return array

def fill(array):
    array[:,:] = 1
    return array

def run():
    surface = pygame.display.set_mode((width, height))
    running = True
    array = np.zeros([width // (size + distance), width // (size + distance)])
    array[3:10, 5:22] = 1
    pause = True
    speed = 100

    while running:
        draw(surface, 0, 0, array)
        pygame.display.flip()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_SPACE:
                    pause = False
                if event.key == K_r:
                    array = reset()
                if event.key == K_t:
                    array = random_array(array)
                    draw(surface, 0, 0, array)
                if event.key == K_f:
                    array = fill(array)
                    draw(surface, 0, 0, array)
                
                pygame.display.flip()
            if event.type == MOUSEBUTTONDOWN:
                x_loc = mouse_x // (size + distance)
                y_loc = mouse_y // (size + distance)
                if event.button == 1 or event.button == 2:
                    array[y_loc, x_loc] = 1
                if event.button == 3:
                    array[y_loc, x_loc] = 0

        while not pause:
            surface.fill((0, 0, 0))
            array = get_array(array)
            draw(surface, 0, 0, array)
            pygame.display.flip()
            pygame.time.wait(speed)
            for event in pygame.event.get():
                if event.type == QUIT:
                    quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_SPACE:
                        pause = True
                    if event.key == K_DOWN:
                        speed += 25
                    if event.key == K_UP and speed > 0:
                        speed -= 25


if __name__ == '__main__':
    run()

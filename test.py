import pygame

pygame.init()
p = 2
y = True
s = True
click = 0
x = 640
y = 480
height = 100
width = 100
display = pygame.display.set_mode((x, y))


def main():
    pygame.draw.rect(display, (255, 255, 255), (x // 2 - (width // 2), y - height, height, width))


def click():
    pygame.draw.rect(display, (0, 255, 255), (x // 2 - (width // 2), y - height, height, width))


while s:
    for event in pygame.event.get():
        main()
        clock = pygame.time.Clock()
        x_mouse = pygame.mouse.get_pos()[0]
        y_mouse = pygame.mouse.get_pos()[1]
        x_square1 = x // 2 - (width // 2)
        x_square2 = x // 2 - (width // 2) + width
        y_square1 = y - height
        y_square2 = (y - height) + height

        if x_mouse >= x_square1 and x_mouse <= x_square2 and y_mouse >= y_square1 and y_mouse <= y_square2:
            stop = pygame.mouse.get_pressed()[0]
            click()
            t = True
            print('окраска произошла ')
            while stop:  # == 1:
                #                stop = pygame.mouse.get_pressed()[0]                    # ---
                print('ЛКМ нажата')
                while t:  # == True:
                    print("цикл вычисления координат")
                    t = False
                    x_square_dim = x_mouse - x_square1
                    y_square_dim = y_mouse - y_square1
                    pygame.display.update()
                print("цикл отображения")

                pygame.draw.rect(display, (0, 255, 255),
                                 (x_mouse - x_square_dim, y_mouse - y_square_dim, height, width))
                pygame.display.update()

                # +++  vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
                event_list = pygame.event.get()
                for event in event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        print(f'MOUSEBUTTONUP отжата !!!')
                stop = pygame.mouse.get_pressed()[0]
        # +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        else:
            main()

        if event.type == pygame.QUIT:
            s = False
    pygame.display.update()
    clock.tick(30)

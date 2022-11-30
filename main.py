# Подключение библиотеки PyGame
import pygame
import random
# Инициализация PyGame (запуск модуля)
pygame.init()
# Окно игры: размер, позиция
gameScreen = pygame.display.set_mode((400, 400))
# Модуль os - позиция окна
import os
x: int = 100
y: int = 100
os.environ['Sp_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
# Параметры окна
size = [800,540]
screen = pygame.display.set_mode(size) #размер окна
pygame.display.set_caption("Рисование") # название заголовка
gameScreen.fill((0, 0, 200)) # заливка экрана цветом
FPS=30
clock = pygame.time.Clock()
pygame.display.flip() # двойная буферизация (после отрисовки переворачивает экран игроку)

# Игровой цикл игры
runGame = True  # флаг выхода из цикла игры
while runGame: #цикл (пока) контролируемый переменной runGame
    clock.tick(FPS)
    # Отслеживание события: "закрыть окно"
    for event in pygame.event.get():   # event - переменная цикла
        if event.type == pygame.QUIT:
            runGame = False
    pygame.display.flip()


# Выход из игры:
pygame.quit()

import pygame
import sys
import time 

pygame.init()
WHITE_COLOR = (255,255,255)
BLUE_COLOR = (0, 0, 255)
WIDTH_SCREEN = 1200
HEIGHT_SCREEN = 800
THICKNESS = 30
BORDER_RADIUS = 10
SPEED = 10
BALL_COLOR = (0, 0, 0)
RED_COLOR = (255, 0, 0)
GREY_COLOR = (105, 105, 105)
BALL_RADIUS = 10
Vx = -5
Vy = 2
FPS = 60
flLeft=flRight=False
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
screen.fill(WHITE_COLOR)

r1 = pygame.Rect(WIDTH_SCREEN // 2 - 300/2, HEIGHT_SCREEN - THICKNESS, 300, THICKNESS)
c1 = pygame.Rect(WIDTH_SCREEN // 2, HEIGHT_SCREEN // 2, 10, 10)
right_wall = pygame.Rect(WIDTH_SCREEN - 5, 0, WIDTH_SCREEN + 1, HEIGHT_SCREEN)
left_wall = pygame.Rect(-1, 0, 5, HEIGHT_SCREEN)
roof1 = pygame.Rect(0,0, WIDTH_SCREEN // 2 - 30, 10)
roof2 = pygame.Rect(WIDTH_SCREEN // 2 + 30,0, WIDTH_SCREEN, 10)



rect_width_velocity = 1   
rect_width_bool = False
def change_rect_width(rect, velocity):
    global rect_width_bool
    
    if rect_width_bool:
        rect.left -= rect_width_velocity
        rect.width += 2 * rect_width_velocity
        if rect.width >= WIDTH_SCREEN // 4:
            rect_width_bool = not rect_width_bool
    else:
        rect.left += rect_width_velocity
        rect.width -= 2 * rect_width_velocity
        if rect.width <= WIDTH_SCREEN // 8:
            rect_width_bool = not rect_width_bool
    



def change_ball_coordinate(rect, Vx, Vy):
    rect.x += Vx
    rect.y += Vy
    

def change_ball_speed():
    global Vx, Vy
    Vx = Vx / abs(Vx) * (abs(Vx) + 1)
    Vy = Vy / abs(Vy) * (abs(Vy) + 1)
    


previous_time = time.time()
start_time = time.time()

f = pygame.font.Font('Times New Roman.ttf', 24)
f_win_lose = pygame.font.Font('Times New Roman.ttf', 72)

    
def show_time():
    sc_text = f.render(f'Время в игре: {(time.time() - start_time):.0f}', 1, BLUE_COLOR, WHITE_COLOR)
    pos = sc_text.get_rect(center=(WIDTH_SCREEN - sc_text.get_width(), HEIGHT_SCREEN // 2))
    screen.blit(sc_text, pos)
    
def check_win(rect):
    if rect.y <= 0:
        sc_text_win = f_win_lose.render(f'Вы победили', 1, BLUE_COLOR, WHITE_COLOR)
        pos = sc_text_win.get_rect(center=(WIDTH_SCREEN//2, HEIGHT_SCREEN // 2))
        screen.blit(sc_text_win, pos)
        
    

def check_lose(rect):
    if rect.y >= HEIGHT_SCREEN:
        sc_text_win = f_win_lose.render(f'Вы проиграли', 1, BLUE_COLOR, WHITE_COLOR)
        pos = sc_text_win.get_rect(center=(WIDTH_SCREEN//2, HEIGHT_SCREEN // 2))
        screen.blit(sc_text_win, pos)
        

while True:
    BALL_COLOR = (0, 0, 0)
    
    screen.fill(WHITE_COLOR)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                flRight = True
            if event.key == pygame.K_LEFT:
                flLeft = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                flLeft=flRight = False

    if flRight:
        if r1.x <= WIDTH_SCREEN - r1.width:
            r1.x += SPEED
    elif flLeft:
        if r1.x >= 0:
            r1.x -= SPEED
            
    if c1.collidelist([r1, roof1, roof2]) >=0:
        BALL_COLOR = (0, 255, 0)
        Vy= -Vy
    elif c1.collidelist([left_wall, right_wall])>=0:
        BALL_COLOR = (0, 255, 0)
        Vx= -Vx
    
    change_rect_width(r1, rect_width_velocity)
    change_ball_coordinate(c1, Vx, Vy)      
    if time.time() - previous_time > 10:
        change_ball_speed()
        previous_time = time.time()
    
    check_lose(c1)
    check_win(c1)
    
    pygame.draw.rect(screen, RED_COLOR, r1, 0, border_radius=BORDER_RADIUS)
    pygame.draw.circle(screen, BALL_COLOR, c1.center, 10)
    pygame.draw.rect(screen, GREY_COLOR, right_wall, 0)
    pygame.draw.rect(screen, GREY_COLOR, left_wall, 0)
    pygame.draw.rect(screen, BLUE_COLOR, roof1, 0)
    pygame.draw.rect(screen, BLUE_COLOR, roof2, 0)
    
    show_time()
    pygame.display.update()
    clock.tick(FPS)
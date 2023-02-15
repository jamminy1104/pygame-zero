import pgzrun
from random import randint

WIDTH = 400                     # 높이랑 길이를 정하는 거
HEIGHT = 400

dots = []
lines = []

next_dot = 0
timer = 0           # 시간 기록을 위해 선언

for dot in range(0, 10):                                            
    actor = Actor("dot")
    actor.pos = randint(20,WIDTH - 20),randint(20, HEIGHT - 20)
    dots.append(actor)

def draw():
    screen.fill("black")               # 스크린을 검은색으로 채우는 거
    number = 1

    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))

        dot.draw()
        number = number + 1             #저거랑 number += 1 이랑 같은 뜻이다.

    for line in lines:
        screen.draw.line(line[0], line[1], (255, 153, 255))             # 라인 색깔 적는 코드
        
    screen.draw.text(str(round(timer,2)), topleft=(10,10), color=(102,153,102), fontsize=50)    # 타이머 폰트크기,색깔같은거적는코드


def on_mouse_down(pos): 
    global next_dot
    global lines

    if (next_dot < 10 and timer <= 15):                         # 만약 다음 점이 10 초과거나 타이머가 15초 이상 이 아니때만 실행됨
        if dots[next_dot].collidepoint(pos):
            if next_dot:
                lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
            next_dot = next_dot + 1             # next dot의 값을 1씩 추가하는 코드
        else:
            lines = []   
            next_dot = 0        


def update():           # update는 pygame에 기본적으로 있는거로,게임 중간중간에 업데이트가 있을때,실행된다.
    global timer
    global next_dot
    
    if (timer >= 15):                   # 만약에 시간이 15초 이상이면 머머추는 코드
        return
    else:                               # 만약 시간이 15초 이상이아니면 시간을 계속 보내는 코드
        if(next_dot != 10):
            timer += 1/60


pgzrun.go()
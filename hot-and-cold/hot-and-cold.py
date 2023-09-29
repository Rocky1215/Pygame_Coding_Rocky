from random import randint
WIDTH = 600
HEIGHT = 350
score = 0
time_left = 45

tiger = Actor("tiger")
tiger.pos = 300,175
tiger_coordinates = tiger.x, tiger.y

chicken = Actor("chicken")
chicken.pos = 300, 175
chicken_coordinates = chicken.x, chicken.y
chicken.opacity = 0.0

def oob_check():
    if tiger.right >= WIDTH:
        tiger.right = WIDTH
    elif tiger.left <= 0:
        tiger.left = 0
    elif tiger.bottom >= HEIGHT:
        tiger.bottom = HEIGHT
    elif tiger.top <= 0:
        tiger.top = 0

def draw():
    screen.blit('forest', (0, 0))
    tiger.draw()
    chicken.draw()
    chicken.opacity = 0.0
    screen.draw.text(str(time_left), color=("red"), topleft=(10, 10))
    

def update():
    if keyboard.a:
        tiger.x = tiger.x - 2
    elif keyboard.d:
        tiger.x = tiger.x + 2
    elif keyboard.w:
        tiger.y = tiger.y - 2
    elif keyboard.s:
        tiger.y = tiger.y + 2
    elif keyboard.t:
        tiger.x = tiger.x -1
        tiger.y = tiger.y -1
        check_proximity()
        
    elif keyboard.left:
        tiger.x = tiger.x - 2
    elif keyboard.right:
        tiger.x = tiger.x + 2
    elif keyboard.up:
        tiger.y = tiger.y - 2
    elif keyboard.down:
        tiger.y = tiger.y + 2

    oob_check()

def check_proximity():
    
    if Actor.distance_to(chicken, tiger) < 40:
        print("You won! Press w,a,s,d,t, or any of the arrow keys to quit.")
        chicken.opacity = 1.0
        keyboard.a
        quit()
        keyboard.d
        quit()
        keyboard.w
        quit()
        keyboard.s
        quit()
        keyboard.t
        pass
        keyboard.left
        quit()
        keyboard.right
        quit()
        keyboard.up
        quit()
        keyboard.down
        quit()
    else:
        print(Actor.distance_to(chicken, tiger))


def place_chicken():
    chicken.x = randint(20, (WIDTH - 20))
    chicken.y = randint(20, (HEIGHT - 20))

def update_time_left():
    global time_left

    if time_left:
        time_left = time_left - 1
    else:
        game_lost()

def game_lost():
    print("You lost")
    chicken.opacity = 1.0
    print("The chicken was here!")
    keyboard.a
    
    keyboard.d
    
    keyboard.w
    
    keyboard.s
    
    keyboard.t
    
    keyboard.left
    
    keyboard.right
    
    keyboard.up
    
    keyboard.down
    

place_chicken()        
clock.schedule_interval(update_time_left, 1.0)

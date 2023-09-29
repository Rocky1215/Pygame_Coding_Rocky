#make the program let the user miss once but not twice!
from random import randint
apple = Actor("apple")

def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10,600)

def on_mouse_down(pos):
    
    collision_apple_false = apple.x and apple.y != (pos)
    collision_apple_true = apple.x and apple.y == (pos)
    
    miss_count = 0

    if collision_apple_true:
        print("Good shot!")
        place_apple()
    elif collision_apple_false:
        print("One last chance!")
        miss_count = miss_count + 1
    else:
        quit()
        
        if miss_count <2:
            place_apple()
        else:
            quit()


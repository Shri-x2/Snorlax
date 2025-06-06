import pgzrun, random, time
WIDTH, HEIGHT = 800, 600
TITLE="Snorlax shoot"
print("Hello")
msg= "Shoot Snorlax!"
gamestage = "start"
score = 0 
print(msg)
snorlax= Actor("snorlax")
snorlax.pos = (random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))
def draw():
    print("Drawing Snorlax")
    screen.fill("teal")
    if gamestage == "start":
        screen.draw.text("Click to start the game", (WIDTH // 2 - 100, HEIGHT // 2), fontsize=30, color="white")
    elif gamestage == "play":
        snorlax.draw()
    screen.draw.text(msg, (10, 10), fontsize=30, color="white")
def on_mouse_down(pos):
    global msg, gamestage
    if gamestage == "start":
        gamestage = "play"
        msg = "Game Started! Click on Snorlax to catch it!"
        print("Game started")
        return
    
    print("Mouse clicked at", pos)
    if snorlax.collidepoint(pos):
        # print("Snorlax clicked!")
        msg= "You caught Snorlax!"
        print(msg)
        snorlax.pos = (random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))
    else:
        msg = "Missed Snorlax!"
        # print(msg)

def gameover():
    global msg, gamestage
    print("Game Over")
    msg = "Game Over! Final Score: " + str(score)
    gamestage = "over"
    snorlax.pos = (WIDTH // 2, HEIGHT // 2)
clock.schedule(gameover,10) 
pgzrun.go()
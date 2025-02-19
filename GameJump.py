import pgzrun
import random

WIDTH = 800
HEIGHT = 400
GRAVITY = 0.5

class Player(Actor):
    def __init__(self, x, y):
        super().__init__('hero_idle', (x, y))
        self.vy = 0
        self.on_ground = True

    def jump(self):
        if self.on_ground:
            self.vy = -10
            self.on_ground = False

    def update(self):
        self.y += self.vy
        self.vy += GRAVITY
        if self.y >= HEIGHT - 50:
            self.y = HEIGHT - 50
            self.on_ground = True

player = Player(100, HEIGHT - 50)
enemies = [Actor("enemy", (random.randint(200, 700), HEIGHT - 50)) for _ in range(3)]
game_active = False

def draw():
    screen.clear()
    screen.blit("background", (0, 0))  
    if game_active:
        player.draw()
        for enemy in enemies:
            enemy.draw()
    else:
        screen.draw.text("Jump Hero", center=(WIDTH // 2, 100), fontsize=50, color="white")
        screen.draw.text("Press SPACE to Start", center=(WIDTH // 2, 200), fontsize=30, color="white")

def update():
    global game_active
    if game_active:
        player.update()
        for enemy in enemies:
            enemy.x -= 2
            if enemy.x < 0:
                enemy.x = WIDTH

def on_key_down(key):
    global game_active
    if key == keys.SPACE:
        game_active = True
    if key == keys.UP:
        player.jump()

pgzrun.go()

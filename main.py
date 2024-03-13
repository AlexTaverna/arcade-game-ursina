from distutils.log import debug
from turtle import update
from ursina import *
from Player import *
from BG import *
from Enemy import *

app = Ursina()

camera.orthographic=True
camera.fov=40
window.fullscreen=True
window.exit_button.visible = False
window.fps_counter.enabled = True
window.vsync = True
window.color = color.rgb(0,94,184)

player = Player()
bg = BG()
  
for enemy in range(1):
    enemy=HeavyEnemy()
    enemy=BaseEnemy()
    enemy=SinEnemy()
    
                  
def update():

    for bullet in player.bullet_renderer.model.vertices:
        for enemy in enemies:
            if distance_2d(bullet, enemy) < enemy.hit_zone : 
                player.bullet_renderer.model.vertices.remove(bullet)             
                enemy.hp -= 1
                enemy.blink(color.red,duration=.08, delay=0,)
                if enemy.hp<=0:
                    kill_enemy(enemy)
                    spawn_enemy(enemy.__class__.__name__)
    
    for enemy in enemies:
        for bullet in enemy.bullet_renderer.model.vertices:
            if distance_2d(bullet, player) <player.hit_zone : 
                enemy.bullet_renderer.model.vertices.remove(bullet)
                player.hp-= enemy.damage             
                player.blink(color.red,duration=.05,)
                player.set_sprite()
                if player.hp<=0:
                    player.kill()
                    print_on_screen("GAME OVER")
                    application.paused = True
                    
                    
app.run()

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

enemies = [] 

player = Player()
bg = BG()

for enemy in range(10):
    enemy = Enemy()
    enemies.append(enemy)
    
    


def bullets():
   
    for i, bullet in enumerate(player.bullet_renderer.model.vertices):
        for enemy in enemies :
            if distance_2d(bullet, enemy) < 2:
                enemy.hp -= 1              
                if enemy.hp <= 0:
                        enemies.remove(enemy)
                        destroy(enemy)                                           
                player.bullet_renderer.model.vertices.remove(bullet)

    for enemy in enemies :
        for i, bullet in enumerate(enemy.bullet_renderer.model.vertices):
            if distance_2d(bullet, player) < 2:
                player.hp -= 5
                player.set_sprite()      
                enemy.bullet_renderer.model.vertices.remove(bullet)

        
    
def update():
    bullets()
    
    








app.run()

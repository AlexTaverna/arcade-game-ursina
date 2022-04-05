from ast import parse
from hashlib import new
from pickle import TRUE
from tkinter import Y, Scale
from turtle import Screen, position, screensize
from ursina import *
from random import randint
app=Ursina()


texures=["P38_lvl_1_d0.png","P38_lvl_1_d1.png","P38_lvl_1_d2.png","P38_lvl_1_d3.png","P38_lvl_1_d4.png"]
class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.model="quad"
        self.scale = (5,4.5)
        self.position = (0,0,-0.1)
        self.HP=100
        self.texture=texures[0]
        self.hidden=False
        self.mobility=7
        self.collider = 'box'
        self.shadow=Sprite(model="quad",texture="P38_shadow.png",scale=(0.5,0.5))   
player=Player()
def spriteChange():
        if player.HP >= 80:
            player.texture=texures[0]
        elif player.HP > 60 and player.HP < 81:
            player.texture=texures[1]
        elif player.HP > 40 and player.HP < 61:
            player.texture=texures[2]    
        elif player.HP > 20 and player.HP < 41:
            player.texture=texures[3]
        elif player.HP <= 20:
            player.texture=texures[4]
cloudTexture=["smoke1.png","smoke2.png","smoke3.png","smoke4.png"]
class Cloud(Sprite):
    def __init__(self):
        super().__init__()
        self.model="cube"
        self.scale = (randint(4,15),randint(4,15),5)
        self.position = (randint(-30,+30),randint(25,140),-1.7)
        self.rotation = (0,0,randint(0,360))
        self.texture=cloudTexture[randint(0,3)]
        self.collider = 'box'
        self.speed=4
clouds = []
for i in range(1):
    cloud=Cloud()
    clouds.append(cloud)
        
def clamp(n, minn, maxn):                                
    return max(min(maxn, n), minn)
sea=Entity(model="quad",texture="sea.png",scale=90,rotation=(0,0,0),position=(0,0,5))


camera.orthographic=True
camera.fov=40
window.vsync=True
window.fullscreen=False
window.exit_button.visible = False
window.fps_counter.enabled = True

def update():
    print_on_screen( "DAMEGE: "+str(player.HP), position=(-0.8,-0.4), origin=(0,0),duration=0.1)     

    playerSpeed = (mouse.position*camera.fov - player.position)*player.mobility
    player.rotation_y = clamp(playerSpeed.x*-1, -50 ,50)
    player.position += playerSpeed*time.dt
    player.shadow.x=player.x-2.5
    player.shadow.y=player.y-2.5
    spriteChange()
    
    sea.y-=1*time.dt
    if(sea.y< -21 ):
        sea.y=0
    
    for cloud in clouds:
        cloud.y-= cloud.speed*time.dt
       
        if(cloud.y<-30):
            cloud.__init__()

        if player.intersects(cloud).hit:
            player.hidden=True
            print_on_screen( "HIDDEN", position=(-0.8,-0.45), origin=(0,0),duration=0.1)
        else:
            player.hidden=False    
            
            
app.run()
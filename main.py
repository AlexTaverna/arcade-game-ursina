
from distutils.command.build import build

from ursina import *
from Bullet import *
from Cloud import Cloud
from Player import *

app = Ursina()
player = Player()
clouds = []



for i in range(4):
    cloud=Cloud()
    clouds.append(cloud)

sea=Entity(model="quad",texture="sea.png",scale=90,rotation=(0,0,0),position=(0,0,5))

camera.orthographic=True
camera.fov=40
window.fullscreen=True
window.exit_button.visible = False
window.fps_counter.enabled = True

def input (key):
    if key == "space":
        player.HP-=10
        


   


def update():
    
    player_update(player)
    print_on_screen( "HULL: "+str(player.HP), position=(-0.8,-0.4), origin=(0,0),duration=0.1)     

    sea.y-=2*time.dt
    if(sea.y< -21 ):
        sea.y=0
    
    for cloud in clouds:
        cloud.y-= cloud.speed*time.dt
       
        if(cloud.y<-30):
            cloud.__init__()



app.run()

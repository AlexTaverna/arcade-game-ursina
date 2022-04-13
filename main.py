
from distutils.command.build import build
from ursina import *
from Player import *
from Bullet import *
from Cloud import Cloud

app = Ursina()
# bullet = Bullet()                 the bullet class is WIP
player = Player()
clouds = []
for i in range(4):
    cloud=Cloud()
    clouds.append(cloud)

def clamp(n, minn, maxn):                                
    return max(min(maxn, n), minn)

sea=Entity(model="quad",texture="sea.png",scale=90,rotation=(0,0,0),position=(0,0,5))


camera.orthographic=True
camera.fov=40
window.fullscreen=True
window.exit_button.visible = False
window.fps_counter.enabled = True

def input (key):
    if key == "space":
        player.HP-=10
        setSprite(player)
        
def update():

    

    print_on_screen( "DAMAGE: "+str(player.HP), position=(-0.8,-0.4), origin=(0,0),duration=0.1)     

    playerSpeed = (mouse.position*camera.fov - player.position)*player.mobility
    player.rotation_y = clamp(playerSpeed.x*-2, -50 ,50)
    player.position += playerSpeed* time.dt
    player.shadow.x=player.x-2.5
    player.shadow.y=player.y-2.5
    
    sea.y-=2*time.dt
    if(sea.y< -21 ):
        sea.y=0
    
    for cloud in clouds:
        cloud.y-= cloud.speed*time.dt
       
        if(cloud.y<-30):
            cloud.__init__()

        if player.intersects(cloud).hit:
            player.hidden=True
            print_on_screen( "HIDDEN", position=(-0.8,-0.45), origin=(0,0),duration=0.1)  # this couse a preatty big fps drop!! 
        else:
            player.hidden=False   
            
            
app.run()

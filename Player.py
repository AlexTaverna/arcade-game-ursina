from ursina import Sprite
from ursina import mouse
from ursina import camera
from ursina import time
from ursina import*
from Bullet import*

texures=["P38_lvl_1_d0.png","P38_lvl_1_d1.png","P38_lvl_1_d2.png","P38_lvl_1_d3.png","P38_lvl_1_d4.png"]

player_bullets=[]

left_prop=Entity(model='cube', color=color.gray,scale=(1,.05,.05))
right_prop=Entity(model='cube', color=color.gray,scale=(1,.05,.05))


class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.model="quad"
        self.scale = (5,4.4)
        self.position = (0,0,-0.1)
        self.HP=100
        self.mobility=10
        self.collider = 'box'
        self.primary_cooldown=False
        self.secondary_cooldown=False
        setSprite(self)
        
        
def setSprite(me):
    if me.HP >= 80:
        me.texture=texures[0]
    elif 60< me.HP < 81:
        me.texture=texures[1]
    elif me.HP > 40 and me.HP < 61:
        me.texture=texures[2]    
    elif me.HP > 20 and me.HP < 41:
        me.texture=texures[3]
    elif me.HP <= 20:
        me.texture=texures[4]   

def clamp(n, minn, maxn):                                
    return max(min(maxn, n), minn)

def shoot_primary(me):
    if not me.primary_cooldown:
     me.primary_cooldown = True
     invoke(setattr,me, 'primary_cooldown', False, delay=.15)
     player_bullet = Bullet("bullet_2_orange.png",me.position+(0,3),(0,25))
     player_bullets.append(player_bullet)
     

def player_update(me):
    playerSpeed = (mouse.position*camera.fov - me.position)*me.mobility
    me.rotation_y = clamp(playerSpeed.x*-2, -50 ,50)
    me.position += playerSpeed* time.dt
    
    setSprite(me)
    
    left_prop.rotate((0,2,0), relative_to=None)
    left_prop.position=(me.position+(-0.75,1.5,-0.1))

    right_prop.rotate((0,-2,0), relative_to=None)
    right_prop.position=(me.position+(0.75,1.5,-0.1))  

    if held_keys['left mouse']:
        shoot_primary(me)
    for player_bullet in player_bullets:
        move_bullet(player_bullet)
    


     
    
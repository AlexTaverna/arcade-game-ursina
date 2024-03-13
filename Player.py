
from random import *

from ursina import mouse
from ursina import camera
from ursina import time
from ursina import *
from Enemy import *


texures=["P38_lvl_1_d0.png","P38_lvl_1_d1.png","P38_lvl_1_d2.png","P38_lvl_1_d3.png","P38_lvl_1_d4.png"] 

left_prop=Entity(model='cube', color=color.gray,scale=(.9,.07,.07))
right_prop=duplicate(left_prop)



class Player(Entity):
    def __init__(self):
        super().__init__()
        self.model="quad"
        self.scale = 4
        self.hp=100
        self.mobility=5
        self.primary_cooldown=False
        self.secondary_cooldown=False 
        self.set_sprite()
        self.position_z= 2
        self.always_on_top = 2
        self.hit_zone = self.scale/2
        self.bullet_renderer = Entity(model=Mesh(mode='point', thickness=.2), texture='circle', color=color.yellow)
       
    
    def kill(self):
        self.disable()
        destroy(left_prop)
        destroy(right_prop)            
        
    def set_sprite(self):
        if self.hp >= 80:
            self.texture=texures[0]
        elif 60< self.hp < 81:
            self.texture=texures[1]
        elif self.hp > 40 and self.hp < 61:
            self.texture=texures[2]    
        elif self.hp > 20 and self.hp < 41:
            self.texture=texures[3]
        elif self.hp <= 20:
            self.texture=texures[4]   

    def clamp(n, minn, maxn):                                
        return max(min(maxn, n), minn)

    def shoot_primary(self):
        if not self.primary_cooldown:
            self.primary_cooldown = True
            invoke(setattr,self, 'primary_cooldown', False, delay=.15)
            self.bullet_renderer.model.vertices.append(self.position + (0,2))

    

    def update(self):
        playerSpeed = (mouse.position*camera.fov - self.position)*self.mobility
        self.rotation_y = clamp(playerSpeed.x*-2, -50 ,50)
        self.position += playerSpeed* time.dt
        
        
        
        left_prop.rotate((0,40* time.dt,0), relative_to=None)
        left_prop.position=(self.position+(-0.6,1.3,-0.1))

        right_prop.rotate((0,-40* time.dt,0), relative_to=None)
        right_prop.position=(self.position+(0.6,1.3,-0.1))  

        if held_keys['left mouse']:
            self.shoot_primary()


        for i, bullet in enumerate(self.bullet_renderer.model.vertices):
            bullet += Vec3(0, time.dt * 20, 0)
            if bullet.y>25:
                self.bullet_renderer.model.vertices.remove(bullet)   
         
        self.bullet_renderer.model.generate() 
        
        
     
         
          
              
    


     
    
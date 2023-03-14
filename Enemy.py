from pyexpat import model
from random import randint
from ursina import Sprite
from ursina import time
from ursina import*





class Enemy(Entity):
    def __init__(self):
        super().__init__()
        self.model='quad'
        self.scale = 4
        self.hp=5  
        self.primary_cooldown=False
        self.secondary_cooldown=False
        self.direction = Vec3(0,-5,00)
        self.position=( randint(-25,25) , randint(25,100) , 0 )     
        self.points = 5
        self.texture = "Aircraft_02"
        self.rotation = (0,0,180)
        self.always_on_top = 1

        self.bullet_renderer = Entity(model=Mesh(mode='point', thickness=.3), texture='circle', color=color.green) 
        
    def clamp(n, minn, maxn):                                
        return max(min(maxn, n), minn)

    def shoot_primary(self):
        if not self.primary_cooldown:
            self.primary_cooldown = True
            invoke(setattr,self, 'primary_cooldown', False, delay=2)
            self.bullet_renderer.model.vertices.append(self.position + (0,-2))
       
    
    def update(self):
       
        self.position += self.direction*time.dt
        

        if self.position.y<35 and self.hp >= 0:   
            self.shoot_primary()

        self.bullet_renderer.model.generate()

        for i, bullet in enumerate(self.bullet_renderer.model.vertices):
            self.bullet_renderer.model.vertices[i] += Vec3(0, time.dt * -10, 0)
            

        
    


     
    
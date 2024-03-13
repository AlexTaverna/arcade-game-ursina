from pyexpat import model
from random import randint
from ursina import Sprite
from ursina import time
from ursina import*


enemies = [] 

def spawn_enemy(enemy):
    match enemy :
        case "BaseEnemy":
            enemy=BaseEnemy() 
        case "SinEnemy":
            enemy=SinEnemy()
        case "HeavyEnemy":
            enemy=HeavyEnemy()
      
    
    
def kill_enemy(enemy):
    destroy(enemy.bullet_renderer)
    enemies.remove(enemy)
    destroy(enemy)



#############################################################################

class BaseEnemy(Entity):
    def __init__(self):
        super().__init__()
        self.model='quad'
        self.scale = 3
        self.hp=2 
        self.primary_cooldown=False
        self.secondary_cooldown=False
        self.direction = Vec3(0,-5,00)
        self.position=( randint(-25,25) , randint(25,100) , 0 )     
        self.points = 4
        self.texture = "Aircraft_02"
        self.rotation = (0,0,180)
        self.always_on_top = 1
        self.damage = 2
        self.hit_zone = self.scale/2
        enemies.append(self)
        self.bullet_renderer = Entity(model=Mesh(mode='point', thickness=.2), texture='circle', color=color.green, direction = Vec3(0,-15, 0)) 
        

    def shoot_primary(self):
        if not self.primary_cooldown:
            self.primary_cooldown = True
            invoke(setattr,self, 'primary_cooldown', False, delay=2)
            self.bullet_renderer.model.vertices.append(self.position + (0,-2))
       
    
    def update(self):
       
        self.position += self.direction*time.dt

        if self.position.y<25 :   
            self.shoot_primary()
        
        

        self.bullet_renderer.model.generate()

        for i, bullet in enumerate(self.bullet_renderer.model.vertices):
            self.bullet_renderer.model.vertices[i] += self.bullet_renderer.direction * time.dt
            if self.bullet_renderer.model.vertices[i].y < -25:
                self.bullet_renderer.model.vertices.remove(bullet)   
                 
 ##################################################################################################       



class SinEnemy(BaseEnemy):
    def __init__(self):
        super().__init__()
        self.hp=3 
        self.direction = Vec3( 0 ,-5,00)
        self.position=( randint(-10,10) , randint(25,100) , 0 )     
        self.texture = "Aircraft_03"
        self.always_on_top = 1
        self.damage = 1
        self.amplitude =12
        self.frequency = 1.5
        self.direction_modifier=random.choice([-1, 1])
        self.bullet_renderer = Entity(model=Mesh(mode='point', thickness=.15), texture='circle', color=color.orange, direction = Vec3(0,-15, 0)) 
        
    
  
    def shoot_primary(self):
        if not self.primary_cooldown:
            self.primary_cooldown = True
            invoke(setattr,self, 'primary_cooldown', False, delay=.5)
            self.bullet_renderer.model.vertices.append(self.position + (0,-2))
       
    
    def update(self):
        
        self.direction.x = (sin(time.time()*self.frequency )*self.amplitude)*self.direction_modifier
        self.position += self.direction*time.dt

        if self.position.y<25 :   
            self.shoot_primary()

        self.bullet_renderer.model.generate()
       
        for i, bullet in enumerate(self.bullet_renderer.model.vertices):
            self.bullet_renderer.model.vertices[i] += self.bullet_renderer.direction * time.dt
            if self.bullet_renderer.model.vertices[i].y < -25:
                self.bullet_renderer.model.vertices.remove(bullet)   
              
            
##################################################################################################       



class HeavyEnemy(BaseEnemy):
    def __init__(self):
        super().__init__()
       
       
        self.hp=6
        self.direction = Vec3( 0 ,-3,00)
        self.position=( randint(-10,10) , randint(20,50) , 0 )     
        self.texture = "Aircraft_05"
        self.always_on_top = 1
        self.damage = 3
        self.scale=3.5
        
        self.bullet_renderer = Entity(model=Mesh(mode='point', thickness=.22), texture='circle', color=color.red, direction = Vec3(0,-8, 0)) 
        
    
    def shoot_primary(self):
        if not self.primary_cooldown:
            self.primary_cooldown = True
            invoke(setattr,self, 'primary_cooldown', False, delay=1.5)
            self.bullet_renderer.model.vertices.append(self.position + (.8,-2))
            self.bullet_renderer.model.vertices.append(self.position + (-.8,-2))
       
    
   
        
    


     
    
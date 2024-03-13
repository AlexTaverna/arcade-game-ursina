

from pyexpat import model

from ursina import *
from random import randint
reference_speed=5
clouds=[]


class Cloud(Sprite):
    def __init__(self):
        super().__init__()
        self.model="quad"
        self.scale = (randint(4,20),randint(4,20),5)
        self.position = (randint(-30,+30),randint(25,140),1)
        self.rotation = (0,0,randint(0,360))
        self.texture="smoke" + str(randint(1,4)) + ".png"
        self.speed = reference_speed + 4
        self.always_on_top = 1

def make_cloud():
            cloud = Cloud()
            clouds.append(cloud)
        

class BG (Entity):
   
    def __init__(self):
        super().__init__()

      

        
            
        for i in range(4):
           make_cloud()
     
        self.drop = Entity(
        model="quad",
        texture="watertile",
        scale=80,
        position_z=100                      
    ) 

                
    def update(self):
        for self.cloud in clouds:
            self.cloud.y -= self.cloud.speed*time.dt
            if self.cloud.y<-25:
                clouds.remove(self.cloud)
                destroy(self.cloud)
                make_cloud()
                
       
        
        self.drop.texture_offset += (0, time.dt*0.05)
        




 
        
        



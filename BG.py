

from pyexpat import model

from ursina import *
from random import randint
reference_speed=5
clouds=[]
isles=[]


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

"""class Isle(Sprite):
    def __init__(self):
        super().__init__()
        self.model="cube"
        self.scale = (randint(30,80),randint(30,80),1)
        self.position = (randint(-30,+30),randint(25,140),3)
        self.rotation = (0,0,randint(0,360))
        self.texture="islands\isle_" + str(randint(1,25))+".png"
        self.speed = reference_speed
        self.always_on_top = -1"""
        

class BG (Entity):
   
    def __init__(self):
        super().__init__()

        """for y in range(1):
            isle = Isle()
            isles.append(isle)"""

        
        for i in range(4):
            cloud = Cloud()
            clouds.append(cloud)
     
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
                self.cloud.__init__()
        
        """ for self.isile in isles:
            self.isile.y -= self.isile.speed*time.dt
            if self.isile.y<-30:
                self.isile.__init__()"""
        
        self.drop.texture_offset += (0, time.dt*0.05)
        




 
        
        



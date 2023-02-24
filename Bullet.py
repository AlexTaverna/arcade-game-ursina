from ursina import *

class Bullet(Sprite):
    def __init__(self,texure,position,direction):
        super().__init__()
        self.model="quad"
        self.scale = (0.5,1,5)
        self.position=position
        self.collider = 'cube'
        self.texture= texure
        self.direction=direction
        
        
def move_bullet(me):
    me.x+=me.direction[0]*time.dt
    me.y+=me.direction[1]*time.dt
        
        
        
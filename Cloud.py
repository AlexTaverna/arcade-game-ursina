from ursina import Sprite
from random import randint
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
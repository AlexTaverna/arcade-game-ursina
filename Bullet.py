from ursina import Sprite

class Bullet(Sprite, ):
    def __init__(self,texure):
        super().__init__()
        self.model="quad"
        self.scale = (0.5,1,5)
        self.position = (0,0)
        self.collider = 'cube'
        self.texture= texure
        self.speed=20
        
        
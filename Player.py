from ursina import Sprite
texures=["P38_lvl_1_d0.png","P38_lvl_1_d1.png","P38_lvl_1_d2.png","P38_lvl_1_d3.png","P38_lvl_1_d4.png"]
class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.model="quad"
        self.scale = (5,4.5)
        self.position = (0,0,-0.1)
        self.HP=100
        self.hidden=False
        self.mobility=7
        self.collider = 'box'
        self.shadow=Sprite(model="quad",texture="P38_shadow.png",scale=(0.5,0.5))
        setSprite(self)
        
def setSprite(instance):
    if instance.HP >= 80:
        instance.texture=texures[0]
    elif 60< instance.HP < 81:
        instance.texture=texures[1]
    elif instance.HP > 40 and instance.HP < 61:
        instance.texture=texures[2]    
    elif instance.HP > 20 and instance.HP < 41:
        instance.texture=texures[3]
    elif instance.HP <= 20:
        instance.texture=texures[4]   
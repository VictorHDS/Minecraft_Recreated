from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
grass_texture = load_texture('assets/images/grass_block.png')
stone_texture = load_texture('assets/images/stone_block.png')
brick_texture = load_texture('assets/images/brick_block.png')
dirt_texture = load_texture('assts/images/dirt_block.png')
class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = grass_texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.lime,
            scale = 0.5
        )
    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                voxel = Voxel(position = self.position + mouse.normal)
            if key == 'left mouse down':
                destroy(self)

for z in range(16):
    for x in range(16):
        voxel = Voxel(position = (x,0,z))
player = FirstPersonController()
app.run()
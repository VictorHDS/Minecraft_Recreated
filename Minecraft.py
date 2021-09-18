from ursina import *
class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube', 
            color = color.white, 
            texture = 'white_cube', 
            rotation = Vec3(45,45,45)
            )
class Test_button(Button):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'cube',
            texture = 'brick',
            color = color.blue,
            highlight_color = color.red,
            press_color = color.yellow
        )
def update():
    if held_keys['a']:
        test_square.x -= 4 * time.dt
app = Ursina()#Basic instance of the game
test_square = Entity(model = 'quad', color = color.red, scale = (1,4), position = (5,1))
mc_texture = load_texture('assets/images/minecraft-icon.png')
mc = Entity(model = 'quad', texture = mc_texture)
test_cube = Test_button()
app.run()#Run the instance
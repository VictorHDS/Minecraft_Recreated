from ursina import *
def update():
    if held_keys['a']:
        test_square.x -= 4 * time.dt
app = Ursina()#Basic instance of the game
test_square = Entity(model = 'quad', color = color.red, scale = (1,4), position = (5,1))
# sans_texture = land_texture('assets/Sans.png')
# sans = Entity(model = 'quad', texture = sans_texture)
app.run()#Run the instance

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()
def input(key):
    if key == 'q' or key == 'escape':
         quit()
boxes = []
Sky(texture='sky_sunset')




for b in range(20):
    for t in range(20):
        block = Entity(
            position=(t,0,b),
            model='cube',
            texture='GrassBlock.jpg',
            highlight_color=color.light_gray,
            collider='box',
            color=color.white,
            parent=scene
        )
        boxes.append(block)


player = FirstPersonController()

app.run()
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
from numpy import floor
app = Ursina()

boxes = []

def input(key):
    if key == 'q' or key == 'escape':
        quit()

Sky()

noise = PerlinNoise(seed=2022, octaves=4)
boxw = 60


freq = 30
amp = 5
        

for i in range(boxw*boxw):
    t = Entity(model='cube',color=color.white, texture='GrassBlock.jpg', collider='box')
    t.x = floor(i/boxw)
    t.z = floor(i%boxw)
    t.y = floor((noise([t.x/freq,t.z/freq]))*amp)


player = FirstPersonController()
player.cursor.color = color.white

app.run()
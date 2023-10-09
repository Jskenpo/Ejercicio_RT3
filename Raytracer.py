import pygame
from pygame.locals import *
from rt import Raytracer
from figures import *
from lights import *
from materials import *

width = 512
height = 1024/2

pygame.init()

screen = pygame.display.set_mode(
    (width, height), 
    pygame.DOUBLEBUF | 
    pygame.HWACCEL | 
    pygame.HWSURFACE
)
screen.set_alpha(None)


raytracer = Raytracer(screen)
raytracer.rtClearColor(0.25, 0.25, 0.25)


snow = Material(diffuse=[1, 1, 1], spec = 64)
button = Material(diffuse=[0.2, 0.2, 0.2], spec = 250)
nose = Material(diffuse=[1, 0.5, 0], spec = 64)
eyes = Material(diffuse=[0, 0, 0], spec = 64)
mouth = Material(diffuse=[0.5, 0.5, 0.5], spec = 64)

## Snowman

##BODY
raytracer.scene.append(
    Sphere(position=(0,-1.5,-10), radius=1, material=snow)
)
raytracer.scene.append(
    Sphere(position=(0,0,-10), radius=0.75, material=snow)
)
raytracer.scene.append(
    Sphere(position=(0,1.1,-10), radius=0.6, material=snow)
)

##BUTTONS
raytracer.scene.append(
    Sphere(position=(0,-1.5,-10), radius=0.2, material=button)
)

raytracer.scene.append(
    Sphere(position=(0,0.2,-10), radius=0.15, material=button)
)

raytracer.scene.append(
    Sphere(position=(0,-0.2,-10), radius=0.15, material=button)
)

##NOSE
raytracer.scene.append(
    Sphere(position=(0,1.1,-10), radius=0.1, material=nose)
)

##EYES
raytracer.scene.append(
    Sphere(position=(0.2,1.2,-10), radius=0.05, material=eyes)
)

raytracer.scene.append(
    Sphere(position=(-0.2,1.2,-10), radius=0.05, material=eyes)
)

##MOUTH
raytracer.scene.append(
    Sphere(position=(0.2,0.9,-10), radius=0.05, material=mouth)
)

raytracer.scene.append(
    Sphere(position=(-0.2,0.9,-10), radius=0.05, material=mouth)
)

raytracer.scene.append(
    Sphere(position=(0.0,0.8,-10), radius=0.05, material=mouth)
)

raytracer.scene.append(
    Sphere(position=(0.1,0.85,-10), radius=0.05, material=mouth)
)

raytracer.scene.append(
    Sphere(position=(-0.1,0.85,-10), radius=0.05, material=mouth)
)

raytracer.lights.append(
    AmbientLight(intensity=0.2)
) 
raytracer.lights.append(
    DirectionalLight(direction=(-1, -1, -1), intensity=0.5)
)

isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

    raytracer.rtClear()

    raytracer.rtRender()
    
    pygame.display.flip()

pygame.quit()
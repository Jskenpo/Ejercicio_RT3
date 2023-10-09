from math import tan,pi
import numpy as np

class Raytracer(object):
    def __init__(self, screen):
        self.screen = screen

        self.rtViewport(0, 0, screen.get_width(), screen.get_height())
        self.rtProyection()

        _,_, self.width, self.height = screen.get_rect()

        self.scene = []
        self.lights = []

        self.camPosition = [0,0,0]

        self.rtColor(1, 1, 1)
        self.rtClearColor(0, 0, 0)
        self.rtClear()

    def rtClearColor(self, r, g, b):
        # Recibe valores de 0 a 1
        self.clearColor = (r*255, g*255, b*255)

    def rtClear(self):
        # Pygame usa vlores de 0 a 255
        self.screen.fill(self.clearColor)
        
    def rtColor(self, r, g, b):
        self.currColor = (r*255, g*255, b*255)

    def rtPoint(self, x, y, color=None):
        y = self.height - y
        # Pygame usa valores de 0 a 255
        if (0<=x<self.width) and (0<=y<self.height):
            if color != None:
                color = (color[0] * 255,
                            color[1] * 255,
                            color[2] * 255)
                self.screen.set_at((x,y), color)
            else:
                self.screen.set_at((x,y), self.currColor)
    

    def rtViewport(self, posX, posY, width, height):
        self.vpX = posX
        self.vpY = posY
        self.vpWidth = width
        self.vpHeight = height

    def rtProyection ( self, fov = 60, n = 0.1):
        aspectRatio = self.vpWidth / self.vpHeight
        self.nearPlane = n
        self.topEdge = (tan(pi * fov / 360) / 2) * self.nearPlane
        self.rightEdge = self.topEdge * aspectRatio

    def rtCastRay(self, origin, direction):
        intercept = None
        hit = None

        for obj in self.scene:
            intercept = obj.ray_intersect(origin, direction)
            if intercept != None:
                hit = intercept
            
        return hit
            
        
    def rtRender(self):
        for x in range(self.vpX, self.vpWidth + 1):
            for y in range(self.vpY, self.vpHeight + 1):
                if 0<=x<self.width and 0<=y<self.height:
                    # Pasar de coordenadas de ventana a coordenadas de NDC (-1 a 1)
                    xp = 2*(x + 0.5)/self.vpWidth - 1
                    yp = 2*(y + 0.5)/self.vpHeight - 1

                    xp *= self.rightEdge
                    yp *= self.topEdge

                    # Crear un rayo
                    direction = (xp, yp, -self.nearPlane)
                    direction = direction / np.linalg.norm(direction) # Normalizar en libreria de matematicas

                    intercept = self.rtCastRay(self.camPosition, direction)
                    if intercept != None:
                        """
                        material = intercept.obj.material

                        colorP = list(material.diffuse)

                        ambienLight = [0,0,0]
                        directionalLight = [0,0,0]

                        for light in self.lights:
                            if light.lightType == "AmbientLight":
                                ambienLight[0] += light.color[0] * light.intensity
                                ambienLight[1] += light.color[1] * light.intensity
                                ambienLight[2] += light.color[2] * light.intensity
                            elif light.lightType == "DirectionalLight":
                                lightDir = np.array(light.direction) * -1
                                lightDir = lightDir / np.linalg.norm(lightDir)
                                intensity = np.dot(intercept.normal, lightDir)
                                intensity = max(0,min(1, intensity))

                                directionalLight[0] += intensity * light.color[0]
                                directionalLight[1] += intensity * light.color[1]
                                directionalLight[2] += intensity * light.color[2]
                            
                            colorP[0] *= ambienLight[0] + directionalLight[0]
                            colorP[1] *= ambienLight[1] + directionalLight[1]
                            colorP[2] *= ambienLight[2] + directionalLight[2]

                            colorP[0] = min(1, colorP[0])
                            colorP[1] = min(1, colorP[1])
                            colorP[2] = min(1, colorP[2])
                            """
                        
                        # phong reflection model
                        # lightColor = AmbientIntensity + DiffuseIntensity + SpecularIntensity
                        # FinalColor = SurfaceColor * lightColor
                        surfaceColor = intercept.obj.material.diffuse

                        ambientColor = [0,0,0]
                        diffuseColor = [0,0,0]
                        specularColor = [0,0,0]

                        for light in self.lights:
                            if light.lightType == "AmbientLight":
                                ambientColor = [ambientColor[i] + light.getLightColor()[i] for i in range(3)]
                                

                            else:
                                diffuseColor = [(diffuseColor[i] + light.getDiffuseColor(intercept)[i]) for i in range(3)]
                                specularColor = [(specularColor[i] + light.getSpecularColor(intercept, self.camPosition)[i]) for i in range(3)]


                        lightColor = [ambientColor[i] + diffuseColor[i] + specularColor[i] for i in range(3)]
                        finalColor = [min(1,surfaceColor[i] * lightColor[i]) for i in range(3)]
                        self.rtPoint(x, y, finalColor)
                



import random
import time

from pygame import Vector2

import core


class Projectile:
    def __init__(self):
        self.taille=2
        self.vitesse=Vector2()
        self.acceleration=Vector2()
        self.vitesseMax=15
        self.position = Vector2()
        self.dureeDeVie=3
        self.startTime=time.time()
        self.accelerationTemp = Vector2()

    def deplacementProj(self):

        self.vitesse += self.acceleration
        self.position += self.vitesse
        self.acceleration = Vector2(0, 0)

    def collisionProj(self):
        pass

    def drawProj(self):
        core.Draw.circle((255,255,255), self.position, self.taille)

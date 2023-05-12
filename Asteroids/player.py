import random
import time

from pygame import Vector2

import core



class Player:
    def __init__(self):
        self.taille = 10
        self.vitesse = Vector2()
        self.acceleration = Vector2()
        self.accelerationTemp = Vector2()
        self.position = Vector2(400,400)
        self.vie = 3
        self.startTime = time.time()
        self.vitesseMax = 10
        self.accelerationMax = 10
        self.orientation = Vector2(0,-1)
        self.vel = Vector2(0, 0)
        self.frottement = Vector2()

    def deplacementPlayer(self):

        self.acceleration=Vector2(0,0)

        # self.acceleration = 0, 5 * Vector2(self.vitesse) - Vector2(self.vitesse)
        self.frottement[0] = (-0.04 * self.vitesse[0])
        self.frottement[1] = (-0.04 * self.vitesse[1])

        if core.getKeyPressList("z"):

            self.accelerationTemp = Vector2(self.orientation)
            self.accelerationTemp.scale_to_length(self.acceleration.length() + 0.3)
            self.acceleration = Vector2(self.accelerationTemp)

        if core.getKeyPressList("d"):
            self.orientation = self.orientation.rotate(10)

        if core.getKeyPressList("q"):
            self.orientation = self.orientation.rotate(-10)

        #DEFINITION DE L'ACCELERATION

        self.acceleration += Vector2(self.frottement)

        # DEFINITION DE LA VITESSE
        if self.vitesse.length() <= self.vitesseMax:
            self.vitesse += self.acceleration

        # DEFINITION DE LA POSITION
        self.position += self.vitesse
        if self.position.x <= 0:
            self.position.x = 800
        if self.position.x > 800:
            self.position.x = 0
        if self.position.y <= 0:
            self.position.y = 800
        if self.position.y > 800:
            self.position.y = 0

    def drawPlayer(self):
        a = 0 - self.orientation.angle_to(Vector2(0, 1))

        p1 = self.position + Vector2(-5, -5).rotate(a)
        p2 = self.position + Vector2(0, 10).rotate(a)
        p3 = self.position + Vector2(5, -5).rotate(a)

        core.Draw.polygon((255,255,255), ((p1), (p2), (p3)))
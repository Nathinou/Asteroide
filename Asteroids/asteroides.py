import random
import time

from pygame import Vector2

import core


class Asteroides:
    def __init__(self):
        self.taille = 40
        self.vitesse = Vector2()
        self.acceleration = Vector2()
        self.position = Vector2()
        self.lvl = 1
        self.vitesseMax = 10

    def collision(self, projectile):
        d=self.position.distance_to(projectile.position)
        if d < self.taille+projectile.taille:
            return True
        return False

    def collisionPlayer(self, player):
        e=self.position.distance_to(player.position)
        if e < self.taille+player.taille:
            return True
        return False


    def deplacementAsteroides(self):

        self.vitesse += self.acceleration
        self.position += self.vitesse
        self.acceleration = (0, 0)

    def drawAsteroides(self):
        core.Draw.circle((100, 100, 100), self.position, self.taille)











        '''
        #CREATION DE 2 ASTEROIDES
        for b in range(1): 
            ast = Asteroides()
            ast.position = Vector2(self.position)
            ast.taille = self.taille-15
            
            rdm1 = random.randint(1, 2)
            if rdm1 == 1:
                rdmX = random.uniform(-5, -3)
            else:
                rdmX = random.uniform(5, 3)
    
            rdm1 = random.randint(1, 2)
            if rdm1 == 1:
                rdmY = random.uniform(-5, -3)
            else:
                rdmY = random.uniform(5, 3)
    
            ast.acceleration = Vector2(rdmX, rdmY)
    
            core.memory('mesAsteroides').append(ast)

        core.memory('mesAsteroides').remove
        '''
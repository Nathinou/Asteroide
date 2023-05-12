import random
import time

from pygame import Vector2

import core
from Asteroids import player
from Asteroids.asteroides import Asteroides
from Asteroids.etat import Etat
from Asteroids.player import Player
from Asteroids.projectiles import Projectile


class Map:

    def __init__(self):
        self.maxPlayer = 1
        self.maxAsteroides = 10
        self.maxEnnemis = 1
        self.maxProjectile = 5
        self.taille = Vector2(800,800)



    def creationProjectile(self):

            proj = Projectile()
            proj.position = Vector2(core.memory("mesPlayers").position)
            proj.acceleration = Vector2(core.memory("mesPlayers").orientation)
            proj.acceleration.scale_to_length(core.memory("mesPlayers").orientation.length() + 5)
            proj.vitesse = Vector2(core.memory("mesPlayers").vitesse)
            proj.taille = 2
            core.memory('mesProjectiles').append(proj)

    def creationPlayer(self):
            play = Player()
            play.position = Vector2(400,400)
            play.vitesse = Vector2(0, 0)
            play.acceleration = Vector2(0, 0)
            play.taille = 10
            core.memory("mesPlayers",play)

    def creationAsteroide(self, position=None, taille=40):
        ast = Asteroides()

        if position is None:
            zoneSpawn = random.randint(1,4)
            if zoneSpawn == 1:
                ast.position = Vector2(random.randint(-40,840),-40)
            if zoneSpawn == 2:
                ast.position = Vector2(-40,random.randint(-40,840))
            if zoneSpawn == 3:
                ast.position = Vector2(random.randint(-40, 840), 840)
            if zoneSpawn == 4:
                ast.position = Vector2(840,random.randint(-40,840))
        else:
            ast.position = Vector2(position)
            ast.taille = taille

        rdm1 = random.randint(1,2)
        if rdm1 == 1:
            rdmX = random.uniform(-3,-1.5)
        else:
            rdmX = rdmX = random.uniform(3,1.5)

        rdm1 = random.randint(1, 2)
        if rdm1 == 1:
            rdmY = random.uniform(-3, -1.5)
        else:
            rdmY = rdmY = random.uniform(3, 1.5)

        ast.acceleration = Vector2(rdmX, rdmY)

        core.memory('mesAsteroides').append(ast)

    def update(self):

    #PLAYERS

        core.memory("mesPlayers").deplacementPlayer()
        core.memory("mesPlayers").drawPlayer()

    # PROJECTILES

        if core.getKeyPressList("SPACE"):
            if len(core.memory('mesProjectiles')) == 0:
                self.creationProjectile()

            if len(core.memory('mesProjectiles')) > 0:
                if len(core.memory('mesProjectiles')) < 5:
                    if time.time() - core.memory('mesProjectiles')[-1].startTime > 0.2:
                        self.creationProjectile()

        for p in core.memory('mesProjectiles'):
            if time.time() - p.startTime > p.dureeDeVie:
                core.memory('mesProjectiles').remove(p)

        for p in core.memory('mesProjectiles'):
            p.deplacementProj()
            p.drawProj()

    #ASTEROIDES

        if len(core.memory('mesAsteroides')) < 5:
            self.creationAsteroide()

        for a in core.memory('mesAsteroides'):
            if a.position.x < -40:
                core.memory('mesAsteroides').remove(a)
            elif a.position.x > 840:
                core.memory('mesAsteroides').remove(a)
            elif a.position.y < -40:
                core.memory('mesAsteroides').remove(a)
            elif a.position.y > 840:
                core.memory('mesAsteroides').remove(a)


        for a in core.memory('mesAsteroides'):
            a.deplacementAsteroides()
            a.drawAsteroides()

        #COLLISION ASTEROIDES
        for a in core.memory('mesAsteroides'):
            for p in core.memory('mesProjectiles'):
                hit = a.collision(p)

                if hit:
                    if a.taille > 10:
                        self.creationAsteroide(a.position, a.taille/2)
                        self.creationAsteroide(a.position, a.taille/2)
                    core.memory('mesAsteroides').remove(a)
                    core.memory('mesProjectiles').remove(p)

        for a in core.memory('mesAsteroides'):

                hit = a.collisionPlayer(core.memory("mesPlayers"))

                if hit:
                    if a.taille > 10:
                        self.creationAsteroide(a.position, a.taille/2)
                        self.creationAsteroide(a.position, a.taille/2)
                    core.memory('mesAsteroides').remove(a)
                    if core.memory("mesPlayers").vie > 0:
                        core.memory("mesPlayers").vie = core.memory("mesPlayers").vie - 1
                    else:

                        core.memory("mesPlayers").vie = 3
                        core.memory('mesAsteroides',[])
                        core.memory('mesProjectiles', [])
                        core.memory('mesPlayers').position = Vector2(400,400)
                        core.memory('mesPlayers').vitesse = Vector2(0,0)
                        core.memory('mesPlayers').orientation = Vector2(0, -1)
                        if core.memory('maPartie').score > core.memory('maPartie').scoreMax1:
                            core.memory('maPartie').scoreMax5 = core.memory('maPartie').scoreMax4
                            core.memory('maPartie').scoreMax4 = core.memory('maPartie').scoreMax3
                            core.memory('maPartie').scoreMax3 = core.memory('maPartie').scoreMax2
                            core.memory('maPartie').scoreMax2 = core.memory('maPartie').scoreMax1
                            core.memory('maPartie').scoreMax1 = core.memory('maPartie').score

                        elif core.memory('maPartie').score > core.memory('maPartie').scoreMax2:
                            core.memory('maPartie').scoreMax5 = core.memory('maPartie').scoreMax4
                            core.memory('maPartie').scoreMax4 = core.memory('maPartie').scoreMax3
                            core.memory('maPartie').scoreMax3 = core.memory('maPartie').scoreMax2
                            core.memory('maPartie').scoreMax2 = core.memory('maPartie').score

                        elif core.memory('maPartie').score > core.memory('maPartie').scoreMax3:
                            core.memory('maPartie').scoreMax5 = core.memory('maPartie').scoreMax4
                            core.memory('maPartie').scoreMax4 = core.memory('maPartie').scoreMax3
                            core.memory('maPartie').scoreMax3 = core.memory('maPartie').score

                        elif core.memory('maPartie').score > core.memory('maPartie').scoreMax4:
                            core.memory('maPartie').scoreMax5 = core.memory('maPartie').scoreMax4
                            core.memory('maPartie').scoreMax4 = core.memory('maPartie').score

                        elif core.memory('maPartie').score > core.memory('maPartie').scoreMax5:
                            core.memory('maPartie').scoreMax5 = core.memory('maPartie').score

                        core.memory('maPartie').score = 0
                        core.memory("etat", Etat.GAMEOVER)

                        print(core.memory('maPartie').scoreMax1)
                        print(core.memory('maPartie').scoreMax2)
                        print(core.memory('maPartie').scoreMax3)
                        print(core.memory('maPartie').scoreMax4)
                        print(core.memory('maPartie').scoreMax5)
        #SCORE

        core.memory("maPartie").score += 1







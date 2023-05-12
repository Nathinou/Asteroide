import time

from pygame import Vector2, Rect

import core
from Asteroids.etat import Etat
from Asteroids.map import Map


class Partie:

    def __init__(self):
        self.scoreMax1 = 0
        self.scoreMax2 = 0
        self.scoreMax3 = 0
        self.scoreMax4 = 0
        self.scoreMax5 = 0
        self.map=Map()
        self.timeStart = 0
        self.score = 0

    def afficherMenu(self):
        core.Draw.rect((0,0,0),(369,339,74,20))
        core.Draw.rect((0,0,0), (334, 379, 143, 20))
        core.Draw.text((255, 255, 255), "JOUER", (370, 340), 30, "calibri light")
        core.Draw.text((255, 255, 255), "HIGH SCORES", (335, 380), 30, "calibri light")

        if core.getKeyPressList("SPACE"):
            core.memory("etat", Etat.JEU)

        if core.getMouseLeftClick():
            position = core.getMouseLeftClick()
            rec = Rect(369,339,74,20)
            if rec.collidepoint(position):
                core.memory("etat", Etat.JEU)
            rec = Rect(334, 379, 143, 20)
            if rec.collidepoint(position):
                core.memory("etat", Etat.HIGHSCORE)


    def initJeu(self):
        core.memory("map1").creationPlayer()
        core.memory("map1").creationAsteroide()
        self.timeStart = time.time()

    def afficherJeu(self):

        if core.getKeyPressList("ESCAPE"):
            core.memory("etat", Etat.MENU)

        core.memory("maPartie").map.update()

    def afficherGameOver(self):

        core.Draw.text((255, 255, 255), "GAME OVER", (310, 300), 50, "calibri light")

        core.Draw.rect((0, 0, 0), (369, 349, 100, 20))
        core.Draw.text((255, 255, 255), "REJOUER", (370, 350), 30, "calibri light")

        core.Draw.rect((0, 0, 0), (389, 379, 62, 20))
        core.Draw.text((255, 255, 255), "MENU", (390, 380), 30, "calibri light")

        if core.getMouseLeftClick():
            position = core.getMouseLeftClick()
            rec = Rect(369, 349, 100, 20)
            if rec.collidepoint(position):
                core.memory("etat", Etat.JEU)
            rec = Rect(389,379,62,20)
            if rec.collidepoint(position):
                core.memory("etat", Etat.MENU)




    def afficherHighScore(self):
        core.Draw.rect((0, 0, 0), (20, 20, 90, 20))
        core.Draw.text((255, 255, 255), "RETOUR", (22, 22), 30, "calibri light")

        if core.getMouseLeftClick():
            position = core.getMouseLeftClick()
            rec = Rect(20, 20, 90, 20)
            if rec.collidepoint(position):
                core.memory("etat", Etat.MENU)

    def Enregistrementscore(self):
        pass

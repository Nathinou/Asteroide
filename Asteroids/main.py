import core
from Asteroids import player
from Asteroids.etat import Etat
from Asteroids.map import Map
from Asteroids.partie import Partie
from Asteroids.player import Player


def setup():

    core.WINDOW_SIZE = [800, 800]
    core.fps = 30
    core.memory("mesAsteroides", [])
    core.memory("mesProjectiles", [])
    core.memory("map1", Map())
    p=Partie()
    p.initJeu()
    core.memory("maPartie",p)
    core.memory("etat", Etat.MENU)

def run():
    core.cleanScreen()

    if core.memory("etat") == Etat.MENU:
        core.memory("maPartie").afficherMenu()
    if core.memory("etat") == Etat.JEU:
        core.memory("maPartie").afficherJeu()
    if core.memory("etat") == Etat.GAMEOVER:
        core.memory("maPartie").afficherGameOver()
    if core.memory("etat") == Etat.HIGHSCORE:
        core.memory("maPartie").afficherHighScore()




core.main (setup,run)

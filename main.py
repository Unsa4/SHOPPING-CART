from ProgramManager import ProgramManager
from pygame.time import wait
import pygame as pg


class Main:

    def __init__(self):
        global programManager

        pg.init()

        pg.display.set_caption("Computer Store")
        screen = pg.display.set_mode((800, 600))

        programManager = ProgramManager(screen)

    def MainLoop(self):
        while True:
            wait(1)
            programManager.ManageProgram()


if __name__ == '__main__':
    main = Main()
    main.MainLoop()

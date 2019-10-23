import pygame
import subprocess
import os
import sys
pygame.init()


class GUI:
    def __init__(self, automaton):
        self.automaton = automaton
        self.draw()

    def screen_size(self):
        size = (None, None)
        args = ["xrandr", "-q", "-d", ":0"]
        proc = subprocess.Popen(args, stdout=subprocess.PIPE)
        for line in proc.stdout:
            if isinstance(line, bytes):
                line = line.decode("utf-8")
                if "Screen" in line:
                    size = (int(line.split()[7]), int(line.split()[9][:-1]))
        return size

    def draw(self):

        # screen
        screen = pygame.display.set_mode(self.screen_size())
        pygame.display.set_caption('Automaton')

        # Fonts
        fontP = pygame.font.SysFont("Times new Roman", 20)

        while True:
            screen.fill((76, 217, 138))
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.drawAuto(screen, fontP)
            pygame.display.update()

    def drawAuto(self, screen, fontP):
        for state in self.automaton.states:
            for adj in state.adj:
                pygame.draw.line(screen, (255, 255, 255),
                                 (state.x, state.y), (adj.x, adj.y), 5)

        for state in self.automaton.states:
            pygame.draw.circle(screen, (0, 0, 0),
                               (state.x, state.y), 15)
            screen.blit(fontP.render(
                f"{state.values}", True, (0, 0, 0)), (state.x - 30, state.y + 12))
            screen.blit(fontP.render(
                f"{state.pos}", True, (0, 0, 0)), (state.x + 30, state.y - 12))

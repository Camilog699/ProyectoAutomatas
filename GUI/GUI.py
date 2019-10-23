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
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.drawAuto(screen, fontP)
            pygame.display.update()

    def drawAuto(self, screen, fontP):
        for state in self.automaton.states:
            for adj in state.adj:
                pygame.draw.line(screen, (76, 217, 138),
                                 (state.x, state.y), (adj.x, adj.y), 5)
        ini = self.automaton.states[0]
        pygame.draw.line(screen, (249, 55, 55),
                         (ini.x-50, ini.y), (ini.x, ini.y), 5)

        for state in self.automaton.states:
            if ini.pos is "L":
                if state.values[0] == 0 and state.values[1] == (state.values[0]+state.values[1]):
                    pygame.draw.circle(screen, (249, 55, 55),
                                       (state.x, state.y), 30)
            if ini.pos is "R":
                if state.values[0] == (state.values[0]+state.values[1]) and state.values[1] == 0:
                    pygame.draw.circle(screen, (249, 55, 55),
                                       (state.x, state.y), 30)
            pygame.draw.circle(screen, (255, 255, 255),
                               (state.x, state.y), 20)
            screen.blit(fontP.render(
                f"{state.values}", True, (255, 255, 255)), (state.x - 30, state.y + 12))
            screen.blit(fontP.render(
                f"{state.pos}", True, (255, 255, 255)), (state.x + 30, state.y - 12))
            self.evaluateArrows(screen, state)


    #(c)=Raiz((21)2+(21)2)
    def evaluateArrows(self, screen, state):
        for adj in state.adj:
            #12
            if adj.x == state.x and adj.y < state.y:
                pygame.draw.polygon(screen, (76, 217, 138), [
                                    (adj.x, adj.y+15), (adj.x-15, adj.y+45), (adj.x+15, adj.y+45)])
            #1
            if adj.x > state.x and adj.y < state.y:
                pygame.draw.polygon(screen, (76, 217, 138), [
                                    (adj.x-15, adj.y+15), (adj.x-45, adj.y+15), (adj.x-15, adj.y+45)])
            #3
            if adj.x > state.x and adj.y == state.y:
                pygame.draw.polygon(screen, (76, 217, 138), [
                                    (adj.x-15, adj.y), (adj.x-45, adj.y-15), (adj.x-45, adj.y+15)])
            #5
            if adj.x > state.x and adj.y > state.y:
                pygame.draw.polygon(screen, (76, 217, 138), [
                                    (adj.x-15, adj.y-15), (adj.x-15, adj.y-45), (adj.x-45, adj.y-15)])
            #6
            if adj.x == state.x and adj.y > state.y:
                pygame.draw.polygon(screen, (76, 217, 138), [
                                    (adj.x, adj.y-15), (adj.x-15, adj.y-45), (adj.x+15, adj.y-45)])
            #7
            if adj.x < state.x and adj.y > state.y:
                pygame.draw.polygon(screen, (76, 217, 138), [
                                    (adj.x+15, adj.y-15), (adj.x+15, adj.y-45), (adj.x+45, adj.y-15)])
            #9
            if adj.x < state.x and adj.y == state.y:
                pygame.draw.polygon(screen, (76, 217, 138), [
                                    (adj.x+15, adj.y), (adj.x+45, adj.y-15), (adj.x+45, adj.y-15)])
            #11
            if adj.x < state.x and adj.y < state.y:
                pygame.draw.polygon(screen, (76, 217, 138), [
                                    (adj.x+15, adj.y+15), (adj.x+15, adj.y+45), (adj.x+45, adj.y+15)])

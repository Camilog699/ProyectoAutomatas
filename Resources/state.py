from random import randint
class State:

    def __init__(self, values, adj, pos):
        self.values = values
        self.adj = adj
        self.pos = pos
        self.x = randint(20, 1200)
        self.y = randint(20, 700)

    def __eq__(self, node):
        sal = (node.values[0] == self.values[0] and node.values[1] == self.values[1] and node.pos is self.pos)
        return sal

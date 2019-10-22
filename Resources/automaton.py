from Resources.state import State


class Automaton:

    def __init__(self):
        self.pos = {"L1", "L2", "R1", "R2"}
        self.root = None
        self.visited = []
        self.states = []

    def AddRoot(self, val1, val2, adj, pos):
        if self.root is None:
            self.root = State([val1, val2], adj, pos)
            self.states.append(self.root)
            self.Transitions(self.root)
            for node in self.states:
                print(f"{node.values}, {node.pos}")

    def Transitions(self, state):
        if state.pos is 'L':
            if state.values[0] >= 1 and state.values[1] <= 3:
                newState = State(
                    [state.values[0]-1, state.values[1]+1], [], "R")
                exist = True
                for evaluated in self.states:
                    if newState == evaluated:
                        for node in state.adj:
                            if evaluated == node:
                                exist = True
                                break
                            else:
                                exist = False
                        if not exist:
                            state.adj.append(evaluated)
                            exist = True
                            break
                    else:
                        exist = False
                if not exist:
                    state.adj.append(newState)
                    self.states.append(newState)
            if state.values[0] >= 2 and state.values[1] <= 2:
                newState = State(
                    [state.values[0]-2, state.values[1]+2], [], "R")
                exist = True
                for evaluated in self.states:
                    if newState == evaluated:
                        for node in state.adj:
                            if evaluated == node:
                                exist = True
                                break
                            else:
                                exist = False
                        if not exist:
                            state.adj.append(evaluated)
                            exist = True
                            break
                    else:
                        exist = False
                if not exist:
                    state.adj.append(newState)
                    self.states.append(newState)
        if state.pos is "R":
            if state.values[1] >= 1 and state.values[0] <= 3:
                newState = State(
                    [state.values[0]+1, state.values[1]-1], [], "L")
                exist = True
                for evaluated in self.states:
                    if newState == evaluated:
                        for node in state.adj:
                            if evaluated == node:
                                exist = True
                                break
                            else:
                                exist = False
                        if not exist:
                            state.adj.append(evaluated)
                            exist = True
                            break
                    else:
                        exist = False
                if not exist:
                    state.adj.append(newState)
                    self.states.append(newState)
            if state.values[1] >= 2 and state.values[0] <= 2:
                newState = State(
                    [state.values[0]+2, state.values[1]-2], [], "L")
                exist = True
                for evaluated in self.states:
                    if newState == evaluated:
                        for node in state.adj:
                            if evaluated == node:
                                exist = True
                                break
                            else:
                                exist = False
                        if not exist:
                            state.adj.append(evaluated)
                            exist = True
                            break
                    else:
                        exist = False
                if not exist:
                    state.adj.append(newState)
                    self.states.append(newState)
        self.visited.append(state)
        for child in state.adj:
            if child not in self.visited:
                self.Transitions(child)
        return state

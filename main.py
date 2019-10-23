from Resources.automaton import Automaton
from GUI.GUI import GUI


def main():
    automaton = Automaton()
    automaton.AddRoot(4, 0, [], 'L')
    GUI(automaton)

main()

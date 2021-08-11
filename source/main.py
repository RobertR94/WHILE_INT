from controller import Controller
import sys


if __name__ == "__main__":
    c = Controller()
    c.run("../WhilePrograms/" + sys.argv[1])
    exit()
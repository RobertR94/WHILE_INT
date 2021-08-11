from interpreter import Interpreter


class Controller:


    def __init__(self):
        self.interpreter = Interpreter()
        return 
    

    def run(self, p):
        self.interpreter.read(path=p)
        return
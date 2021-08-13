from interpreter import Interpreter


class Controller:


    def __init__(self):
        self.interpreter = Interpreter()
        return 
    

    def run(self, p):
        result = self.interpreter.read(path=p)
        print(result)
        return
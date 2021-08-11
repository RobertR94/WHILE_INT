class Interpreter:

    def __init__(self):
        self.makros = dict()
        self.attributes = dict()
        self.loops = ["LOOP", "WHILE"]
        return


    def read_file(self, path):
        code = list()
        with open(path) as p:
            for line in p:
                code.extend(line.split())
        print(code)
        return code



    def read_makro(self, makros):
        for makro in makros:
            name = makro.pop(0)
            if makro.pop(0) == "DO":
                self.makros[name] = []
                for elem in makro:
                    self.makros[name].append(elem)
        return
    

    def get_makros(self, code):
        done = False
        i = 0
        cnt = 0
        makros = list()
        while i < len(code) and done == False:
            makro = list()
            if code[i] == "define":
                cnt += 1
                i += 1
                while cnt > 0:
                    if code[i] in self.loops:
                        cnt += 1
                        makro.append(code[i])
                    elif code[i] == "END":
                        cnt -= 1
                        if cnt != 0:
                            makro.append(code[i])
                    elif code[i] != ":":
                        makro.append(code[i]) 
                    i += 1
                makros.append(makro)
            else:
                done = True
        self.read_makro(makros)
        return i
                        



    def interpret(self, code, pos):
        i = 0
        while i < len(code):
            if code[i] == self.loops[0]:
                #LOOP
                return self.interpret(code, pos)
            elif code[i] == self.loops[1]:
                #WHILE
                return
            elif code[i][0].islower() and code[i+1] == ":=":
                i = i + 2
            else:
                return "Invalid format!"

        return 
    

    def read(self, path):
        code = self.read_file(path)
        pos = self.get_makros(code)
        print(self.makros)
        #return self.interpret(code, pos)
import copy

class Interpreter:

    def __init__(self):
        self.makros = dict()
        self.attributes = dict()
        self.attributes["x_0"] = 0
        self.loops = ["LOOP", "WHILE"]
        self.code = None
        return


    def read_file(self, path):
        code = list()
        with open(path) as p:
            for line in p:
                code.extend(line.split())
        print(code)
        self.code = code
        return 



    def read_makro(self, makros):
        for makro in makros:
            name = makro.pop(0)
            if makro.pop(0) == "DO":
                self.makros[name] = []
                for elem in makro:
                    self.makros[name].append(elem)
        return
    

    def get_makros(self):
        done = False
        i = 0
        cnt = 0
        makros = list()
        while i < len(self.code) and done == False:
            makro = list()
            if self.code[i] == "define":
                cnt += 1
                i += 1
                while cnt > 0:
                    if self.code[i] in self.loops:
                        cnt += 1
                        makro.append(self.code[i])
                    elif self.code[i] == "END":
                        cnt -= 1
                        if cnt != 0:
                            makro.append(self.code[i])
                    elif self.code[i] != ":":
                        makro.append(self.code[i]) 
                    i += 1
                makros.append(makro)
            else:
                done = True
        self.read_makro(makros)
        return i


    def add(self, x, y, operator):
        if operator == "+":
            return x + y
        else:
            if x - y < 0:
                return 0
            return x - y


    def interpret(self, i):
        while i < len(self.code):
            if self.code[i] == self.loops[0]:
                #LOOP
                i += 1
                num_it = self.attributes[self.code[i]]
                i += 1
                if self.code[i] == "DO":
                    i += 1
                    for num in range(num_it):
                        pos = self.interpret(i)
                    i = pos
                else:
                    return "Ivalid LOOP"
            elif self.code[i] == self.loops[1]:
                #WHILE
                return
            elif self.code[i][0].islower() and self.code[i+1] == ":=":
                x  = self.code[i]
                if x not in self.attributes.keys():
                    self.attributes[x] = 0

                if self.code[i+2].isdigit():
                    self.attributes[x] = int(self.code[i+2])
                    i = i + 3
                elif self.code[i+2] in self.attributes.keys():
                    self.attributes[x] = self.add(self.attributes[self.code[i+2]], int(self.code[i+4]), self.code[i+3])
                    i = i + 5
                else:
                    return "Invalid format add"
            elif self.code[i] == "END":
                return i + 1
            else:
                return "Invalid format!"

        return self.attributes["x_0"]
    

    def read(self, path):
        self.read_file(path)
        pos = self.get_makros()
        return self.interpret(pos)
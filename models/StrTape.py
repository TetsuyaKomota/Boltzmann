# coding = utf-8

from models.AlphabetTable import table

class StrTape:

    def __init__(self):
        self.tape = []
        self.head = 0

    def getLength(self):
        return len(self.tape)

    def initHead(self):
        self.head = 0

    def pushCode(self, code):
        self.tape = [code] + self.tape

    def appendCode(self, code):
        self.tape.append(code)

    def inputStr(self, string):
        for alph in string:
            t = table[alph]
            for i in range(len(t[0])):
                tempcode = []
                for l in t:
                    tempcode.append(int(l[i]))
                self.appendCode(tempcode)

    def getNext(self):
        flag = (self.head == len(self.tape)-1)
        code = self.tape[self.head]
        if flag == True:
            self.head = 0
        else:
            self.head += 1
        return [flag, code]

    def show(self, length):
        codelen = len(self.tape[0])
        output = ["" for _ in range(codelen)]
        for _ in range(length):
            code = self.getNext()[1]
            for i in range(codelen):
                output[i] += str(code[i])

        return output

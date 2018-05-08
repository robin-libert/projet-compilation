class Programme:

    def __init__(self, element1 , element2):
        self.element1 = element1
        self.element2 = element2

    def evaluate(self):
        self.element1.evaluate()
        if self.element2 is not None:
            self.element2.evaluate()


class ExpressionList:
    def __init__(self, element1 , element2):
        self.element1 = element1
        self.element2 = element2

    def evaluate(self):
        self.element1.evaluate()
        if self.element2 is not None:
            self.element2.evaluate()

class ForExpression:
   def __init_(self, var, stringList, expressionList):
        self.var = var
        self.stringList = stringList
        self.expressionList = expressionList

class Eprint:
    def __init__(self, txt):
        self.txt = txt

    def evaluate(self):
        print(self.txt)


class Text:
    
    def __init__(self, txt):
        self.txt = txt

    def evaluate(self):
        print(self.txt)

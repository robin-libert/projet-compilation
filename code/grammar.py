class Programme:

    def __init__(self, element1 , element2):
        self.element1 = element1
        self.element2 = element2

    def evaluate(self, dico):
        self.element1.evaluate(dico)
        if self.element2 is not None:
            self.element2.evaluate(dico)


class ExpressionList:
    def __init__(self, element1 , element2):
        self.element1 = element1
        self.element2 = element2

    def evaluate(self, dico):
        self.element1.evaluate(dico)
        if self.element2 is not None:
            self.element2.evaluate(dico)

class ForExpression:
   def __init__(self, var, stringList, expressionList):
        self.var = var
        self.stringList = stringList
        self.expressionList = expressionList

   def evaluate(self, dico):
        for elem in self.stringList.evaluate(dico):
            self.dico = dico.copy() #pour plus de securite chacun aura son dico
            self.dico[self.var] = EString(elem)
            self.expressionList.evaluate(self.dico)

class Eprint:
    def __init__(self, txt):
        self.txt = txt

    def evaluate(self, dico):
        txtTMP = self.txt.evaluate(dico)
        print(txtTMP,end='')

class StringList:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def evaluate(self, dico):
        if self.var2 is None:
            return [self.var1.evaluate(dico)]
        else:
            return [self.var1.evaluate(dico)] + self.var2.evaluate(dico)

class StringExpression:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def evaluate(self, dico):
        if self.var2 is None:
            return self.var1.evaluate(dico)
        else:
            return self.var1.evaluate(dico) + self.var2.evaluate(dico)

class EString:
    def __init__(self, txt):
        self.txt = txt
    
    def evaluate(self, dico):
        return self.txt

class EVariable:
    def __init__(self, var):
        self.var = var

    def evaluate(self,dico):
        return dico[self.var].evaluate(dico)

class Text:
    
    def __init__(self, txt):
        self.txt = txt

    def evaluate(self, dico):
        print(self.txt,end='')

#programme avec en element1 un text ou un dumboBloc et en elment deux (si il y en a un) un autre programme.
class Programme:

    def __init__(self, element1 , element2):
        self.element1 = element1
        self.element2 = element2

    def evaluate(self, dico):
        self.element1.evaluate(dico)
        if self.element2 is not None:
            self.element2.evaluate(dico)

#liste d'expression contenant en premier elment une expression et en deuxieme elment (si il y en a un) une autre liste d'expression.
class ExpressionList:
    def __init__(self, element1 , element2):
        self.element1 = element1
        self.element2 = element2

    def evaluate(self, dico):
        self.element1.evaluate(dico)
        if self.element2 is not None:
            self.element2.evaluate(dico)

#cette classe affiche l'elment dans la classe qui lui est envoyee (la classe doit avoir sa methode "evaluate" qui lui renvoi un elment a afficher)
class Eprint:
    def __init__(self, txt):
        self.txt = txt

    def evaluate(self, dico):
        txtTMP = self.txt.evaluate(dico)
        print(txtTMP,end='')

#fais un if (ou if else si on lui envoit deux expression list) avec comme condition le boolean qui lui est envoye.
class IfExpression:
    def __init__(self, boolean, expressionList1, expressionList2):
        self.boolean = boolean
        self.expressionList1 = expressionList1
        self.expressionList2 = expressionList2


    def evaluate(self, dico):
        if(self.boolean.evaluate(dico)):
            self.expressionList1.evaluate(dico)
        elif self.expressionList2 is not None:
            self.expressionList2.evaluate(dico)

#la methode evaluate de la classe renvoi soit un entier si il n'y a qu'un element soit l'operation entre le premier et le second entier (var1 et var2).
class globalInteger:

    def __init__(self, var1, opera, var2):
        self.var1 = var1
        self.var2 = var2
        self.opera = opera

    def evaluate(self, dico):
        operations = {
        '+' : lambda x , y: x+y,
        '-' : lambda x , y: x-y,
        '*' : lambda x , y: x*y,
        '/' : lambda x , y: x/y,
        }
        if(self.opera is None or self.var2 is None):
            return self.var1.evaluate(dico)
        else:
            return operations[self.opera](self.var1.evaluate(dico),self.var2.evaluate(dico))

#la methode evaluate de la classe renvoi l'operation binaire entre les deux variables (var1 et var2).
class booleanExpression:

    def __init__(self, var1, opera, var2):
        self.var1 = var1
        self.var2 = var2
        self.opera = opera

    def evaluate(self, dico):
        operator = {
        '<' : lambda x , y: x<y,
        '>' : lambda x , y: x>y,
        '=' : lambda x , y: x==y,
        '!=' : lambda x , y: x!=y,
        }
        return operator[self.opera](self.var1.evaluate(dico),self.var2.evaluate(dico))

#la methode evaluate de la classe renvoi le boolean ou le resultat de l'operation entre les deux boolean (si il y a deux boolean).
class boolean:
    def __init__(self, var1, opera, var2):
        self.var1 = var1
        self.var2 = var2
        self.opera = opera
    
    def evaluate(self, dico):
        operator = {
        'and' : lambda x , y: x and y,
        'or' : lambda x , y: x or y,
        }
        if(self.opera is None or self.var2 is None):
            return self.var1.evaluate(dico)
        else:
            return operator[self.opera](self.var1.evaluate(dico),self.var2.evaluate(dico))

#la methode evaluate de la classe change la valeur de la variable var dans le dictionnaire et l'envoi a la liste d'expression pour chaque variable de la liste.
class ForExpression:
    def __init__(self, var, stringList, expressionList):
        self.var = var
        self.stringList = stringList
        self.expressionList = expressionList

    def evaluate(self, dico):
        for elem in self.stringList.evaluate(dico):
            dico2 = dico.copy() #pour plus de securite chacun aura son dico
            dico2[self.var] = EForVariable(elem)
            self.expressionList.evaluate(dico2)

#represente une list avec var1 le debut de la liste et var2 la suite de la liste.
class List:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def evaluate(self, dico):
        if self.var2 is None:
            return [self.var1.evaluate(dico)]
        else:
            return [self.var1.evaluate(dico)] + self.var2.evaluate(dico)

#fais un string si il y a un elemenent (var1) ou une concatenation de string si il y a deux element(var1.var2) 
class StringExpression:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def evaluate(self, dico):
        if self.var2 is None:
            return self.var1.evaluate(dico)
        else:
            return self.var1.evaluate(dico) + self.var2.evaluate(dico)


class booleanVAR:
    def __init__(self, elem):
        self.elem = elem
    
    def evaluate(self, dico):
        return self.elem

class EForVariable:
    def __init__(self, elem):
        self.elem = elem
    
    def evaluate(self, dico):
        return self.elem

class IntegerVar:
    def __init__(self, inte):
        self.inte = inte

    def evaluate(self, dico):
        return self.inte

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

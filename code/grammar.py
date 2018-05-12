class Programme:
    #Cette classe un programme/sous-programme qui prend en premier parametre un texte ou un dumbo Bloc et en deuxième parametre un programme/sous-programme ou rien.
    def __init__(self, element1 , element2):
        self.element1 = element1
        self.element2 = element2

    def evaluate(self, dico):
        #evalue les deux elements (ou l'ements si il n'y en a qu'un) envoye en parametre.
        x = self.element1.evaluate(dico)
        if(x is not None):
            dico = x
        if self.element2 is not None:
            y = self.element2.evaluate(dico)
            if(y is not None):
                dico = y
        return dico
    

class ExpressionList:
    #Cette classe represente une liste d'expression qui prend en premier parametre une expression et en deuxieme si il y en a une une liste d'expression.
    def __init__(self, element1 , element2):
        self.element1 = element1
        self.element2 = element2


    def evaluate(self, dico):
        #evalue les deux elements (ou l'ements si il n'y en a qu'un) envoye en parametre.
        x = self.element1.evaluate(dico)
        if(x is not None):
            dico = x
        if self.element2 is not None:
            y = self.element2.evaluate(dico)
            if(y is not None):
                dico = y
        return dico


class Eprint:
    #Cette classe effectue la fonction d'un print et prend une global expression en parametre.
    def __init__(self, txt):
        self.txt = txt

    def evaluate(self, dico):
        #affiche l'element.
        txtTMP = self.txt.evaluate(dico)
        print(txtTMP,end='')

#fais un if (ou if else si on lui envoit deux expression list) avec comme condition le boolean qui lui est envoye.
class IfExpression:
    def __init__(self, boolean, expressionList1, expressionList2):
        self.boolean = boolean
        self.expressionList1 = expressionList1
        self.expressionList2 = expressionList2


    def evaluate(self, dico):
        v = self.boolean.evaluate(dico)
        if(v == 'true'):
            self.expressionList1.evaluate(dico)
        elif self.expressionList2 is not None:
            self.expressionList2.evaluate(dico)

#la methode evaluate de la classe renvoi soit un entier si il n'y a qu'un element soit l'operation entre le premier et le second entier (var1 et var2).
class globalExpression:

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
        '<' : lambda x , y: x<y,
        '>' : lambda x , y: x>y,
        '=' : lambda x , y: x==y,
        '!=' : lambda x , y: x!=y,
        'and' : lambda x , y: x and y,
        'or' : lambda x , y: x or y,
        '.' : lambda x , y: "{0}{1}".format(x , y),
        }
        if(self.opera is None or self.var2 is None):
            return self.var1.evaluate(dico)
        else:
            return operations[self.opera](self.var1.evaluate(dico),self.var2.evaluate(dico))

#la methode evaluate de la classe change la valeur de la variable var dans le dictionnaire et l'envoi a la liste d'expression pour chaque variable de la liste.
class ForExpression:
    def __init__(self, var, stringList, expressionList):
        self.var = var
        self.stringList = stringList
        self.expressionList = expressionList

    def evaluate(self, dico):
        for elem in self.stringList.evaluate(dico):
            dico2 = dico.copy() #pour plus de securite chacun aura son dico
            dico2[self.var] = ElementVAR(elem)
            dico = self.expressionList.evaluate(dico2)
        return dico
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

class VariableASS:
    def __init__(self, variable, elem):
        self.variable = variable
        self.elem = elem
    
    def evaluate(self, dico):
        dico[self.variable] = ElementVAR(self.elem.evaluate(dico))
        return dico

class ElementVAR:
    def __init__(self, elem):
        self.elem = elem
    
    def evaluate(self, dico):
        return self.elem

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

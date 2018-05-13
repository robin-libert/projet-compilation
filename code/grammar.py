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
        dico['+'] = (dico['+'] + str(txtTMP))
        return dico


class IfExpression:
    #Cette classe represente un if si il y a deux parametre (le premier etant la condition et le second l'expression) si un troisieme parametre est passe alors celui-ci est pris comme l'expression du else.
    def __init__(self, boolean, expressionList1, expressionList2):
        self.boolean = boolean
        self.expressionList1 = expressionList1
        self.expressionList2 = expressionList2


    def evaluate(self, dico):
        #calcul la condition avant de la gerer.
        v = self.boolean.evaluate(dico)
        if(v == 'true'):
            self.expressionList1.evaluate(dico)
        elif self.expressionList2 is not None:
            self.expressionList2.evaluate(dico)


class globalExpression:
    #Cette classe represente une expression de type boolean, integer ou string.Formatter le premier element doit sauf pour la concatenation etre du meme type que le troisieme element(si il y en a un)
    def __init__(self, var1, opera, var2):
        self.var1 = var1
        self.var2 = var2
        self.opera = opera

    # retourne le premier element et si il y a trois element l'opration sur le premeier et le troisieme element.
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


class ForExpression:
    #Cette classe represente un for.
    def __init__(self, var, stringList, expressionList):
        self.var = var
        self.stringList = stringList
        self.expressionList = expressionList

    #envoi la valeur de chaque variable de la liste dans l'expression.
    def evaluate(self, dico):
        self.dicoTMP = dico
        for elem in self.stringList.evaluate(dico):
            dico2 = self.dicoTMP.copy() #pour plus de securite chacun aura son dico
            dico2[self.var] = ElementVAR(elem)
            self.dicoTMP = self.expressionList.evaluate(dico2)
        return self.dicoTMP

    
class List:
    #Cette classe represente une liste.
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    #renvoi une liste avec le premier element et (si il y en a une) la suite de la liste.
    def evaluate(self, dico):
        if self.var2 is None:
            return [self.var1.evaluate(dico)]
        else:
            return [self.var1.evaluate(dico)] + self.var2.evaluate(dico)

class VariableASS:
    #Cette classe represente une assignation de variable
    def __init__(self, variable, elem):
        self.variable = variable
        self.elem = elem

    #assigne la variable dans le dictionnaire et la renvoi.
    def evaluate(self, dico):
        dico[self.variable] = ElementVAR(self.elem.evaluate(dico))
        return dico


class ElementVAR:
    #cette classe represente un element.
    def __init__(self, elem):
        self.elem = elem

    #revoi cet element.
    def evaluate(self, dico):
        return self.elem

class EVariable:
    #Cette classe represenete une variable
    def __init__(self, var):
        self.var = var

    #renvoi la valeur de cette variable dans le dictionnaire.
    def evaluate(self,dico):
        return dico[self.var].evaluate(dico)

class Text:
    #Cette classe represente le texte hors dumbo Bloc
    def __init__(self, txt):
        self.txt = txt

    def evaluate(self, dico):
        txtTMP = self.txt
        dico['+'] = (dico['+'] + txtTMP)
        return dico

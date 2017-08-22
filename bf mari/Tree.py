class No:
    def __init__(self,valor):
        self.info=valor
        self.esq=None
        self.dir=None

    def imprimir(self):
        self.busca()
    def insereRaiz(self, valor):
        if self.info == None:
            self.info = No(valor)
        else:
            print("Raiz já preenchida!")
           
    def insereDireita(self, valor):
        self.dir = No(valor)
        print(self.dir.info, end=": na direita.\n")
                    
    def insereEsquerda(self, valor):
        self.esq = No(valor)
        print(self.esq.info, end=": na esquerda.\n")
        
    def insereNaEsquerdaDaDireita(self, valor):
        self.dir.esq = No(valor)
        print(self.dir.info.esq.info, end=": na esquerda da direita.\n")
           
    def insereNaDireitaDaEsquerda(self, valor):
        self.esq.dir = No(valor)
        print(self.esq.dir.info, end=": na direita da esquerda.\n")
        

    
            
                
    def busca(self, valor):
        if valor == self.info:
            print(self.info, end=": elemento está na raiz.\n")
            
        if valor == self.dir.info:
            print(self.dir.info, end=": elemento está na direita.\n")
            
        if valor == self.dir.esq.info:
            print(self.dir.esq.info, end=": elemento na esquerda da direita.\n")
            
        if valor == self.esq.dir.info:
            print(self.esq.dir.info, end=": elemento na direita da esquerda.\n")
            
             
'''------------------------------------------------------------------'''    

class Tree:
    def __init__(self):
        self.raiz=None
        
    def insereRaiz(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
            print(valor, end=": na raiz.\n")
        else:
            self.raiz.insereRaiz(valor)
            print(valor, end=": não é possível inserir. Raiz ocupada!\n")
        
                  
    def insereDireita(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
            
        else:
            self.raiz.insereDireita(valor)

    def insereEsquerda(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
            
        else:
            self.raiz.insereEsquerda(valor)

    def insereNaEsquerdaDaDireita(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
            
        else:
            self.raiz.insereNaEsquerdaDaDireita(valor)

    def insereNaDireitaDaEsquerda(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
            
        else:
            self.raiz.insereNaDireitaDaEsquerda(valor)

    
           
    def busca(self, valor):
        if self.raiz == None:
            return True
        else:
                        
            return self.raiz.busca(valor)


        

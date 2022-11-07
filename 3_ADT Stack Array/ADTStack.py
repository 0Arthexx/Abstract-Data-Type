class stack :
    ## Definisi Konstruktor
    # Kamus Lokal
    # N : ukuran stack
    def __init__(self,N):
        self.items = [None]*(N+1)
        self.size = N
        self.top = 0
        return

    ## Definisi Method pop()
    # Kamus Lokal
    # X : nilai yang akan dikembalikan (integer)
    def pop(self):
        X = self.items[self.top-1]
        self.top = self.top - 1
        self.items[self.top] = None
        return X
    
    ## Definisi Method push(X)
    # Kamus Lokal
    # X : nilai yang akan dimasukkan (integer)
    def push(self, X):
        self.items[self.top] = X
        self.top = self.top + 1
        return
    
    ## Definisi Method isEmpty()
    # Kamus Lokal
    def isEmpty(self):
        return self.top == 0
    
    ## Definisi Method isFull()
    # Kamus Lokal
    def isFull(self):
        return self.top == self.size
    
    ## Definisi Method infoTop()
    # Kamus Lokal
    def infoTop(self):
        return self.items[self.top - 1]
    
    ## Definisi Method countElm()
    # Kamus Lokal
    def CetakStack(self):
        for i in range(self.size-1,-1,-1):
            print(self.items[i])

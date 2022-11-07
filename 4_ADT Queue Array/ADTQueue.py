class Queue():
    ## Definisi Konstruktor
    # Kamus Lokal
    # size : ukuran queue (integer)
    def __init__(self,size):
        self.head = -1
        self.tail = -1
        self.MaxEl = size
        self.items = [None]*(size+1)

    def insert(self, X):
        if (self.isEmpty()):
            self.head = 1
            self.tail = 1
            self.items[self.tail] = X
        else:
            self.tail += 1
            self.items[self.tail] = X

    def delete(self):   
        self.items[self.head] = None
        for i in range (self.head, self.tail+1):
            self.items[i] = self.items[i+1]
            
        if(self.tail > 0):
            self.tail -= 1
        else:
            self.head == -1
            self.tail = 0

    ## Definisi Method isEmpty()
    # Kamus Lokal
    def isEmpty(self):
        return (self.head == 0 and self.tail == 0)
    
    ## Definisi Method isFull()
    # Kamus Lokal
    def isFull(self):
        return self.head == self.items
    
    def CetakQueue(self):
        for i in range(0,self.MaxEl):
            print("Data [", self.items[i], "] di Index ke - [", i, "]")

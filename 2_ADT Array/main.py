class MyArray :
    def __init__(self,size):
        self.items = [None]*size
        self.maxElmt = size
        self.N = 0
        return

## Definisi Method isiArray()
# Kamus Lokal
# NN : var input (integer)
# i : var iterator (integer)
    def isiArray(self):
        NN = int(input("Nilai N : "))
        for i in range(0,NN):
            self.items[i] = int(input("Nilai X : "))
        self.N = NN
        return

    def search(self, x):
        nm = 0
        for i in range(0, self.N):
            if x == self.items[i]:
                nm = self.items[i]
        if nm > 0 : 
            print(nm)
        else: 
            print("Nilai", x ,"tidak ada")

    def isEmpty(self):
        return self.N == 0
    
    def isFull(self):
        return self.N == self.maxElmt

    def printarray(self):
        for i in range(0, self.N):
            print("A","[",i,"]","=",self.items[i])

    def AddEiFirst(self,X):
        Na = -1
        for i in range(0, self.N):
            if(self.items[i] == X):
                Na = X
        if(Na >= 0):
            for i in range(0, self.N):
                print('A','[',i,']','=', self.items[i])
        else:
            self.N = self.N + 1
            for i in range(self.N, 0, -1):
                self.items[i] = self.items[i-1]
            self.items[0] = X
            for i in range(0,self.N):
                print('A','[',i,']','=',self.items[i])    
                
    def Inverse(self):
        inverse = [None] * self.N
        inv = self.N - 1
        for i in range (0, self.N):
            inverse[inv] = self.items[i]
            inv-=1
        for j in range (0, self.N):
            print("A","[",i,"]","=",inverse[j])
                
def main():
    A = MyArray(5)
    print('Input Data Array')
    A.isiArray()

    print('Isi Array : ')
    A.printarray()

    x = int(input("Input nilai yang dicari "))
    A.search(x)

    x = int(input("Tambah Data Baru : "))
    A.AddEiFirst(x)

    x = int(input("Tambah Data Baru : "))
    A.AddEiFirst(x)

    print('Inverse Array : ')
    A.Inverse()
if __name__ == '__main__':
    main()
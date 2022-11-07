class MyListElement():
    ## Definisi Konstruktor
    # Kamus Lokal
    # value : var yang menyimpan nilai (integer)
    def __init__(self, value):
        self.info = value
        self.next = None
        return


## Definisi Kelas Node
## Definisi Atribut
# value : atribut yang menyimpan nilai (integer)
# next : atribut reference elemen berikutnya (Node)
class QueueList():
    ## Definisi Konstruktor
    # Kamus Lokal
    def __init__(self):
        self.head = None
        self.tail = None
        return

    ## Definisi Method countElm()
    # Kamus Lokal
    # P : iterator node (Node)
    # c : counter node (integer)
    def countElm(self):
        P = self.head
        c = 0
        while (P!=None):
            c = c + 1
            P = P.next
        return c
    
    ## Definisi Method isEmpty()
    # Kamus Lokal
    def isEmpty(self):
        return (self.head == None)
    
    ## Definisi Method insert(X)
    # Kamus Lokal
    # X : elemen yang ditambahkan (integer)
    # Q : node X (Node)
    def enqueue(self, X):
        Q = MyListElement(X)
        if self.isEmpty():
            self.head = Q
            self.tail = Q
        else:
            self.tail.next = Q
            self.tail = Q
        return

    ## Definisi Method delete()
    # Kamus Lokal
    # Q : node terbuang (Node)
    def dequeue(self):
        Q = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return Q.info
    
    def traversal(self):
        if self.head == None:
            print("List Kosong")
        else:
            a = self.head
            while (a.next != None):
                print(a.info, end=" ")
                a = a.next
            print(a.info)
    
def main():
    A = QueueList()
    print("Menu : ")
    print("1. enqueue")
    print("2. dequeue")
    print("3. traversal")
    print("0. Keluar")
    Menu = int(input("Pilihan Anda : "))
    while Menu != 0:
        if Menu == 1:
            isi = int(input("Masukkan : "))
            A.enqueue(isi)
            print("===============")
        elif Menu == 2:
            A.dequeue()
            print("===============")
        elif Menu == 3:
            A.traversal()
            print("===============")
        Menu = int(input("Pilihan Anda : "))
if __name__ == '__main__':
    main()
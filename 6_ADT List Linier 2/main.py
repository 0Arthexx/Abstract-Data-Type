## Definisi Kelas Node
## Definisi Atribut
# value : atribut yang menyimpan nilai (integer)
# next : atribut reference elemen berikutnya (Node)
class Node():
    ## Definisi Konstruktor
    # Kamus Lokal
    # value : var yang menyimpan nilai (integer)
    def __init__(self, value):
        self.info = value
        self.next = None
        return

## Definisi Kelas QueueList
## Definisi Atribut
# head : atribut reference elemen pertama (Node)
# tail : atribut reference elemen terakhir (Node)
class QueueList():
    ## Definisi Konstruktor
    # Kamus Lokal
    def __init__(self):
        self.first = None
        return

    ## Definisi Method insert(X)
    # Kamus Lokal
    # X : elemen yang ditambahkan (integer)
    # Q : node X (Node)
    def InsertF(self, Q):
        Q.next = self.first
        self.first = Q
        return

    ## Definisi Method InsertLast(a)
    # Kamus Lokal
    # a  : parameter nilai yang akan ditambahkan pada list (Node)
    # last : var yang akan menyimpan reference elemen terakhir (Node)
    def InsertL(self, a):
        if (self.first == None):
            self.InsertFirst(a)
        else:
            last = self.first
            while (last.next != None):
                last = last.next
            last.next = a 
        return
    
    ## Definisi Method isEmpty()
    # Kamus Lokal
    def isEmpty(self):
        return (self.first == None )
    
    
## Definisi Method delete()
# Kamus Lokal
# Q : node terbuang (Node)
    def DeleteF(self):
        Q = self.first
        self.first = self.first.next
        Q.next = None
        return Q.info
    
    ## Mengambil RemoveLast Program dari Praktikum 5 ##
    ## Definisi Method RemoveLast()
    # Kamus Lokal
    # last : elemen terbuang dari list (MyListElement)
    # prevlast : penyimpan reference elemen kedua terakhir (MyListElement)
    # lastinfo : penyimpan last info dari list element
    def DeleteL(self):
        if (self.first.next == None):
            last = self.first
            self.first = None
            lastinfo= last.info
        else:
            prevlast = None 
            last = self.first
            while (last.next != None):
                prevlast = last
                last = last.next
            prevlast.next = None
            lastinfo= last.info
        return lastinfo

    ## Definisi Method traversal()
    # Kamus Lokal
    # temp : penyimpan sementara nilai dari self.info (int)
    def traversal(self):
        temp = self.first
        while (temp.next != None):
            print(temp.info, end=" ")
            temp = temp.next
        print(temp.info, end="")
        print()
        return
    
# Program Utama
def main():
    A = QueueList()
    print("Kondisi List : ")
    print("Menu : ")
    print("1. Insert First")
    print("2. Insert Last")
    print("3. Delete First")
    print("4. Delete Last")
    print("0. Keluar")
    Menu = int(input("Pilihan Anda : "))
    while Menu != 0:
        if Menu == 1:
            InsNamaF = Node(str(input("Masukkan Nama : "))) 
            A.InsertF(InsNamaF)
            print("===============")
        elif Menu == 2:
            InsNamaL = Node(str(input("Masukkan Nama : ")))
            A.InsertL(InsNamaL)
            print("===============")
        elif Menu == 3:
            rf = A.DeleteF()
            print(rf, "terhapus")
            print("===============")
        elif Menu == 4:
            rl = A.DeleteL()
            print(rl, "terhapus")
            print("===============")
        Menu -= 1
        print("Kondisi List : ")
        if A.isEmpty() == True:
            print("List kosong")
        else:
            A.traversal()
        print("Menu : ")
        print("1. Insert First")
        print("2. Insert Last")
        print("3. Delete First")
        print("4. Delete Last")
        print("0. Keluar")
        Menu = int(input("Pilihan Anda : "))
        
if __name__ == '__main__':
    main()
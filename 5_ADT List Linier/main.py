# Cristianto Tri Arthurito
# 2172027

## Definisi Kelas Node
## Definisi Atribut
# value : atribut yang menyimpan nilai (integer)
# next : atribut reference elemen berikutnya (Node)
class MyListElement():
    ## Definisi Konstruktor
    # Kamus Lokal
    # value : var yang menyimpan nilai (integer)
    def __init__(self, value):
        self.info = value
        self.next = None
        return

## Definisi Kelas ListL
## Definisi Atribut
# first : atribut reference elemen pertama (Node)
class MyList():
    ## Definisi Konstruktor
    # Kamus Lokal
    def __init__(self):
        self.first = None
        return

    def InsertFirst(self, Q):
        Q.next = self.first
        self.first = Q
        return

    def traversal(self):
        temp = self.first
        while (temp.next != None):
            print(temp.info, end=" ")
            temp = temp.next
        print(temp.info, end=" ")

    ## Definisi Method removeLast()
    # Kamus Lokal
    # last : elemen terbuang dari list (Node)
    # prevlast : penyimpan reference elemen kedua terakhir (Node)
    def removeLast(self):
        if (self.first.next == None):
            last = self.first
            self.first = None
            a = last.info
        else:
            prevlast = None
            last = self.first
            while (last.next != None):
                prevlast = last
                last = last.next
            prevlast.next = None
            a = last.info
        return a

# Program Utama
def main():
    L = MyList()
    ij = int(input("N : "))
    MyListElement(ij)
    for i in range(0, ij):
        x = MyListElement(str(input("- ")))
        L.InsertFirst(x)
    print(" ")
    print("isi list : ")
    L.traversal()
    print(" ")
    print("kondisi list terbalik dari urutan masukan karena penambahan elemen menggunakan pola insert first")
    for i in range(0, ij):
        test = L.removeLast()
        print("kondisi penghapusan ", i+1, ":")
        if i+1 == ij:
            print("elemen ", test, " terhapus menyisakan kekosongan")
        else:
            print("elemen ", test, " terhapus menyisakan", end=" ")
            L.traversal()
            print(" ")
if __name__ == '__main__':
    main()
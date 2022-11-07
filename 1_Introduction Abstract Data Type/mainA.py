## Definisi Kelas ##
## Definisi Kelas Mahasiswa
## Definisi Atribut
# makan : atribut untuk menyimpan string makan (string)
# tidur : atribut untuk menyimpan string tidur (string)
# jalan : atribut untuk menyimpan string jalan (string)
# nugas : atribut untuk menyimpan string nugas (string)
# main : atribut untuk menyimpan string main (string)

class Mahasiswa:
## Definisi Method tampilkan()
# Kamus Lokal
    def makan1(self) :
        print("Kegiatan 1", self.makan)
        return
    
    def tidur2(self) :
        print("Kegiatan 2", self.tidur)
        return
    
    def jalan3(self) :
        print("Kegiatan 3", self.jalan)
        return
    
    def nugas4(self) :
        print("Kegiatan 4", self.nugas)
        return
    
    def main5(self) :
        print("Kegiatan 5", self.main)
        return
def main():
    arthur = Mahasiswa() # buat mahasiswa baru
    
    arthur.makan = 'Saya Sedang Makan'
    arthur.tidur = 'Saya Sedang tidur'
    arthur.jalan = 'Saya Sedang jalan'
    arthur.nugas = 'Saya Sedang nugas'
    arthur.main = 'Saya Sedang main'
    
    arthur.makan1()
    arthur.tidur2()
    arthur.jalan3()
    arthur.nugas4()
    arthur.main5()

    return
if __name__ == '__main__':
    main()
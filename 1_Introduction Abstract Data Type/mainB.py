## Definisi Kelas ##
## Definisi Kelas Mahasiswa
## Definisi Atribut
# Nama :  atribut untuk menyimpan nilai nama (String)
# Umur :  atribut untuk menyimpan nilai umur (integer)
# Tinggi Badan :  atribut untuk menyimpan nilai tinggi badan (integer)
# Berat Badan :  atribut untuk menyimpan Berat Badan (integer)
# BMI :  atribut untuk menyimpan BMi (integer)

class Mahasiswa:
## Definisi Method tampilkan()
# Kamus Lokal
    def tampilkan(self) :
        print("Nama        :",self.Nama)
        print("Umur        :",self.Umur)
        print("TinggiBadan :",self.TinggiBadan)
        print("BeratBadan  :",self.BeratBadan)
        return
    
## Definisi Method hitungbmi()
# Kamus Lokal
    def hitungbmi(self):
        return ( self.BeratBadan/(self.TinggiBadan/100*self.TinggiBadan/100))
    
    def indeksbmi(self):
        na = self.hitungbmi()
        if(na > 30):
            print("Obesitas Tingkat Tinggi 2")
        elif(na < 29.9 and na > 25):
            print("Obesitas Tingkat Tinggi 1")
        elif(na < 24.9 and na > 23):
            print("Kelebihan Berat Badan")
        elif(na > 18.5 and na < 22.9):
            print("Normal")
        elif(na < 18.5):
            print("Kurang Berat Badan")
        return
    
def main():
    arthur = Mahasiswa() # buat mahasiswa baru
    arthur.Nama = str(input("Masukkan Nama  : "))
    arthur.Umur = int(input("Masukkan Umur : "))
    arthur.TinggiBadan = int(input("Masukkan Tinggi Badan : "))
    arthur.BeratBadan = int(input("Masukkan Berat Badan : "))
    
    print("")
    arthur.tampilkan()
    print("BMI         :", arthur.hitungbmi())
    print("IMT         :"), arthur.indeksbmi()
    
    print("")
    cris = Mahasiswa()
    cris.TinggiBadan = int(input("Ubah Tinggi Badan : "))
    cris.BeratBadan = int(input("Ubah Berat Badan : "))
    print("BMI         :", cris.hitungbmi())
    print("IMT         :"), cris.indeksbmi()
    print("")
    
    return
if __name__ == '__main__':
    main()
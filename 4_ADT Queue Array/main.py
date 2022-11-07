# Cristianto Tri Arthurito
# 272027
# input1 : atribut untuk menyimpan nilai inputan (integer)
# Program ini pernah digunakan di praktikum sebelumnya

def main():
    S1 = ADTQueue.Queue(10)
    print("ADT QUEUE")
    print("0. Close Program")
    print("1. Insert")
    print("2. Delete")
    print("3. Cetak")
    print("---------------")
    input1 = int(input("Pil : "))
    while input1 != 0:
        if input1 == 1:
            X = int(input("Insert "))
            S1.insert(X)
            print("---------------")
            
        elif input1 == 2:
            S1.delete()
            print(S1.CetakQueue())
            print("---------------")

        elif input1 == 3:
            print(S1.CetakQueue())
            print("---------------")
        input1 = int(input("Pil : "))
    return
if __name__ == '__main__':
    import ADTQueue
    main()

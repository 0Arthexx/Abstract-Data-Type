# Cristianto Tri Arthurito
# 272027
# input1 : atribut untuk menyimpan nilai inputan (integer)

def main():
    S1 = ADTStack.stack(10)
    print("ADT STACK")
    print("0. Close Program")
    print("1. POP")
    print("2. PUSH")
    print("3. Cetak")
    print("---------------")
    input1 = int(input("Pil : "))
    while input1 != 0 :
        if input1 == 1:
            S1.pop()
            print(S1.CetakStack())
            print("---------------")

        elif input1 == 2:
            X = int(input("Push "))
            S1.push(X)
            print("---------------")

        elif input1 == 3:
            print(S1.CetakStack())
            print("---------------")
        input1 = int(input("Pil : "))
    return
if __name__ == '__main__':
    import ADTStack
    main()

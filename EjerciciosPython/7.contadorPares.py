def contarPares(arreglo):
    if arreglo!=[]:
        return len([num for num in arreglo if num%2==0])
    return 0

def main():
    l=[5,4,7,8]
    print(contarPares(l))

main()



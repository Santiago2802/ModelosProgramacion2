def cuadrados(arreglo):
    if arreglo!=[]:
        return [num*num for num in arreglo]
    return []

def main():
    l=[5,4,7,8]
    print(cuadrados(l))

main()



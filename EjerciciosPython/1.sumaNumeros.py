def sumar(arreglo):
    
    if arreglo != []: 
        return arreglo[0] + sumar(arreglo[1:])
    return 0

def main():
    l=[4,3,2,1]
    print(sumar(l))

main()



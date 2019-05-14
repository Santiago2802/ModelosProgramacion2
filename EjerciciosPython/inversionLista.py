def invertir(arreglo):
    
    if arreglo != []: 
        return invertir(arreglo[1:])+[arreglo[0]] 
    return []

def main():
    l=[4,3,2,1]
    print(invertir(l))

main()



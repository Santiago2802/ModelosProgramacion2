def determinarMayor(arreglo):
    
    if (all(x < arreglo[0] for x in arreglo[1:])): 
        return arreglo[0]
    return determinarMayor(arreglo[1:])

def main():
    l=[1,2,3,9,5,6,7]
    print(determinarMayor(l))

main()

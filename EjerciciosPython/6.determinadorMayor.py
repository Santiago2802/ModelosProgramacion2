def determinarMayor(arreglo):
    
    if (all(x < arreglo[0] for x in arreglo[1:])): 
        return arreglo[0]
    return determinarMayor(arreglo[1:])

def main():
    l=[78,24,56,93,21,237,46,74,125]
    print(determinarMayor(l))

main()

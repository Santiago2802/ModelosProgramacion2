def verificarOrden(arreglo):
    
    if arreglo != [] and len(arreglo)>1: 
        return (arreglo[0]<=arreglo[1]) and verificarOrden(arreglo[1:])
    return True

def main():
    l=['a','b','c','d']
    print(verificarOrden(l))

main()



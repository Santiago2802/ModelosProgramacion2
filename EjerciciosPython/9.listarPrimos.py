def esDivisible(dividendo,divisor):
    return dividendo%divisor==0
    
def listaDivisibles(lim):
    return [num for num in range(1,lim+1) if esDivisible(lim,num)]
    
def esPrimo(num):
    return len(listaDivisibles(num))<=2
    
def primos(lim):
    return [num for num in range(1,lim+1) if esPrimo(num)]
    
def main():
    print(primos(100))

main()



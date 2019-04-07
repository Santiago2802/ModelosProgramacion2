import numpy as np


def ordenarcaracol(arreglo):

    print(" ", end="")
    print(*arreglo[0], end="")

    if len(arreglo[1:, :]) is not 0:
        ordenarcaracol(np.rot90(arreglo[1:, :]))


def main():
    ordenarcaracol(np.genfromtxt('Matriz.txt', delimiter=' ').astype(int))


main()
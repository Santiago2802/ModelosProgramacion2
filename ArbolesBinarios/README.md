# Arboles Binarios :shipit:
## El uso de árboles es una herramienta útil en el manejo de información homogénea
### Uso de árboles binarios a través de código en Python
#### Estructura de un nodo
Para la determinación de un árbol binario realizaremos la estructuración de sus nodos:
```python
class nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha
```
* Árboles binarios solo podrán contar con dos elementos como máximo, en este caso son  izquierda y derecha.
* Sus enlaces por defecto serán nulos, lo único que siempre necesita es un valor.
#### Creación de un árbol binario
La creación de un árbol, basandonos en el código anterior, se verá claramente con el siguiente ejemplo:
```python
arbol = nodo(25, nodo(10, nodo(5), nodo(18)), nodo(40, None, nodo(50)))                                                        
```
Gráficamente el árbol es el siguiente:


<img src="https://user-images.githubusercontent.com/43209755/58387777-5e1bf780-7fda-11e9-8ff6-ae4898618c65.png" width="350">


Como se puede ver, hay diferencias claras entre la creación de nodos con y sin enlaces.


#### Búsqueda de elementos en un árbol binario
La función a definir la búsqueda de un nodo en el árbol binario tendrá como discriminante el valor dentro de él:
```python
def buscar(arbol, valor):
    #Condiciones de Rompimiento de la recursividad
    if arbol == None:
        return False	
    if arbol.valor == valor:
        return True
    if arbol.valor < valor:
         #Se dirige a la derecha del nodo si el valor es menor al nodo
	 return buscar(arbol.derecha, valor)
    #Se dirige a la izquierda si es mayor
    return buscar(arbol.izquierda, valor)
```
#### Suma de los valores del árbol
Una operación entre nodos nos ayudará a relacionarlos entre sí para ejemplificar el manejo de información que
podemos realizar con árboles binarios:
```python
def sumar(arbol):
    if arbol == None:
        return 0
    return sumar(arbol.izquierda)+arbol.valor+sumar(arbol.derecha)
```
El uso de la recursividad, podemos ver que se realiza desde la raíz hasta las hojas.
#### Listando los nodos del árbol
Los elementos del árbol, los podemos conocer a través de una lista con sus valores, para asi conocer toda la 
información que el árbol guarda.
```python
def a_lista(arbol):
    if arbol == None:
        return []
    return a_lista(arbol.izquierda)+[arbol.valor]+a_lista(arbol.derecha)
```
Nuevamente vemos el recorrido descendente que realiza la recursividad.
#### Agregando un nodo a la lista
Como vemos, el árbol se ordena de manera tal que, al agregar un nodo se debe colocar en orden numérico:
```python
def agregarNodo(arbol,valor):

    if arbol.valor == valor:
        return arbol
    #Si el valor que entra es menor, debe ingresar por izquierda
    if arbol.valor > valor:
        # Si no hay mas nodos donde realizar comparaciones, se coloca en base al nodo actual
        if(arbol.izquierda == None):
            return nodo(arbol.valor, nodo(valor), arbol.derecha)
        # Se sigue buscando el lugar del valor
        else:
            return nodo(arbol.valor, agregarNodo(arbol.izquierda, valor), arbol.derecha)
    #Si el valor que entra es mayor, debe ingresar por derecha
    if arbol.valor < valor:
        if(arbol.derecha == None):
            return nodo(arbol.valor, arbol.izquierda, nodo(valor))
        else:
            return nodo(arbol.valor, arbol.izquierda, agregarNodo(arbol.derecha, valor))
```
Si analizamos esta recursividad veremos los siguiente:
* El retorno se hace siempre usando la creación de nodos.
* El criterio de rompimiento se realiza a partir de los enlaces del nodo:
  * Si el valor a introducir es menor que el del nodo, se verifica si su enlace izquierdo esta
    vacío, al cumplir el criterio de rompimiento, se sabe que está vacío, entonces introduce
    el nuevo nodo con el valor a introducir en su enlace izquierdo, asimismo conserva tanto
    su valor como su enlace derecho
  * Si el valor a introducir es mayor que el del nodo, se verifica si su enlace derecho esta 
    vacío, igualmente al cumplir el criterio de rompimiento, está vacío, introduce el nodo 
    con el valor a introducir en su enlace derecho, también conservando su valor y enlace derecho
* Cada retorno en donde se  realiza la recursividad, tiene presente al nodo usando la misma creación
  de un nodo, puesto que en sus parametros hacemos referencia a su valor y enlaces, por lo tanto,
  sabremos que no perdemos ni valores ni enlaces del árbol en nuestros llamados recursivos. 
#### Creando árboles binarios a través de listas
Para crear un árbol binario a través de una función cuyo único parámetro sea una lista, usaremos la 
función realizada anteriormente, ya que es idónea para esta situacion.
El uso de dos funciones se hace necesario debido a los dos criterios a manejar:
1. La agregación continua de nodos al árbol.
2. El paso de valores de la lista para crear el árbol nodo a nodo.
```python	
#Agrega los nodos en la creación del árbol
def agregarElemento(arbol, valor):
    if arbol == None:
        return nodo(valor)
    return agregarNodo(arbol, valor)


#Pasa los valores a la agregación de nodos
def a_arbol(lista):
    if lista == []:
        return None
    return agregarElemento(a_arbol(lista[:-1]),lista[-1])
```
Para la primer función, veremos que no usa recursividad, sin embargo es el apoyo que la siguiente
función necesita para discriminar la raíz del árbol del resto del árbol.
Al analizar la segunda función, veremos que:
* La raíz del árbol será el primer valor, puesto que el criterio de rompimiento es una lista vacía,
  evento que solo se da en el llamado en caso de  una lista de un elemento,el cual es ese valor.
* El None que se retorna, será ese discriminante que necesitamos para indicar que el primer valor
  es la raíz del árbol a crear.

 
Finalmente veremos en la función main() unas pruebas para probar cada función y comprobar lo dicho anteriormente.

#### Gabriel Esteban Castillo Ramirez
#### Omar Alejandro Espitia Sanchez
#### Juan Camilo Martinez Lopez



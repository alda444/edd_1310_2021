class NodoArbol:
    def __init__(self, value, left = None, right = None):
        self.data = value
        self.left = left
        self.right = right

arbol1 = NodoArbol("+",NodoArbol("-",NodoArbol(5),NodoArbol(4)),NodoArbol("*",NodoArbol(3),NodoArbol(2)))

print("Este es el 1er Arbol:")
print(arbol1.data)
print(arbol1.left.data)
print(arbol1.left.left.data)
print(arbol1.left.right.data)
print(arbol1.right.data)
print(arbol1.right.left.data)
print(arbol1.right.right.data)
print(f"El recorrido de forma Infija es: (comenzando por la izquierda, después por la raíz y por último por  la derecha) es: {arbol1.left.left.data}, {arbol1.left.data}, {arbol1.left.right.data}, {arbol1.data}, {arbol1.right.left.data}, {arbol1.right.data}, {arbol1.right.right.data}")
print(f"El recorrido de forma Prefija es: (comenzando por la raíz, después por la izquierda y por último la derecha) es: {arbol1.data}, {arbol1.left.data}, {arbol1.left.left.data}, {arbol1.left.right.data}, {arbol1.right.data}, {arbol1.right.left.data}, {arbol1.right.right.data}")
print(f"El recorrido de forma Posfija es: (comenzando por la izquierda, después por la derecha y por último la raíz) es: {arbol1.left.left.data}, {arbol1.left.right.data}, {arbol1.left.data}, {arbol1.right.left.data}, {arbol1.right.right.data}, {arbol1.right.data}, {arbol1.data}")
print("************************************************************************************************************************************")

arbol2 = NodoArbol(40,NodoArbol(30,NodoArbol(25),NodoArbol(35)),NodoArbol(50,NodoArbol(45),NodoArbol(60)))

print("Este es el 2do Arbol:")
print(arbol2.data)
print(arbol2.left.data)
print(arbol2.left.left.data)
print(arbol2.left.right.data)
print(arbol2.right.data)
print(arbol2.right.left.data)
print(arbol2.right.right.data)
print(f"El recorrido de forma Infija es: (comenzando por la izquierda, después por la raíz y por último la por derecha) es: {arbol2.left.left.data}, {arbol2.left.data}, {arbol2.left.right.data}, {arbol2.data}, {arbol2.right.left.data}, {arbol2.right.data}, {arbol2.right.right.data}")
print(f"El recorrido de forma prefija es: (comenzando por la raíz, después por la izquierda y por último por la derecha) es: {arbol2.data}, {arbol2.left.data}, {arbol2.left.left.data}, {arbol2.left.right.data}, {arbol2.right.data}, {arbol2.right.left.data}, {arbol2.right.right.data}")
print(f"El recorrido de forma posfija es: (comenzando por la izquierda, después por la derecha y por último la raíz) es: {arbol2.left.left.data}, {arbol2.left.right.data}, {arbol2.left.data}, {arbol2.right.left.data}, {arbol2.right.right.data}, {arbol2.right.data}, {arbol2.data}")

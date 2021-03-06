class NodoArbol:
    def __init__ (self, value , left=None , right=None):
        self.data=value
        self.left=left
        self.right=right

class BinarySearchTree:
    def __init__(self):
        self.__root=None

    def insert(self, value ):
        # Regla 1
        if self.__root == None:
            self.__root = NodoArbol(value)

        else:
            self.__insert__(self.__root,value)

    def __insert__(self,nodo,value):
        if nodo.data==value:
            print("el dato ya existe no se ingresa nada")

        elif value < nodo.data:
            # regla 1
            if nodo.left == None:
                nodo.left= NodoArbol(value)
            else:
                self.__insert__(nodo.left ,value)

            #regla 2

        else:
            if nodo.right == None:
                nodo.right= NodoArbol(value)
            else:
                self.__insert__(nodo.right ,value)

    def __recorrido_in(self,nodo):
        if nodo != None:
            self.__recorrido_in(nodo.left)
            print(nodo.data, end=",")
            self.__recorrido_in(nodo.right)

    def __recorrido_pre(self,nodo):
        if nodo != None:
            print(nodo.data, end=",")
            self.__recorrido_pre(nodo.left)
            self.__recorrido_pre(nodo.right)

    def __recorrido_pos(self,nodo):
        if nodo != None:
            self.__recorrido_pos(nodo.left)
            self.__recorrido_pos(nodo.right)
            print(nodo.data, end=",")


    def tranversal(self,format="inorden"):
        if format == "inorden":
            print("inorden")
            self.__recorrido_in(self.__root)

        elif format == "preorden":
            print("preorden")
            self.__recorrido_pre(self.__root)

        elif format == "posorden":
            print("posorden")
            self.__recorrido_pos(self.__root)

        else:
            print("Error , ese reorrido no exite ")
        print()

    def search(self,value):
        if self.__root == None:
            return None
        else:
            return self.__search(self.__root, value)


    def __search(self, nodo, value):
        if nodo == None: #esta vacio
            return None

        elif nodo.data == value: # caso base de recursividad
            print("encontrado")
            return nodo
        elif value < nodo.data:
            print("buscar a la izquierda")
            return self.__search(nodo.left,value)
        else:
            print("buscar a la derecha")
            return self.__search(nodo.right,value)

    def remove(self, value):
        if self.__root == None:
            print("nada que eliminar")
        else:
            self.__remove(None, None, self.__root, value )

    def __remove(self, padre_hi , padre_hd , actual , value):
        if actual == None:
            print("caso base")
            return None
        elif actual.data == value: #caso base
            print("enconrtrado:", actual.data)
            #caso 1 (hoja)
            if actual.left == None and actual.right == None:
                if padre_hi != None:
                    padre_hi.left = None
                else:
                    padre_hd.right = None
            #caso 2 (con un hijo)
            if (actual.left != None and actual.right ==None) or (actual.left == None and actual.right !=None):
                print("es una nodo con un hijo" , actual.data)
                if actual.left != None:
                    actual.data = actual.left.data
                    actual.left = None
                else:
                    actual.data = actual.right.data
                    actual.right = None

            #caso 3 (con los 2 hijos)


            #return actual

        elif value < actual.data:
            print("buscar a la izquierda")
            self.__remove(actual, None, actual.left , value)
        else:
            print("buscar a la derecha")
            self.__remove(None, actual, actual.right , value)

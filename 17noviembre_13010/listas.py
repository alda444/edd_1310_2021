class Nodo:
    def __init__(self,value, siguiente= None):
        self.data = value               #falta encapsulamiento
        self.siguiente = siguiente

class LinkedList:
   def __init__(self):
       self.__head= None

    def is_empty(self):
        retun self.__head == None

    def append ( self , value):
    nuevo = Nodo (value)
     if self.__head == None:                #self.is_empty()
       self.__head = nuevo
    else:
        curr_node = self.__head
      while curr_node.siguiente  != None:
        curr_node = curr_node.siguiente
      curr_node.siguiente = nuevo
      def transversal (self):
          curr_node != None:
          print (f" {curr_node.data} -> ", end="")
          curr_node = curr_node.siguiente
      print=("")

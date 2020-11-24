from listas from DoubleLinkedList

ld = DoubleLinkedList()
print ("Esta vacia?: " , ld.is_empty () )
ld.append(10)
ld.append(20)
ld.append(30)
print(f"La lista tiene { ld.get_size()}elementos")
ld.transversal()
ld.reverse_trasnversal()
ld.remove_from_head(20)
ld.reverse_transversal()

from Modelos.ArbolBST import ArbolBST




# Ejemplo de uso
arbol = ArbolBST()
arbol.insertar(20)
arbol.insertar(15)
arbol.insertar(33)
arbol.insertar(10)
arbol.insertar(18)
arbol.insertar(25)
arbol.insertar(50)
arbol.insertar(5)
arbol.insertar(12)
arbol.insertar(17)
arbol.insertar(19)
arbol.insertar(21)
arbol.insertar(27)
arbol.insertar(40)
arbol.insertar(70)
arbol.insertar(1)




#print(arbol.buscar(5))  # Output: True
#print(arbol.buscar(7))  # Output: False

arbol.postorden()
#arbol.imprimir_arbol()



# Dibujar el árbol
arbol.dibujar()
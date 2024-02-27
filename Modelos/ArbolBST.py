from Modelos.Nodo import Nodo
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc

class ArbolBST:
    def __init__(self):
        self.raiz = None

    #################################### Inserción #################################################
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self.insertar_recursivo(self.raiz, valor)

    def insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self.insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self.insertar_recursivo(nodo.derecha, valor)
        else:
            # Valor ya existe en el árbol, podemos manejarlo como quieras
            pass

    #################################### Búsqueda #################################################
    def buscar(self, valor):
        return self.buscar_recursivo(self.raiz, valor)

    def buscar_recursivo(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo is not None
        if valor < nodo.valor:
            return self.buscar_recursivo(nodo.izquierda, valor)
        else:
            return self.buscar_recursivo(nodo.derecha, valor)
    #################################### Recorridos #################################################
    def preorden(self):
        return self._preorden_recursivo(self.raiz)

    def _preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.valor, end=" ")
            self._preorden_recursivo(nodo.izquierda)
            self._preorden_recursivo(nodo.derecha)

    def inorden(self):
        return self._inorden_recursivo(self.raiz)

    def _inorden_recursivo(self, nodo):
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierda)
            print(nodo.valor, end=" ")
            self._inorden_recursivo(nodo.derecha)

    def postorden(self):
        return self._postorden_recursivo(self.raiz)

    def _postorden_recursivo(self, nodo):
        if nodo is not None:
            self._postorden_recursivo(nodo.izquierda)
            self._postorden_recursivo(nodo.derecha)
            print(nodo.valor, end=" ")
############################## Eliminación ##################################

    def eliminar(self, valor):
        self.raiz = self.eliminar_recursivo(self.raiz, valor)

    def eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo

        # Si el valor a eliminar es menor que el valor del nodo actual,
        # entonces se encuentra en el subárbol izquierdo
        if valor < nodo.valor:
            nodo.izquierda = self.eliminar_recursivo(nodo.izquierda, valor)
        # Si el valor a eliminar es mayor que el valor del nodo actual,
        # entonces se encuentra en el subárbol derecho
        elif valor > nodo.valor:
            nodo.derecha = self.eliminar_recursivo(nodo.derecha, valor)
        # Si el valor a eliminar es igual al valor del nodo actual, entonces este es el nodo a eliminar
        else:
            # Caso 1: Nodo sin hijos o con un solo hijo
            if nodo.izquierda is None:
                temp = nodo.derecha
                nodo = None
                return temp
            elif nodo.derecha is None:
                temp = nodo.izquierda
                nodo = None
                return temp

            # Caso 2: Nodo con dos hijos
            # Obtener el sucesor inmediato (el menor valor en el subárbol derecho)
            temp = self.obtener_sucesor(nodo.derecha)
            # Copiar el valor del sucesor al nodo actual
            nodo.valor = temp.valor
            # Eliminar el sucesor
            nodo.derecha = self.eliminar_recursivo(nodo.derecha, temp.valor)

        return nodo

    def obtener_sucesor(self, nodo):
        # Este método devuelve el nodo con el valor más pequeño en un árbol dado (subárbol derecho)
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo
    ############### Imprimir ######################
    def dibujar_arbol(self,nodo, x, y, espaciado, ax):
        if nodo is None:
            return

        radio = 0.2  # Tamaño del círculo

        if nodo.izquierda:
            ax.plot([x, x - espaciado], [y, y - 1], '-k')
            self.dibujar_arbol(nodo.izquierda, x - espaciado, y - 1, espaciado / 2, ax)
        if nodo.derecha:
            ax.plot([x, x + espaciado], [y, y - 1], '-k')
            self.dibujar_arbol(nodo.derecha, x + espaciado, y - 1, espaciado / 2, ax)

        nodo_circle = Circle((x, y), radius=radio, fill=True, color='lightblue',
                             zorder=2)  # Usamos zorder para asegurar que los círculos estén sobre las líneas
        ax.add_patch(nodo_circle)
        ax.text(x, y, str(nodo.valor), ha='center', va='center', color='black')

    def dibujar(self):
        fig, ax = plt.subplots()
        self.dibujar_arbol(self.raiz, 0, 0, 4, ax)  # Modificar el último parámetro para ajustar el espaciado horizontal
        ax.set_aspect('equal')
        ax.axis('off')
        figManager = plt.get_current_fig_manager()
        figManager.window.state('zoomed')
        plt.show()
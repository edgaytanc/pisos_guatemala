from .nodo import Nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_final(self, color):
        nuevo_nodo = Nodo(color)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        ultimo = self.cabeza
        while ultimo.siguiente:
            ultimo = ultimo.siguiente
        ultimo.siguiente = nuevo_nodo

    def __iter__(self):
        self.actual = self.cabeza
        return self
    
    def __next__(self):
        if self.actual:
            color = self.actual.color
            self.actual = self.actual.siguiente
            return color
        else:
            raise StopIteration

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.color, end="")
            actual = actual.siguiente
        print()

    def __len__(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador
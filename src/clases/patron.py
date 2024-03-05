from .lista_enlazada import ListaEnlazada
from graphviz import Digraph

class Patron:
    def __init__(self, codigo, secuencia):
        self.codigo = codigo
        self.secuencia = ListaEnlazada()
        for color in secuencia:
            self.secuencia.insertar_final(color)


    def generar_grafico(self, filas, columnas):
        dot = Digraph(engine='neato', format='png')  # 'neato' permite posicionar nodos con coordenadas
        dot.attr('node', shape='square', width='0.6', height='0.6', style='filled', fixedsize='true')
        
        actual = self.secuencia.cabeza
        for i in range(filas):
            for j in range(columnas):
                if actual is None:
                    break  # No hay más colores en la secuencia
                color = 'white' if actual.color == 'B' else 'black'
                dot.node(f'{i}_{j}',label='', fillcolor=color, pos=f'{j * 0.6},{-i * 0.6}!')
                actual = actual.siguiente


        dot.render(f'patron_{self.codigo}', view=True)
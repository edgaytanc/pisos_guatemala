from .patron import Patron

class Piso:
    def __init__(self, nombre,R,C,F,S):
        self.nombre = nombre
        self.R = R
        self.C = C
        self.F = F # costo de volteo
        self.S = S # costo de intercambio
        self.patrones = []

    def agregar_patron(self, codigo, secuencia):
        self.patrones.append(Patron(codigo, secuencia))
    
    def mostrar_patron(self,secuencia):
        for patron in self.patrones:
            patron.generar_grafico_patron(secuencia)

    

    def calcular_costo_minimo(self, patron_original, patron_nuevo, R, C, F, S):
        print(f"Longitud esperada de R: {R}")
        print(f"Longitud esperada de C: {C}")
        print(f"Longitud de patron_original: {len(patron_original)}")
        print(f"Longitud de patron_nuevo: {len(patron_nuevo)}")
        costo_volteo = 0
        costo_intercambio = 0

        # Asegurarse que la lista esté en el formato correcto
        if len(patron_original) != R or len(patron_nuevo) != R:
            raise ValueError("Dimensiones de R incorrectas para los patrones proporcionados.")

        # Convertir las listas de cadenas a listas de listas para facilitar la manipulación
        patron_original_matriz = [list(fila) for fila in patron_original]
        patron_nuevo_matriz = [list(fila) for fila in patron_nuevo]

        for i in range(R):
            if len(patron_original[i]) != C or len(patron_nuevo[i]) != C:
                raise ValueError("Dimensiones de C incorrectas para los patrones proporcionados.")
            
            for j in range(C):
                if patron_original_matriz[i][j] != patron_nuevo_matriz[i][j]:
                    # Verificar posibilidad de intercambio
                    if j+1 < C and patron_original_matriz[i][j+1] == patron_nuevo_matriz[i][j] and patron_original_matriz[i][j] == patron_nuevo_matriz[i][j+1]:
                        # Realizar intercambio
                        patron_original_matriz[i][j], patron_original_matriz[i][j+1] = patron_original_matriz[i][j+1], patron_original_matriz[i][j]
                        costo_intercambio += S
                    else:
                        # Realizar volteo
                        costo_volteo += F

        costo_total = costo_volteo + costo_intercambio
        return costo_total

    
    def generar_instrucciones(self, patron_original, patron_nuevo, R, C, F, S):
        instrucciones = []

        # Convertir las cadenas a listas de caracteres para permitir la modificación
        patron_original_mod = [list(fila) for fila in patron_original]
        patron_nuevo_mod = [list(fila) for fila in patron_nuevo]

        for i in range(R):
            for j in range(C):
                if patron_original_mod[i][j] != patron_nuevo_mod[i][j]:
                    # Buscar si un intercambio es posible
                    if j+1 < C and patron_original_mod[i][j+1] == patron_nuevo_mod[i][j] and patron_original_mod[i][j] == patron_nuevo_mod[i][j+1]:
                        instrucciones.append(f"Intercambiar ({i}, {j}) con ({i}, {j+1})")
                        # Realizar el intercambio
                        patron_original_mod[i][j], patron_original_mod[i][j+1] = patron_original_mod[i][j+1], patron_original_mod[i][j]
                    elif i+1 < R and patron_original_mod[i+1][j] == patron_nuevo_mod[i][j] and patron_original_mod[i][j] == patron_nuevo_mod[i+1][j]:
                        instrucciones.append(f"Intercambiar ({i}, {j}) con ({i+1}, {j})")
                        # Realizar el intercambio
                        patron_original_mod[i][j], patron_original_mod[i+1][j] = patron_original_mod[i+1][j], patron_original_mod[i][j]
                    else:
                        instrucciones.append(f"Voltear ({i}, {j})")
                        # Realizar el volteo
                        patron_original_mod[i][j] = 'B' if patron_original_mod[i][j] == 'N' else 'N'

        # Convertir las listas de caracteres modificadas de vuelta a cadenas
        patron_modificado = [''.join(fila) for fila in patron_original_mod]

        return instrucciones, patron_modificado

    

    def ordenar_patrones(self):
        self.patrones = sorted(self.patrones, key=lambda patron: patron.codigo)

# La función generar_instrucciones se podría ubicar en un módulo separado de lógica de negocios o como un método en la clase Piso o Patron.

from clases.xml_data_manager import XMLDataManager
from clases.lista_enlazada import ListaEnlazada
from clases.patron import Patron
from clases.piso import Piso


archivo_xml = "d:\\Users\\David\\Desktop\\workspace\\python\\POO\\proyecto\\src\\clases\\entrada.xml"
gestor_datos = XMLDataManager(archivo_xml)


# piso_seleccionado = gestor_datos.pisos[0]
# patron_seleccionado = piso_seleccionado.patrones[0]

# filas = piso_seleccionado.R
# columanas = piso_seleccionado.C

# patron_seleccionado.generar_grafico(filas, columanas)

def seleccionar_piso_y_patron(gestor_datos):
    # Mostrar lista de pisos
    print("Pisos disponibles:")
    for idx, piso in enumerate(gestor_datos.pisos, start=1):
        print(f"{idx}. {piso.nombre}")
    
    # Seleccionar piso
    seleccion_piso = int(input("Seleccione un piso por número: ")) - 1
    piso_seleccionado = gestor_datos.pisos[seleccion_piso]
    
    # Mostrar patrones disponibles para el piso seleccionado
    print(f"Patrones disponibles para el piso '{piso_seleccionado.nombre}':")
    for idx, patron in enumerate(piso_seleccionado.patrones, start=1):
        print(f"{idx}. Código de patrón: {patron.codigo}")
    
    # Seleccionar patrón
    seleccion_patron = int(input("Seleccione un patrón por número: ")) - 1
    patron_seleccionado = piso_seleccionado.patrones[seleccion_patron]
    
    # Llamar al método de visualización para el patrón seleccionado
    # Asegúrate de que la función generar_grafico() esté correctamente definida en tu clase Patron
    print(f"Mostrando patrón '{patron_seleccionado.codigo}' del piso '{piso_seleccionado.nombre}':")
    patron_seleccionado.generar_grafico(piso_seleccionado.R, piso_seleccionado.C)


def secuencia_a_lista(secuencia, R, C):
    lista = []
    actual = secuencia.cabeza
    contador = 0
    fila_temporal = []
    
    while actual:
        fila_temporal.append(actual.color)
        contador += 1
        if contador % C == 0:
            lista.append(fila_temporal)
            fila_temporal = []
        actual = actual.siguiente
    
    if contador != R * C:
        raise ValueError("La longitud de la secuencia no coincide con las dimensiones RxC proporcionadas.")
    return lista

def convertir_cadenas_a_lista_enlazada(lista_cadenas):
    lista_enlazada = ListaEnlazada()
    for cadena in lista_cadenas:
        for caracter in cadena:
            lista_enlazada.insertar_final(caracter)
    return lista_enlazada



def calcular_costo_minimo_para_piso(gestor_datos):
    print("Seleccione un piso para calcular el costo mínimo para cambiar de patrón:")
    for idx, piso in enumerate(gestor_datos.pisos, start=1):
        print(f"{idx}. {piso.nombre}")
    
    indice_piso = int(input("Seleccione un piso por número: ")) - 1
    piso_seleccionado = gestor_datos.pisos[indice_piso]

    print("Seleccione el patrón original:")
    for idx, patron in enumerate(piso_seleccionado.patrones, start=1):
        print(f"{idx}. Código de patrón: {patron.codigo}")
    
    indice_patron_original = int(input("Seleccione el patrón original por número: ")) - 1
    patron_original = piso_seleccionado.patrones[indice_patron_original]

    print("Seleccione el patrón nuevo:")
    indice_patron_nuevo = int(input("Seleccione el patrón nuevo por número: ")) - 1
    patron_nuevo = piso_seleccionado.patrones[indice_patron_nuevo]

    # Convertir secuencias a listas
    lista_patron_original = secuencia_a_lista(patron_original.secuencia, piso_seleccionado.R,piso_seleccionado.C)
    lista_patron_nuevo = secuencia_a_lista(patron_nuevo.secuencia, piso_seleccionado.R,piso_seleccionado.C)

    # Calcular el costo mínimo
    costo = piso_seleccionado.calcular_costo_minimo(
        lista_patron_original, 
        lista_patron_nuevo, 
        piso_seleccionado.R, 
        piso_seleccionado.C, 
        piso_seleccionado.F, 
        piso_seleccionado.S
    )
    
    print(f"\nEl costo mínimo para cambiar del patrón original al nuevo patrón es: {costo} Quetzales.\n")

def ejecutar_cambio_de_patron(gestor_datos):
    # Mostrar lista de pisos
    print("\nSeleccione un piso:")
    for idx, piso in enumerate(gestor_datos.pisos, start=1):
        print(f"{idx}. {piso.nombre}")
    
    # Seleccionar piso
    indice_piso = int(input("Número del piso seleccionado: ")) - 1
    piso_seleccionado = gestor_datos.pisos[indice_piso]
    
    # Mostrar patrones disponibles para el piso seleccionado
    print("\nSeleccione el patrón original:")
    for idx, patron in enumerate(piso_seleccionado.patrones, start=1):
        print(f"{idx}. Código de patrón: {patron.codigo}")
    
    indice_patron_original = int(input("Número del patrón original seleccionado: ")) - 1
    patron_original = piso_seleccionado.patrones[indice_patron_original]

    print("\nSeleccione el patrón nuevo:")
    indice_patron_nuevo = int(input("Número del patrón nuevo seleccionado: ")) - 1
    patron_nuevo = piso_seleccionado.patrones[indice_patron_nuevo]

    # Convertir las secuencias a listas para la comparación
    lista_patron_original = secuencia_a_lista(patron_original.secuencia, piso_seleccionado.R, piso_seleccionado.C)
    lista_patron_nuevo = secuencia_a_lista(patron_nuevo.secuencia, piso_seleccionado.R, piso_seleccionado.C)

    # Generar instrucciones y obtener el patrón modificado
    instrucciones, patron_modificado = piso_seleccionado.generar_instrucciones(
        lista_patron_original, lista_patron_nuevo, piso_seleccionado.R, piso_seleccionado.C, piso_seleccionado.F, piso_seleccionado.S)

    # Prepara y visualiza patron modificado
    secuencia_lista_enlazada = convertir_cadenas_a_lista_enlazada(patron_modificado)
    patron_visualizado = Patron("Patron_Modificado", secuencia_lista_enlazada)
    patron_visualizado.generar_grafico(piso_seleccionado.R,piso_seleccionado.C)

    # preguntar al usuario como desea proceder con las instrucciones
    opcion_instrucciones = input("\n¿Desea guardar las instrucciones en un archivo? (sí/no): ").strip().lower()

    if opcion_instrucciones == 'sí' or opcion_instrucciones == 'si':
        # Crea y escribe las instrucciones en un archivo
        with open('instrucciones.txt', 'w') as archivo:
            for instruccion in instrucciones:
                archivo.write(instruccion + '\n')
            print("Las instrucciones se ha guardado en 'instrucciones.txt'.")
    else:
        # Mostrar instrucciones en pantalla
        print("\nInstrucciones para cambiar de patrón:")
        for instruccion in instrucciones:
            print(instruccion)




def mostrar_menu():
    print("\nBienvenido al sistema de gestión de patrones de Pisos de Guatemala, S.A.\n".upper())
    print("1. Cargar datos del archivo XML")
    print("2. Mostrar todos los pisos y patrones disponibles")
    print("3. Seleccionar un piso y patrón específico para visualización")
    print("4. Calcular el costo mínimo para cambiar a un nuevo patrón")
    print("5. Generar y mostrar gráficamente un nuevo patrón")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            gestor_datos.cargar_datos()
            gestor_datos.ordenar_pisos_y_patrones()
            print("\nDatos cargados en sistema correctamente!!!\n")
        elif opcion == '2':
            gestor_datos.mostrar_datos()
        elif opcion == '3':
            seleccionar_piso_y_patron(gestor_datos)
            
        elif opcion == '4':
            calcular_costo_minimo_para_piso(gestor_datos)
        elif opcion == '5':
            ejecutar_cambio_de_patron(gestor_datos)
        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()

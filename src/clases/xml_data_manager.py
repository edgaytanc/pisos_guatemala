import xml.etree.cElementTree as ET
from .piso import Piso

import os

class XMLDataManager:
    def __init__(self, archivo_xml):
        self.archivo_xml = archivo_xml
        self.pisos = [] 

    def cargar_datos(self):
        arbol = ET.parse(self.archivo_xml)
        raiz = arbol.getroot()

        for piso_xml in raiz.findall('piso'):
            nombre = piso_xml.get('nombre')
            R = int(piso_xml.find('R').text)
            C = int(piso_xml.find('C').text)
            F = int(piso_xml.find('F').text)
            S = int(piso_xml.find('S').text)

            piso = Piso(nombre, R,C,F,S)

            for patron_xml in piso_xml.find('patrones').findall('patron'):
                codigo = patron_xml.get('codigo')
                secuencia = patron_xml.text.replace("\n","").replace(" ","")
                piso.agregar_patron(codigo,secuencia)
            
            self.pisos.append(piso)

    def mostrar_datos(self):
        print("\nPisos y patrones disponibles\n".upper())
        for piso in self.pisos:
            print(f"Piso: {piso.nombre}, Dimensiones: {piso.R}x{piso.C}, Costos: F={piso.F}, S={piso.S}")
            for patron in piso.patrones:
                print(f"    Patron: {patron.codigo}, Secuencia: ", end="")
                patron.secuencia.mostrar()
                

    def ordenar_pisos_y_patrones(self):
        # Ordenar pisos por nombre
        self.pisos = sorted(self.pisos, key=lambda piso: piso.nombre)

        # Ordenar patrones dentro de cad paiso por codigo
        for piso in self.pisos:
            piso.ordenar_patrones()
    
    def ejecutar(self):
        self.cargar_datos()
        self.mostrar_datos()

    
# Punto de entrada del programa
if __name__ == "__main__":
    archivo_xml = "d:\\Users\\David\\Desktop\\workspace\\python\\POO\\proyecto\\src\\clases\\entrada.xml"
    gestor_datos = XMLDataManager(archivo_xml)
    gestor_datos.ejecutar()
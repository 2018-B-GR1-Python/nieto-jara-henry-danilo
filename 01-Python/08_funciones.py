

def imprimir_nombre(*infinito, defecto=1, normal, posicional,**kwargs): ##key word arguments
    print("{kwargs['primer_nombre']} {kwargs['segundo_nombre']} "
          "{kwargs['apellido_paterno'[} {kwargs['apellido_materno']}")

imprimir_nombre(1,2,3,4,5,6,7,8,defecto =2, normal=1, posicional = 3,primer_nombre = "Henry",
                segundo_nombre = "Danilo",
                apellido_paterno = "Nieto",
                apellido_materno = "Jara")

#numero = input("Ingrese un numero: ")
#print(float(numero) + 12.2 +1)

#opcional = input("Desea papas con su orden, Opc:Si o Opc:No")

#if(True if opcional == "Si" else False):
#    print("Truthy")
#else:
#    print("Falsy")

#numeros = input("Ingrese numeros: ")
#proceso
#recibir numeros separadospor comas y usar un split
#1) Recibir numeros -> Validar que sean numeros y q esten separados por comas
#   1.1) separar por comas
#   1.2) sean numeros
#2) Convertir los elementos de la tupla en Float
#3) Ejecutar la funcion!!
#x= input("Ingrese los numeros separados por comas: ")
#x.split(",")
#print(x)
#sumar_numeros(0, valor_inicial = 0)

def calculadora(numero_uno, numero_dos, operacion="suma"):
    def sumar_dos_numeros():
        return numero_uno + numero_dos

    def restar_dos_numeros():
        return numero_uno - numero_dos

    def multiplicar_dos_nuumero():
        return numero_uno * numero_dos

    def dividir_dos_numeros():
        return numero_uno / numero_dos

    def switch_operaciones():
        return {
            'sumar': sumar_dos_numeros(),
            'restar': restar_dos_numeros(),
            'multiplicar': multiplicar_dos_nuumero(),
            'dividir': dividir_dos_numeros()
        }[operacion]
    return switch_operaciones()


print(calculadora(1,2, 'sumar'))
print(calculadora(9,7, 'restar'))
print(calculadora(4,2, 'multiplicar'))
print(calculadora(9,3, 'dividir'))

# proyecto: Crear Borrar Actualizar
#CITAS MEDICAS

def leer_archivos(path):
    try:
        archivo_abierto = open(path) #defecto 'r' q es read
        arreglo_lineas_archivo = archivo_abierto.readlines()
        for linea in arreglo_lineas_archivo:
            print(linea)
        archivo_abierto.close()

     except Exception:
        print('No se pudo leer el archivo')

def agregar_a_archivos(path,*lineas_a_escribir):
    try:
        archivo_abierto = open(path,'a') #'a' añade nueva linea

        for linea in lineas_a_escribir:
            archivo_abierto.write(linea)

        archivo_abierto.close()   

     except Exception:
        print('No se pudo leer el archivo')

leer_archivos('./08_ejemplos.txt')
agregar_a_archivos('./08_ejemplos.txt',"hola, esta", "es una", "prueba")


class Escuela:

    __ciudad = 'Quito'
    pais = 'Ecuador'
    def __init__(self,nombre, valor_categoria = 4):
        print(self)
        print('Hola constructor')
        self.nombre = nombre
        self.valor_categoria = valor_categoria
    def saludar(self):
        print('Hola desde Escuela '+self.nombre +' localizada en '+ self.ciudad +' '+ self.pais)
    def categoria(self):
        return self.valor_categoria * 3

    def __str__(self):
        return 'Escuela'

#twa = Escuela('La salle')
#print(twa)
#twa.saludar()
#print(twa.categoria())

class Auto:
    _ensamblado = 'Quito'
    numero_asientos = 5
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def cambiar_ensamblado(self,ensamblado):
        self.__ensamblado = ensamblado

    def __maximo_numero_pasajeros(self,ensamblado):
        return self.numero_asientos + 3

    def __str__(self):
        return (self.nombre + ' ' + self.color + ' ' + self.numero_asientos.str() +' ' + self.__ensamblado +' ' +\
               self.__maximo_numero_pasajeros().str()).str()

bm = Auto('Balnco', 'Version 1')

print(bm)
class Hyundai(Auto):
    def __init__(self, color, nombre):
        super().__init__(color=color, nombre = nombre)
        print('constructor')
        print(self._ensamblado)

    #def __intit__(self):


mi_carro = Hyundai('Negro','Santa fe')
print(mi_carro)

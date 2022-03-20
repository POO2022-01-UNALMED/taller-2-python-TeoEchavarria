from turtle import color


class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        coloresPermitidos = ['rojo', 'verde', 'amarillo', 'negro', 'blanco']
        if color in coloresPermitidos:
            self.color = color

class Motor:
    def __init__(self, numerosCilindros, tipo, registro):
        self.numerosCilindros = numerosCilindros
        self.tipo = tipo
        self.registro = registro
        
    def cambiarRegistro(self, regitro):
        self.registro = regitro
    
    def asignarTipo(self, tipo):
        tiposPermitidos = ['electrico', 'gasolina']
        if tipo in tiposPermitidos:
            self.tipo = tipo

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = Motor
        self.registro = registro

    def cantidadAsientos(self):
        return sum(1 for i in self.asientos if type(i) == Asiento)
    
    def verificarIntegridad(self):
        if self.registro == self.motor.registro and sum([1 for i in self.asientos if i.registro == self.registro] == len(self.asientos)):
            return 'Auto original'
        else:
            return 'Las piezas no son originales'
    

if __name__ == '__main__':
    pass
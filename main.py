class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        coloresPermitidos = ['rojo', 'verde', 'amarillo', 'negro', 'blanco']
        if color in coloresPermitidos:
            self.color = color
  
class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        
    def cantidadAsientos(self):
        total = [1 for i in self.asientos if type(i) == Asiento]
        return total  

    def verificarIntegridad(self):
        for i in self.asientos:
            if i != None:
                if self.registro == i.registro and self.registro == self.motor.registro:
                    return "Auto original"
                else:
                    return "Las piezas no son originales"

class Motor:
    def __init__(self, numerosCilindros, tipo, registro):
        self.numerosCilindros = numerosCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        tiposPermitidos = ['electrico', 'gasolina']
        if tipo in tiposPermitidos:
            self.tipo = tipo
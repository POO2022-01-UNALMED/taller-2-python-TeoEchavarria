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
        total = 0
        for i in self.asientos:
            verificar = type(i) == Asiento
            if verificar == True:
                total += 1   
        return total  

    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for i in self.asientos:
                if self.registro != i.registro:
                    return "Las piezas no son originales"
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
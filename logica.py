# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False  # Estado inicial del vehículo: apagado

    def encender(self):
        self.encendido = True
        print(f"{self.marca} {self.modelo} encendido.")

    def apagar(self):
        self.encendido = False
        print(f"{self.marca} {self.modelo} apagado.")

    def obtener_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Encendido: {self.encendido}"

# Subclase Coche, que hereda de Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, color, tipo_motor, puertas):
        # Llamamos al constructor de la clase base (Vehiculo)
        super().__init__(marca, modelo, color)
        self.tipo_motor = tipo_motor  # Atributo específico para coches
        self.puertas = puertas  # Atributo específico para coches

    def obtener_informacion(self):
        # Modificamos el método obtener_informacion para incluir los atributos de Coche
        info_base = super().obtener_informacion()  # Obtenemos la información básica del vehículo
        return f"{info_base}, Tipo de motor: {self.tipo_motor}, Puertas: {self.puertas}"

    def abrir_sunroof(self):
        print(f"Abriendo el sunroof del {self.marca} {self.modelo}...")

# Crear una instancia de Vehiculo
vehiculo1 = Vehiculo("Toyota", "Corolla", "Rojo")
print(vehiculo1.obtener_informacion())  # Mostramos la información del vehículo
vehiculo1.encender()  # Encendemos el vehículo
vehiculo1.apagar()  # Apagamos el vehículo

print()  # Separador de salida

# Crear una instancia de Coche (subclase)
coche1 = Coche("BMW", "Serie 3", "Azul", "V6", 4)
print(coche1.obtener_informacion())  # Mostramos la información del coche
coche1.encender()  # Encendemos el coche
coche1.abrir_sunroof()  # Abrimos el sunroof del coche

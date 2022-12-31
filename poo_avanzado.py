# PROGRAMACION ORIENTADA A OBJETOS AVANZADO



# se declara la clase Vehiculo
class Vehiculo():
    # atributo de clase / fuera de los de instancia
    pais_origen = "Alemania"
    # Constructor de la clase
    def __init__(self, color, longitud_metros, ruedas):
    # Atributos de instancia
        self.color = color
        self.longitud_metros = longitud_metros
        self.ruedas = ruedas

    # Metodos

    def arrancar(self):
        print("El vehiculo ha arrancado")

    def parar(self):
        print("El vehiculo ha parado")

    def mostrar_info(self):
        print(f"Vehiculo de color {self.color}. con una longitud de {self.longitud_metros} metros y tiene {self.ruedas} ruedas.\nEl pais de origen es {self.pais_origen}")

# Instanciar

vehiculo_1 = Vehiculo("verde", 4, 4)
vehiculo_2 = Vehiculo("naranja", 12, 10)

# Llamadas a los metodos
vehiculo_2.arrancar()
vehiculo_2.mostrar_info()
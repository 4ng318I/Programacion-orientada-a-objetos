# PROGRAMACION ORIENTADA A OBJETOS BASICO

# se declara la clase Vehiculo
class Vehiculo():
    # Atributos
    color = None
    longitud_metros = None
    ruedas = 4

    # Metodos

    def arrancar(self):
        print("El vehiculo ha arrancado")

    def parar(self):
        print("El vehiculo ha parado")

# Instanciar

vehiculo_1 = Vehiculo()
vehiculo_2 = Vehiculo()

# crear una propiedad para solamente un vehiculo

vehiculo_2.material_aleron = "Fibra de Carbono"

# Llamadas a los metodos

vehiculo_1.arrancar()
vehiculo_1.parar()
print (vehiculo_2.material_aleron)
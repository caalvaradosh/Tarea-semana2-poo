# Clase Mascota
# Representa una mascota mediante atributos y métodos.

class Mascota:

    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad 

    def mostrar_informacion(self):
        print("\n--- INFORMACIÓN DE LA MASCOTA ---")
        print(f"Nombre : {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad   : {self.edad} años")

    def hacer_sonido(self):
        print(f"{self.nombre} está haciendo un sonido.")
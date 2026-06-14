# Programa tradicional para gestionar una mascota
# Utiliza variables y funciones, sin clases ni objetos.

def registrar_mascota():
    """Solicita los datos de la mascota."""
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    edad = input("Ingrese la edad de la mascota: ")

    return nombre, especie, edad


def mostrar_mascota(nombre, especie, edad):
    """Muestra la información registrada."""
    print("\n--- INFORMACIÓN DE LA MASCOTA ---")
    print(f"Nombre : {nombre}")
    print(f"Especie: {especie}")
    print(f"Edad   : {edad} años")


# Programa principal
nombre, especie, edad = registrar_mascota()
mostrar_mascota(nombre, especie, edad)
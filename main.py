# Lista para almacenar la información de las películas
lista_peliculas = []

# Función encargada de agregar películas a la lista con la información dada por el administrador
def info_peliculas():
    while len(lista_peliculas) < 3:  
        nombre = input("Ingrese el nombre de la película: ")
        dia_inicio = int(input("Ingrese el día desde el cual estará disponible la película (1-31): "))
        dia_fin = int(input("Ingrese el día hasta el cual estará disponible la película (1-31): "))
        sala = int(input("Ingrese la sala asignada (1 a 4): "))

        # Validación correcta de sala y fechas
        if (1 <= sala <= 4) or (1 <= dia_inicio <= 31) and (1 <= dia_fin <= 31) and (dia_inicio <= dia_fin):
            datospelicula = {  # diccionario con los datos de cada pelicula
                "nombre": nombre,
                "dia_inicio": dia_inicio,
                "dia_fin": dia_fin,
                "sala": sala
            } 
            lista_peliculas.append(datospelicula)
        else:
            print("Datos incorrectos. Asegúrate de ingresar correctamente los días y la sala.")

# Función para consultar las películas disponibles en una fecha específica
def disponibilidad_peliculas(dia_consulta):
    disponibles = []
    proximamente = []
    
    for datospelicula in lista_peliculas:
        if datospelicula["dia_inicio"] <= dia_consulta <= datospelicula["dia_fin"]:
            disponibles.append(f"{datospelicula['nombre']} en Sala {datospelicula['sala']}")
        elif dia_consulta < datospelicula["dia_inicio"]:
            proximamente.append(f"{datospelicula['nombre']} (se estrena el {datospelicula['dia_inicio']})")

    # Mostrar películas disponibles
    if disponibles:
        print(f"Películas disponibles el {dia_consulta} de octubre:")
        for disp in disponibles:
            print(disp)
    else:
        print(f"No hay películas disponibles el {dia_consulta} de octubre.")

    # Mostrar películas próximas a estrenarse
    if proximamente:
        print("Próximamente:")
        for prox in proximamente:
            print(prox)

# Función principal que coordina el flujo del programa
def principal():
    # Agregar las películas
    info_peliculas()

    while True:  # Bucle infinito para seguir preguntando por días
        dia_consulta = input("Ingrese el día de octubre que desea consultar (1-31) o 'salir' para terminar: ").strip()

        if dia_consulta.lower() == 'salir':
            print("Gracias por utilizar el programa. ¡Hasta luego!")
            break  # Salir del bucle y terminar el programa
        else:
            try:
                dia_consulta = int(dia_consulta)
                if 1 <= dia_consulta <= 31:
                    disponibilidad_peliculas(dia_consulta)
                else:
                    print("Día no válido. Debe estar entre 1 y 31.")
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número de día válido o 'salir'.")
            
# Ejecutar el programa principal
if __name__ == "__main__":
    principal()

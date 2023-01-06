import time

# Define el tiempo límite para el ingreso de datos en segundos
timeout = 5

# Almacena el tiempo de inicio
start_time = time.time()

# Inicializa la variable que almacena el input del usuario
user_input = ""

# Ciclo infinito
while True:
    # Si el tiempo límite ha transcurrido y el usuario no ha ingresado ningún valor
    if time.time() - start_time >= timeout and not user_input:
        # Rellena el input con el valor predeterminado
        user_input = "valor predeterminado"
        # Sal del ciclo
        break
    # Si el usuario ha ingresado un valor
    elif user_input:
        # Sal del ciclo
        break
    # Si el usuario aún no ha ingresado un valor y el tiempo límite no ha transcurrido
    else:
        # Pide al usuario que ingrese un valor
        user_input = input("Ingresa un valor: ")

# Muestra el valor final del input del usuario
print(user_input)

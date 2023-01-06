import select
import sys
import time

# Definir las cantidades de tiempo en segundos para los estados 2 y 3
time1 = 1
time2 = 8 
time3 = 5
time4 = 10

last_input = None
# Iniciar el estado en 1
state = 0

start_time=time.time() #tiempo actual

def input_with_timeout(prompt, timeout):
  print(prompt, end="")
  rlist, _, _ = select.select([sys.stdin], [], [], timeout)
  if rlist:
    return sys.stdin.readline().strip()
  return ""


# Bucle infinito
while True:

    if state == 0:
        print("Entering state 0")
        # Leer una entrada del usuario
        user_input = input()

        # Si el usuario escribe "R", cambiar al estado 1 si no, cambia al 3
        if user_input == "R":
            state = 1

        elif user_input == "M":
            state= 3
    # Si el estado es 1
    elif state == 1:
        print("Entering state 1")
        # Leer una entrada del usuario
        time.sleep(time1)

        state = 2

    # Si el estado es 2
    elif state == 2:
        if last_input or time.time() - start_time > time2:
        # Mostrar el estado 2
            print("Entering state 2")
            response = input_with_timeout("Ingresa un valor: ", time2)
            time.sleep(time2)
            last_input = response
            print("ingreso por fin")
            if response == "R" :
                state = 1

            elif response == "":
                state= 0

    # Si el estado es 3
    elif state == 3:
        # Mostrar el estado 3
        print("Entering state 3")

        # Esperar la cantidad de tiempo 2
        time.sleep(time3)

        # Cambiar al estado 4
        state = 4

    elif state == 4:
        # Mostrar el estado 3
        if last_input or time.time() - start_time > time4:
            print("Entering state 4")
            user_input = input()
            
            last_input = user_input
            print("ingreso por fin")
            if user_input == "R":
                state = 3

            elif user_input == "":
                time.sleep(time4)
                state= 0
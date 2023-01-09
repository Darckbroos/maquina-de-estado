import time
import threading

def limit_input(prompt, timeout):
  timer = threading.Timer(timeout, lambda: print("\n"))
  timer.start()
  try:
    return input(prompt)
  except:
    return print("\n")
  finally:
    timer.cancel()

# Definir las cantidades de tiempo en segundos para los estados 2 y 4
time1 = 1
time2 = 8 
time3 = 5
time4 = 10

last_input = None
# Iniciar el estado en 1
state = 0

start_time=time.time()

# Bucle infinito
while True:
     #tiempo actual
    tiempor_corriendo= time.time() - start_time
    if state == 0:
        print("Entering state 0")
        # Leer una entrada del usuario
        user_input = input()
        print (tiempor_corriendo)

        # Si el usuario escribe "R", cambiar al estado 1 si no, cambia al 3
        if user_input == "R":
            state = 1

        elif user_input == "M":
            state= 3
    # Si el estado es 1
    elif state == 1:
        print("Entering state 1")
        print (tiempor_corriendo)
        # Leer una entrada del usuario
        time.sleep(time1)

        state = 2

    # Si el estado es 2
    elif state == 2:
        while True:
            timestate2= time.time() - tiempor_corriendo - start_time
            print("Entering state 2")
            print (timestate2)
            user_input = limit_input("Ingresa una respuesta: ", time2)
            if user_input == "R" and timestate2 >= time2:
                state = 1
                break
            else :
                
                state= 0
                break

    # Si el estado es 3
    elif state == 3:
        # Mostrar el estado 3
        print("Entering state 3")
        print (start_time)
        # Esperar la cantidad de tiempo 
        time.sleep(time3)

        # Cambiar al estado 4
        state = 4

    elif state == 4:
        # Mostrar el estado 4
        while True:
            timestate2= time.time() - tiempor_corriendo - start_time
            print("Entering state 4")
            print (timestate2)
            user_input = limit_input("Ingresa una respuesta: ", time4)
            if user_input == "R" and  timestate2 >= time4 :
                state = 3
                break
            else:
                
                state= 0
                break
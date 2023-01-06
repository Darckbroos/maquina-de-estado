import time

def transition(state, event, elapsed_time):
  if state in transitions:
        if event in transitions[state]:
            return transitions[state][event]
  return state
start_time = time.time()
print (start_time)
elapsed_time = time.time() - start_time

start_estado= time.time() - elapsed_time - elapsed_time + elapsed_time
time.sleep(1)

print (elapsed_time)
def on_enter_state0():
  print("Entering state 0") 
  print ("llega aqui")

def on_enter_state1():
  print("Entering state 1")
  print ("llega aqui")
  print (elapsed_time)
  print(start_estado)
  time.sleep(5)
  print(start_estado)

def on_enter_state2():
  print("Entering state 2")
  print("llego aqui")

def on_enter_state3():
  print("Entering state 3")
  print("llego aqui")

def on_enter_state4():
  print("Entering state 4")
  print ("llego aqui")

transitions = {
  'state0': {'R': 'state1', 'M': 'state3'},
  'state1': {'S': 'state2'},
  'state2': {'R': 'state1', 'time': 'state0'},
  'state3': {'time': 'state4'},
  'state4': {'M': 'state3', 'time': 10, 'next_state': 'state0'},
}

state = 'state0'
on_enter_state0()



while True:
  elapsed_time = time.time() - start_time
  event = input("Enter an event: ")
  state = transition(state, event, elapsed_time)
  if state == 'state0':
    on_enter_state0()
  elif state == 'state1':
    on_enter_state1()
  elif state == 'state2':
    on_enter_state2()
  elif state == 'state3':
    on_enter_state3()
  elif state == 'state4':
    on_enter_state4()
  else:
    print("Invalid state: " + state)
    break

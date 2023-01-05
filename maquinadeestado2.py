import time

def transition(state, event, elapsed_time):
  if state in transitions:
    if elapsed_time > transitions[state]['time']:
        if event in transitions[state]:
            return transitions[state][event]['next_state']
  return state

def on_enter_state0():
  print("Entering state 0")

def on_enter_state1():
  print("Entering state 1")

def on_enter_state2():
  print("Entering state 2")

def on_enter_state3():
  print("Entering state 3")

def on_enter_state4():
  print("Entering state 4")

transitions = {
  'state0': {'R': 'state1', 'M': 'state3'},
  'state1': {'time': 1, 'next_state': 'state2'},
  'state2': {'R': 'state1', 'time': 8, 'next_state': 'state0'},
  'state3': {'time': 5, 'next_state': 'state4'},
  'state4': {'M': 'state3', 'time': 10, 'next_state': 'state0'},
}

state = 'state0'
on_enter_state0()

start_time = time.time()

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
  time.sleep(1)

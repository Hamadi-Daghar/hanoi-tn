

class State():

  state = 0
  #0(state 1) to 2**20 - 1 = 1 048 575 (state 2**20)

  def increment_state(increment:int):
    State.state += increment
    if State.state < 0:
      State.state = 0
    elif State.state > (2**20 - 1):
      State.state = 2**20 - 1
  
  def start_state():
    State.state = 0
  
  def end_state():
    State.state = 2**20 - 1
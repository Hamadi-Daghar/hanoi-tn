import math  

def render_time(seconds: int)-> str:
  """Retourne une chaîne de caractère représentant le laps de temps "seconds" en jours, heures, minutes et secondes.

  Le temps à représenter sera compris entre 0s et (2**20)-1 s, soit 12j3h16min15s environ.

  Args:
      seconds (int): Le laps de temps à convertir, en secondes.

  Returns:
      str: La chaîne de caractère représentant le résultat.
  """
  values: list[int] = [0,0,0,0] #j,h,m,s
  secs: int = seconds

  if seconds == 0:
    return "Terminé !"

  #jours (60*60*24s)
  values[0] = secs // (60*60*24)
  secs = secs % (60*60*24)

  #heures (60*60s)
  values[1] = secs // (60*60)
  secs = secs % (60*60)

  #minutes (60s)
  values[2] = secs // 60
  secs = secs % 60

  #secondes
  values[3] = secs

  if values[0] != 0: #jours
    return f"{values[0]} jour{plural(values[0])} {values[1]} heure{plural(values[1])}\n{values[2]} minute{plural(values[2])} {values[3]} seconde{plural(values[3])}"
  elif values[1] != 0: #heures
    return f"{values[1]} heure{plural(values[1])}\n{values[2]} minute{plural(values[2])} {values[3]} seconde{plural(values[3])}"
  elif values[2] != 0: #minutes
    return f"\n{values[2]} minute{plural(values[2])} {values[3]} seconde{plural(values[3])}"
  else: #secondes
    return f"{values[3]} seconde{plural(values[3])}"

def plural(value: int)-> str:
  """Retourne "s" si la valeur 'value' est > 1, "" sinon.

  Args:
      value (int): La valeur à tester.

  Returns:
      str: 's' si value > 1, '' sinon. 
  """
  return 's' if value > 1 else ''


def remaining_time(state: int, speed: int)-> int:
  """Retourne le temps restant pour résoudre les tours de Hanoï, à partir de l'état courant "state" et de la vitesse sélectionnée "speed".

  Args:
      state (int): L'état courant.

  Returns:
      int: Le nombre de secondes pour passer de l'état courant à l'état 2**20 à la vitesse 'speed' (en mouvement/s), arrondi à la seconde supérieure.
  """
  moves:int = (2**20 - 1) - state

  return math.ceil(moves/speed)
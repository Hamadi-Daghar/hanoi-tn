"""
Manipule les tours de Hanoï sous la forme d'une liste de listes d'entiers [[],[],[]], dans laquelle chaque liste correspond à une tour ([0] la tour la plus à gauche).
Les entiers représentent des disques, avec 1 le plus petit.
"""

import hanoi.logic.state as state

def compute_state(nbr_disques: int, etat: int)-> list[list[int]]:
  """Retourne l'état des tours à l'état etat pour nbr_disques disques.

  Args:
      nbr_disques (int): Le nombre de disques utilisés
      etat (int): L'indice de l'état retourné, entre 0 (état 1 initial) et 2**nbr_disques - 1 (état 2**n final) inclus.

  Returns:
      list[list[int]]: La liste représentant l'état des tours obtenu.
  """

  tours = [[],[],[]]
  nbr_mouvements = etat

  # pour chaque disque n de 1 à nbr_disques
  for n in range(1, nbr_disques + 1):
      
    #compter mouvements
    if (nbr_mouvements < 2**(n-1)):
      compteur = 0
    else:
      dernier_mouvement = 2**(n-1)
      compteur = 1
      while dernier_mouvement + 2**n <= nbr_mouvements:
        compteur += 1
        dernier_mouvement += 2**n
    
    #déterminer direction
    vers_gauche = (n%2 == 0) #vers la gauche si n pair

    #calculer position après mouvement nbr_mouvements
    if vers_gauche: 
      tours[(- compteur) % 3].append(n)
    else:
      tours[compteur % 3].append(n)
  
  #inverser tours 1 et 2 si nbr_disques impair
  if nbr_disques % 2 == 1:
    temp = tours[2]
    tours[2] = tours[1]
    tours[1] = temp

  #remettre dans l'ordre
  for i in range(3):
    tours[i].reverse()
  
  return tours

def compute_move_from_state(nbr_disques: int, etat_depart: int, towers: list[list[int]])-> tuple[int,int]:
  """Retourne un tuple (départ, arrivée) représentant le mouvement suivant l'état etat_depart modélisé par towers, pour un problème à nbr_disques disques.
  Le tuple contient des indices des tours (0,1,2).

  Args:
      nbr_disques (int): Le nombre de disques du problème.
      etat_depart (int): L'indice de l'état de départ, entre 0 (état 1 initial) et 2**nbr_disques - 1 (état 2**n final) inclus.
      towers (list[list[int]]): La modélisation des tours à l'état de départ.

  Returns:
      tuple[int,int]: Un tuple (départ, arrivée) représentant les indices de la tour de départ et d'arrivée du mouvement. None si etat_depart est invalide.
  """

  if (etat_depart < 0 or etat_depart >= 2**nbr_disques - 1):
    return None

  #le mouvement implique le disque 1
  if etat_depart % 2 == 0:
    
    depart = tower_with_one(towers)

    if nbr_disques % 2 == 1:
      #disque 1 se déplace vers la gauche
      arrivee = (depart - 1) % 3
    else:
      #vers la droite
      arrivee = (depart + 1) % 3
    
    return (depart, arrivee)

  #le mouvement n'implique pas le disque 1
  else:
    index = [0,1,2]
    index.remove(tower_with_one(towers))

    if len(towers[index[0]]) == 0:
      return(index[1], index[0])
    elif len(towers[index[1]]) == 0:
      return (index[0], index[1])
    elif towers[index[0]][-1] < towers[index[1]][-1]:
      return (index[0], index[1])
    else:
      return(index[1], index[0])
  
def tower_with_one(towers: list[list[int]])-> int:
  """Retourne l'indice (0,1,2) de la tour contenant le disque 1 dans la représentation towers.

  Args:
      towers (list[list[int]]): La représentation des tours.

  Returns:
      int: L'indice de la tour contenant le disque 1. Retourne -1 en cas d'erreur.
  """
  if len(towers[0]) > 0 and towers[0][-1] == 1:
    return 0
  elif len(towers[1]) > 0 and towers[1][-1] == 1:
    return 1
  elif len(towers[2]) > 0 and towers[2][-1] == 1:
    return 2
  else:
    return -1

def compute_state_and_move(nbr_disques: int, etat_depart: int)-> tuple[list[list[int]], tuple[int, int]]:
  """À partir de l'indice d'un état de départ etat_depart et pour un problème à nbr_disques disques, retourne la modélisation des tours à cet état ainsi qu'un tuple représentant le mouvement à réaliser pour accéder à l'état suivant.

  Args:
      nbr_disques (int): Le nombre de disques du problème.
      etat_depart (int): L'indice de l'état de départ.

  Returns:
      tuple[list[list[int]], tuple[int, int]]: De la forme (tours, mouvement).
  """
  towers = compute_state(nbr_disques, etat_depart)
  move = compute_move_from_state(nbr_disques, etat_depart, towers)

  return (towers, move)

# fonctions pour l'interface, vont récupérer state de hanoi.logic.state

def current_state(nbr_disques: int)-> list[list[int]]:
  """Retourne la représentation des tours à l'état actuel (depuis hanoi.logic.state) pour nbr_disques disques.

  Args:
      nbr_disques (int): Le nombre de disques du problème.

  Returns:
      list[list[int]]: La représentation des tours.
  """
  return compute_state(nbr_disques, state.State.state)

def current_state_and_move(nbr_disques: int)-> tuple[list[list[int]], tuple[int, int]]:
  """Retourne la représentation des tours à l'état actuel, et la représentation du mouvement suivant.

  Args:
      nbr_disques (int): Le nombre de disques du problème.

  Returns:
      tuple[list[list[int]], tuple[int, int]]: Sous la forme (tours, mouvement).
  """
  return compute_state_and_move(nbr_disques, state.State.state)

# state = compute_state(20,0)
# print("État 0 :", state)
# for i in range(0,19):
#   move = compute_move(20, i, state)  
#   print(f"[{i}] {move[0]} -> {move[1]} [{i+1}]")
#   state = compute_state(20,i+1)
#   print(f"État {i+1} :", state)

# for i in range(0,20):
#   result = compute_state_and_move(20, i)
#   print(f"État {i+1} :", result[0])
#   print(f"Mouvement {i+1} -> {i+2} :", result[1])
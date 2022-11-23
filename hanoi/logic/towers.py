"""
Manipule les tours de Hanoï sous la forme d'une liste de listes d'entiers [[],[],[]], dans laquelle chaque liste correspond à une tour ([0] la tour la plus à gauche).
Les entiers représentent des disques, avec 1 le plus petit.
"""

# import hanoi.logic.state as state

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

def edge_state(disk_amount: int, final: bool = False)-> list[list[int]]:
  towers = [[],[],[]]
  index: int = 2 if final else 0

  for i in range(disk_amount, 0, -1):
    towers[index].append(i)

  return towers


### ANCIENNE FONCTION
# def compute_move(disk_amount: int, state: int, towers: list[list[int]])-> tuple[int,int]:
#   """Retourne un tuple (départ, arrivée) représentant le mouvement suivant l'état state modélisé par towers, pour un problème à disk_amount disques.
#   Le tuple contient des indices des tours (0,1,2).

#   Args:
#       disk_amount (int): Le nombre de disques du problème.
#       state (int): L'indice de l'état de départ, entre 0 (état 1 initial) et 2**disk_amount - 1 (état 2**n final) inclus.
#       towers (list[list[int]]): La modélisation des tours à l'état de départ.

#   Returns:
#       tuple[int,int]: Un tuple (départ, arrivée) représentant les indices de la tour de départ et d'arrivée du mouvement. None si state est invalide.
#   """

#   if (state < 0 or state >= 2**disk_amount - 1):
#     return None

#   #le mouvement implique le disque 1
#   if state % 2 == 0:
    
#     depart = _tower_with_one(towers)

#     if disk_amount % 2 == 1:
#       #disque 1 se déplace vers la gauche
#       arrivee = (depart - 1) % 3
#     else:
#       #vers la droite
#       arrivee = (depart + 1) % 3
    
#     return (depart, arrivee)

#   #le mouvement n'implique pas le disque 1
#   else:
#     index = [0,1,2]
#     index.remove(_tower_with_one(towers))

#     if len(towers[index[0]]) == 0:
#       return(index[1], index[0])
#     elif len(towers[index[1]]) == 0:
#       return (index[0], index[1])
#     elif towers[index[0]][-1] < towers[index[1]][-1]:
#       return (index[0], index[1])
# #     else:
# #       return(index[1], index[0])
  

# def _tower_with_one(towers: list[list[int]])-> int:
#   """Retourne l'indice (0,1,2) de la tour contenant le disque 1 dans la représentation towers.

#   Args:
#       towers (list[list[int]]): La représentation des tours.

#   Returns:
#       int: L'indice de la tour contenant le disque 1. Retourne -1 en cas d'erreur.
#   """
#   if len(towers[0]) > 0 and towers[0][-1] == 1:
#     return 0
#   elif len(towers[1]) > 0 and towers[1][-1] == 1:
#     return 1
#   elif len(towers[2]) > 0 and towers[2][-1] == 1:
#     return 2
#   else:
#     return -1


def neighbor_state(disk_amount: int, state: int, towers: list[list[int]], increment: int)-> list[list[int]]:
  """Retourne la représentation des tours à l'état state + increment.

  Args:
      disk_amount (int): Nombre de disques du problème.
      state (int): État de départ.
      towers (list[list[int]]): Représentation de l'état de départ.
      increment (int): Différence entre l'état d'arrivée et l'état de départ.

  Returns:
      list[list[int]]: Représentation de l'état obtenu.
  """
  if (state == 0 and increment < 0) or (state == 2**disk_amount - 1 and increment > 0):
    return towers

  while increment != 0:
    
    if increment > 0:
      return neighbor_state(disk_amount, state+1, _apply_move(towers, compute_next_move(disk_amount, state, towers)), increment-1)
    
    if increment < 0:
      return neighbor_state(disk_amount, state-1, _apply_move(towers, _compute_back_move(disk_amount, state, towers)), increment+1)
  
  return towers


def _next_state(disk_amount: int, state: int, towers: list[list[int]])-> list[list[int]]:
  """Retourne l'état state+1 à partir de la représentation towers de l'état state.

  Args:
      disk_amount (int): Le nombre de disques du problème.
      state (int): L'indice de l'état de départ.
      towers (list[list[int]]): La représentation de l'état de départ.

  Returns:
      list[list[int]]: La représentation de l'état suivant l'état de départ.
  """
  return _apply_move(towers, compute_next_move(disk_amount, state, towers))


def _previous_state(disk_amount: int, state: int, towers: list[list[int]])-> list[list[int]]:
  """Retourne l'état state-1 à partir de la représentation towers de l'état state.

  Args:
      disk_amount (int): Le nombre de disques du problème.
      state (int): L'indice de l'état de départ.
      towers (list[list[int]]): La représentation de l'état de départ.

  Returns:
      list[list[int]]: La représentation de l'état précédant l'état de départ.
  """
  return _apply_move(towers, _compute_back_move(disk_amount, state, towers))


def _apply_move(towers: list[list[int]], move: tuple[int, int])-> list[list[int]]:
  """Applique le mouvement move à l'état représenté par towers et retourne le nouvel état obtenu.

  Args:
      towers (list[list[int]]): L'état initial.
      move (tuple[int, int]): Le mouvement à appliquer à towers.

  Returns:
      list[list[int]]: L'état obtenu après avoir appliqué le mouvement.
  """
  towers[move[1]].append(towers[move[0]].pop())
  return towers


def compute_next_move(disk_amount: int, state: int, towers: list[list[int]])-> tuple[int, int]:
  """Retourne le prochain mouvement sous la forme (depart, arrivée)

  Args:
      disk_amount (int): Nombre de disques
      state (int): Indice de l'état actuel (états de 0 à 2**disk_amount - 1)
      towers (list[list[int]]): État actuel des tours

  Returns:
      tuple[int, int]: Représentation du prochain mouvement sous la forme (départ, arrivée), indices entre 0 (gauche) et 2 (droite)
  """
  if state < 0 or state >= 2**disk_amount:
    return None

  #détermine l'indice de la tour sur laquelle se trouve le disque 1
  if _top(disk_amount, towers[0]) == 1:
    one_tower = 0
  elif _top(disk_amount, towers[1]) == 1:
    one_tower = 1
  else:
    one_tower = 2

  if state%2 == 0:
    #indice de mouvement pair ==> mouvement du disque 1

    if disk_amount%2 == 0:
      #nombre de disques pair ==> vers la droite
      return (one_tower, (one_tower+1)%3)
        
    else:
      #nombre de disques impair ==> vers la gauche
      return (one_tower, (one_tower-1)%3)

  else:
    #indice de mouvement impair ==> mouvement n'impliquant pas le disque 1
    remaining_towers = [0,1,2]
    remaining_towers.remove(one_tower)
    
    if _top(disk_amount, towers[remaining_towers[0]]) < _top(disk_amount, towers[remaining_towers[1]]):
      return (remaining_towers[0], remaining_towers[1])
    else:
      return (remaining_towers[1], remaining_towers[0])


def _compute_back_move(disk_amount: int, state: int, towers: list[list[int]])-> list[list[int]]:
  """Retourne le mouvement menant à l'état précédent sous la forme (depart, arrivée)

  Args:
      disk_amount (int): Nombre de disques
      state (int): Indice de l'état actuel (états de 0 à 2**disk_amount - 1)
      towers (list[list[int]]): État actuel des tours

  Returns:
      tuple[int, int]: Représentation du mouvement sous la forme (départ, arrivée), indices entre 0 (gauche) et 2 (droite)
  """
  if state < 1 or state > 2**disk_amount:
    return None

  #détermine l'indice de la tour sur laquelle se trouve le disque 1
  if _top(disk_amount, towers[0]) == 1:
    one_tower = 0
  elif _top(disk_amount, towers[1]) == 1:
    one_tower = 1
  else:
    one_tower = 2

  if state%2 == 1:
    #indice de state impair ==> mouvement du disque 1

    if disk_amount%2 == 0:
      #nombre de disques pair ==> vers la gauche
      return (one_tower, (one_tower-1)%3)
        
    else:
      #nombre de disques impair ==> vers la droite
      return (one_tower, (one_tower+1)%3)

  else:
    #indice de state pair ==> mouvement n'impliquant pas le disque 1
    remaining_towers = [0,1,2]
    remaining_towers.remove(one_tower)
    
    if _top(disk_amount, towers[remaining_towers[0]]) < _top(disk_amount, towers[remaining_towers[1]]):
      return (remaining_towers[0], remaining_towers[1])
    else:
      return (remaining_towers[1], remaining_towers[0])


def _top(nbr_disques: int, list: list)-> int:
  """Retourne le dernier élément de la liste si elle n'est pas vide, nbr_disques+1 sinon.

  Args:
      list (list): La liste.
      nbr_disques (int): Le nombre de disques du problème.

  Returns:
      int: Le dernier élément de la liste, ou nbr_disques+1 si la liste est vide.
  """
  if len(list) == 0:
    return nbr_disques + 1
  else:
    return list[-1]















# def compute_state_and_move(nbr_disques: int, etat_depart: int)-> tuple[list[list[int]], tuple[int, int]]:
#   """À partir de l'indice d'un état de départ etat_depart et pour un problème à nbr_disques disques, retourne la modélisation des tours à cet état ainsi qu'un tuple représentant le mouvement à réaliser pour accéder à l'état suivant.

#   Args:
#       nbr_disques (int): Le nombre de disques du problème.
#       etat_depart (int): L'indice de l'état de départ.

#   Returns:
#       tuple[list[list[int]], tuple[int, int]]: De la forme (tours, mouvement).
#   """
#   towers = compute_state(nbr_disques, etat_depart)
#   move = compute_move(nbr_disques, etat_depart, towers)

#   return (towers, move)

# # fonctions pour l'interface, vont récupérer state de hanoi.logic.state

# def current_state(nbr_disques: int)-> list[list[int]]:
#   """Retourne la représentation des tours à l'état actuel (depuis hanoi.logic.state) pour nbr_disques disques.

#   Args:
#       nbr_disques (int): Le nombre de disques du problème.

#   Returns:
#       list[list[int]]: La représentation des tours.
#   """
#   return compute_state(nbr_disques, state.State.state)

# def current_state_and_move(nbr_disques: int)-> tuple[list[list[int]], tuple[int, int]]:
#   """Retourne la représentation des tours à l'état actuel, et la représentation du mouvement suivant.

#   Args:
#       nbr_disques (int): Le nombre de disques du problème.

#   Returns:
#       tuple[list[list[int]], tuple[int, int]]: Sous la forme (tours, mouvement).
#   """
#   return compute_state_and_move(nbr_disques, state.State.state)







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
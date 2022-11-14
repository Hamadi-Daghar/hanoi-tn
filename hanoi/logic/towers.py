"""
Manipule les tours de Hanoï sous la forme d'une liste de listes d'entiers [[],[],[]], dans laquelle chaque liste correspond à une tour ([0] la tour la plus à gauche).
Les entiers représentent des disques, avec 1 le plus petit.
"""

def compute_state(nbr_disques: int, etat: int)-> list[list[int]]:
  """Retourne l'état des tours #etat pour nbr_disques disques.

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

def compute_move(nbr_disques: int, etat_arrivee: int)-> tuple[int,int]:
  """Retourne un tuple (départ, arrivée) représentant le mouvement qui a mené à l'état etat_arrivee pour un problème à nbr_disques disques.
  Le tuple contient des indices des tours (0,1,2).

  Args:
      nbr_disques (int): Le nombre de disques du problème.
      etat_arrivee (int): L'indice de l'état d'arrivée, entre 0 (état 1 initial) et 2**nbr_disques - 1 (état 2**n final) inclus.

  Returns:
      tuple[int,int]: Un tuple (départ, arrivée) représentant les indices de la tour de départ et d'arrivée du mouvement.
  """
  last_state: list[list[int]] = compute_state(nbr_disques, etat_arrivee - 1)


  #le mouvement implique le disque 1
  if etat_arrivee % 2 == 1:
    
    depart = tower_with_one(last_state)

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
    index.remove(tower_with_one(last_state))

    if len(last_state[index[0]]) == 0:
      return(index[1], index[0])
    elif len(last_state[index[1]]) == 0:
      return (index[0], index[1])
    elif last_state[index[0]][-1] < last_state[index[1]][-1]:
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


# print(compute_state(20,0))
# for i in range(1,20):
#   move = compute_move(20, i)  
#   print(f"{move[0]} -> {move[1]}")
#   print(compute_state(20,i))
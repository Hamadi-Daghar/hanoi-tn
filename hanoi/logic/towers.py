"""
Manipule les tours de Hanoï sous la forme d'une liste de listes d'entiers [[],[],[]], dans laquelle chaque liste correspond à une tour ([0] la tour la plus à gauche).
Les entiers représentent des disques, avec 1 le plus petit.
"""

def calcul_etat(nbr_disques: int, etat: int)-> list[list[int]] :
  """Retourne l'état des tours #etat pour nbr_disques disques.

  Args:
      nbr_disques (int): Le nombre de disques utilisés
      etat (int): L'indice de l'état  retourné, 
        entre 0 (état 1 initial) et 2**nbr_disques - 1 (état 2**n final) inclus.

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


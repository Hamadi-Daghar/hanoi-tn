"""
Permet la manipulation de fichiers pour sauvegarder l'avancement du fil rouge.
"""

import csv
import datetime
import os

from hanoi.logic.state import State

def save_now()-> None:
  file_path = "log.csv"
  exists = os.path.exists(file_path)

  with open(file_path, 'a', newline = '') as file:

    writer = csv.writer(file)
    now = datetime.datetime.now()

    if not exists:
      writer.writerow(["visiteurs", "date"])
      print("Fichier", file_path, "initialisé")
    
    date_str = now.strftime("%Y-%m-%d %H:%M:%S")
    writer.writerow([State.state, date_str])
    print("État ajouté au fichier")
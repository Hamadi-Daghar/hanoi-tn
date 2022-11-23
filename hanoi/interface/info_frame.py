import tkinter.font as font

import customtkinter as ctk

from hanoi.logic.state import State
import hanoi.logic.temporality as temporality

class InfoFrame(ctk.CTkFrame):

  def __init__(self, parent, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)

    #grid
    self.columnconfigure(0, weight = 1)
    self.rowconfigure((0,1,2,3,4,5,6), weight = 1)

    self.parent = parent
    self.colors = parent.colors
    self.fontPolicy = parent.fontPolicy

    #titre
    self.title = ctk.CTkLabel(
      self, text = "Tours de Hanoï",
      text_color = self.colors.get('darkBlue'),
      text_font = font.Font(size = 35, family = self.fontPolicy, weight = "bold")
    )
    self.title.grid(
      column = 0, row = 0, 
    )

    self.separator1 = ctk.CTkLabel(
      self, 
      text_color = self.colors.get("darkBlue"),
      text = "--------------------------------------------",
      text_font = font.Font(size = 15, family = self.fontPolicy)
    )
    self.separator1.grid(
      column = 0, 
      row = 1,
      pady = 10
    )

    #progression
    self.progress = ctk.CTkLabel(
      self,
      text_color = self.colors.get('darkBlue'),
      text_font = font.Font(size = 18, family = self.fontPolicy)
    )
    self.progress.grid(
      column = 0, row = 2,
      pady = 20
    )

    #état/mouvement principal
    self.main_state = ctk.CTkLabel(
      self,
      text_color = self.colors.get('darkBlue'),
      text_font = font.Font(size = 18, family = self.fontPolicy), 
    )
    self.main_state.grid(
      column = 0, row = 3
    )

    #état mouvement secondaire
    self.secondary_state = ctk.CTkLabel(
      self,
      text_color = self.colors.get('darkBlue'),
      text_font = font.Font(size = 18, family = self.fontPolicy)
    )
    self.secondary_state.grid(
      column = 0, row = 4
    )

    #temps restant
    self.remaining_time = ctk.CTkLabel(
      self,
      text_color = self.colors.get('darkBlue'),
      text_font = font.Font(size = 18, family = self.fontPolicy)
    )
    self.remaining_time.grid(
      column = 0, row = 5,
      pady = 20
    )

    self.separator2 = ctk.CTkLabel(
      self,
      text_color = self.colors.get("darkBlue"),
      text = "--------------------------------------------",
      text_font = font.Font(size = 15, family = self.fontPolicy)
    )
    self.separator2.grid(
      column = 0, 
      row = 6,
      pady = 10
    )
  
  def update_display(self):

    state = State.state
    move_display = State.move_display
    
    self.progress.configure(
      text = f"Progression : { format( round(((state)/(2**20 - 1))*100, 6), 'f').rstrip('0').rstrip('.') } %"
      # text = format( round(((state+1)/(2**20))*100, 6), 'f').rstrip('0').rstrip('.') + " %"
    )

    self.main_state.configure(text = (
      f"Mouvement {state + 1}" if move_display else 
      f"État {state + 1}"
    ))

    self.secondary_state.configure(text = (
      f"(De l'État {state + 1} à l'État {state + 2})" if move_display else
      f"(Obtenu après {state} mouvements)"
    ))

    self.remaining_time.configure(text = (
      "Temps restant : " + temporality.render_time(temporality.remaining_time(state, State.speed))
    ))
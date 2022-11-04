import customtkinter as ctk
import tkinter.font as font

class InfoFrame(ctk.CTkFrame):

  def __init__(self, parent, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)

    #grid
    self.columnconfigure(0, weight = 1)
    self.rowconfigure((0,1,2,3,4), weight = 1)

    self.parent = parent

    #titre
    self.title = ctk.CTkLabel(
      self, text = "Tours de Hanoï", 
      text_font = font.Font(size = 40, weight = "bold")
    )
    self.title.grid(
      column = 0, row = 0,
      pady = (0,10)
    )

    #progression
    self.progress = ctk.CTkLabel(
      self, text = "0,00324 %",
      text_color = "green",
      text_font = font.Font(size = 50)
    )
    self.progress.grid(
      column = 0, row = 1, 
      pady = 30
    )

    #état/mouvement principal
    self.main_state = ctk.CTkLabel(
      self,
      text_color = "blue",
      text_font = font.Font(size = 30)
    )
    self.main_state.grid(
      column = 0, row = 2,
      pady = 10
    )

    #état mouvement secondaire
    self.secondary_state = ctk.CTkLabel(
      self, wraplength = 420,
      text_color = "red",
      text_font = font.Font(size = 20)
    )
    self.secondary_state.grid(
      column = 0, row = 3,
      pady = 10
    )

    #temps restant
    self.remaining_time = ctk.CTkLabel(
      self, text = "Temps restant :\nuhzeuif",
      text_font = font.Font(size = 20)
    )
    self.remaining_time.grid(
      column = 0, row = 4,
      pady = 10
    )
  
  def update_display(self, count, move_display):

    self.main_state.configure(text = (
      f"Mouvement #{count + 1}" if move_display else 
      f"État #{count + 1}"
    ))
    self.secondary_state.configure(text = (
      f"État {count + 1} -> État {count + 2}" if move_display else
      f"Obtenu après {count} mouvements"
    ))
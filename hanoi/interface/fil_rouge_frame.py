import tkinter as tk
import customtkinter as ctk
import tkinter.font as font

class FilRougeFrame(ctk.CTkFrame):

  def __init__(self, parent, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)

    #grid
    self.columnconfigure(0, weight = 1)
    self.rowconfigure((0,1,2,3,4), weight = 1)

    self.parent = parent

    #titre
    self.title = ctk.CTkLabel(
      self, text = "Fil Rouge", 
      text_font = font.Font(size = 30, weight = "bold")
    )
    self.title.grid(
      column = 0, row = 0,
      pady = 10, sticky = ctk.W
    )

    self.placeholder = ctk.CTkLabel(
      self, text = "À FAIRE",
      text_font = font.Font(size = 25)
    )
    self.placeholder.grid(
      column = 0, row = 1
    )
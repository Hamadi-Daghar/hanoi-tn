import tkinter as tk
import tkinter.font as font

import customtkinter as ctk

import hanoi.logic.data as data

class FilRougeFrame(ctk.CTkFrame):

  def __init__(self, parent, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)

    #grid
    self.columnconfigure(0, weight = 1)
    self.rowconfigure((0,1,2,3,4), weight = 1)

    self.parent = parent
    self.colors = parent.colors
    self.font_family = parent.font_family

    #titre
    self.title = ctk.CTkLabel(
      self, text = "Fil Rouge", 
      text_font = font.Font(size = 30, family = self.font_family, weight = "bold")
    )
    self.title.grid(
      column = 0, row = 0,
      pady = 5, sticky = ctk.W
    )

    self.placeholder = ctk.CTkLabel(
      self, text = "À FAIRE",
      text_font = font.Font(size = 25, family = self.font_family)
    )
    self.placeholder.grid(
      column = 0, row = 1
    )

    self.button = ctk.CTkButton(
      self, text = "Save State",
      command = data.save_now,
      text_color = self.colors.get("dark_blue"),
      text_font = font.Font(size = 30, family = self.font_family)
    )
    self.button.grid(
      column = 0, row = 2
    )

  def stage(self)-> None:
    """Fait apparaître la frame sur l'interface.
    """
    self.grid(
      column = 0, row = 2, columnspan = 2,
      sticky = ctk.EW
    )
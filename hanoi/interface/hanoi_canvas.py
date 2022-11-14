import tkinter.font as font

import customtkinter as ctk

class HanoiCanvas(ctk.CTkCanvas):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.canvas = ctk.CTkCanvas(self, width = 1500, height = 950, bg = "#FFFFFF")
    self.canvas.grid(column = 0, row = 0, sticky = ctk.NSEW)
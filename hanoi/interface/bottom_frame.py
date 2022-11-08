import tkinter as tk
import customtkinter as ctk
import tkinter.font as font
import os

class BottomFrame(ctk.CTkFrame):

  def __init__(self, parent, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)

    self.parent = parent

    self.rewind_icon = tk.PhotoImage(
      file = os.path.join(os.path.dirname(__file__), "..", "assets", "rewind.png")
    ).subsample(2)
    self.previous_icon = tk.PhotoImage(
      file = os.path.join(os.path.dirname(__file__), "..", "assets", "previous.png")
    ).subsample(2)
    self.next_icon = tk.PhotoImage(
      file = os.path.join(os.path.dirname(__file__), "..", "assets", "next.png")
    ).subsample(2)
    self.forward_icon = tk.PhotoImage(
      file = os.path.join(os.path.dirname(__file__), "..", "assets", "fastForward.png")
    ).subsample(2)

    #grid
    self.columnconfigure((0,1,2,3,4), weight = 1)
    self.rowconfigure(0, weight = 1)
    #bouton <<
    self.beginning_button = ctk.CTkButton(
      self, 
      text = "", image = self.rewind_icon,
    )
    self.beginning_button.grid(
      row = 0, column = 0, padx = 10
    )
    
    #bouton <
    self.back_button = ctk.CTkButton(
      self,
      text = "", image = self.previous_icon,
    )
    self.back_button.grid(
      row = 0, column = 1, padx = 10
    )
    
    #bouton >
    self.forward_button = ctk.CTkButton(
      self,
      text = "", image = self.next_icon,
      command = self.parent.increment_count
    )
    self.forward_button.grid(
      row = 0, column = 2, padx = 10
    )
    
    #bouton >>
    self.end_button = ctk.CTkButton(
      self,
      text = "", image = self.forward_icon,

    )
    self.end_button.grid(
      row = 0, column = 3, padx = 10
    )

    #toggle état/mouvement
    self.display_toggle = ctk.CTkButton(
      self, text = "Mouvements", 
      padx = 100,
      text_font = font.Font(size = 40),
      command = self.toggle_display
    )
    self.display_toggle.grid(row = 0, column = 4, sticky = ctk.E)

  
  def toggle_display(self):
    self.parent.move_display = not self.parent.move_display
    self.parent.update_display()

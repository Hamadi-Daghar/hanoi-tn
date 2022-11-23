import os
import tkinter as tk
import tkinter.font as font

import customtkinter as ctk

from hanoi.logic.state import State
# from hanoi.app import App

class BottomFrame(ctk.CTkFrame):

  def __init__(self, parent, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)

    self.parent = parent
    # self.speed_var = speed_var

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
      command = self.start_state
    )
    self.beginning_button.grid(
      row = 0, column = 0, padx = 10
    )
    
    #bouton <
    self.back_button = ctk.CTkButton(
      self,
      text = "", image = self.previous_icon,
      command = lambda: self.increment_state(-State.speed)
    )
    self.back_button.grid(
      row = 0, column = 1, padx = 10
    )
    
    #bouton >
    self.forward_button = ctk.CTkButton(
      self,
      text = "", image = self.next_icon,
      command = lambda: self.increment_state(State.speed)
    )
    self.forward_button.grid(
      row = 0, column = 2, padx = 10
    )
    
    #bouton >>
    self.end_button = ctk.CTkButton(
      self,
      text = "", image = self.forward_icon,
      command = self.end_state
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

  
  def increment_state(self, increment:int):
    State.increment_state(increment)
    self.parent.update_display()

  def start_state(self):
    State.start_state()
    self.parent.update_display()

  def end_state(self):
    State.end_state()
    self.parent.update_display()

  def toggle_display(self):
    State.move_display = not State.move_display
    self.parent.update_display()

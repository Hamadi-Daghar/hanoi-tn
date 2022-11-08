import os
import tkinter as tk
import tkinter.font as font

import customtkinter as ctk

import hanoi.logic.state as state
# from hanoi.app import App

class BottomFrame(ctk.CTkFrame):

  def __init__(self, parent, speed_var, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)

    self.parent = parent
    self.speed_var = speed_var

    self.rewind_icon = tk.PhotoImage(
      file = os.path.join(os.path.dirname(__file__), "..", "assets", "rewind.png")
    )
    self.previous_icon = tk.PhotoImage(
      file = os.path.join(os.path.dirname(__file__), "..", "assets", "previous.png")
    )
    self.next_icon = tk.PhotoImage(
      file = os.path.join(os.path.dirname(__file__), "..", "assets", "next.png")
    )
    self.forward_icon = tk.PhotoImage(
      file = os.path.join(os.path.dirname(__file__), "..", "assets", "fastForward.png")
    )

    #grid
    self.columnconfigure((0,1,2,3,4), weight = 1)
    self.rowconfigure(0, weight = 1)

    #bouton <<
    self.beginning_button = ctk.CTkButton(
      self, 
      text = "", image = self.rewind_icon,
      # padx = 15, pady = 15,
      # text_font = font.Font(size = 30)
      command = self.start_state
    )
    self.beginning_button.grid(
      row = 0, column = 0, padx = 25
    )
    
    #bouton <
    self.back_button = ctk.CTkButton(
      self,
      text = "", image = self.previous_icon,
      # padx = 15, pady = 15,
      # text_font = font.Font(size = 30)
      command = lambda: self.increment_state(-self.speed_var.get())
    )
    self.back_button.grid(
      row = 0, column = 1, padx = 25
    )
    
    #bouton >
    self.forward_button = ctk.CTkButton(
      self,
      text = "", image = self.next_icon,
      # padx = 15, pady = 15,
      # text_font = font.Font(size = 30),
      # command = self.parent.increment_count
      command = lambda: self.increment_state(self.speed_var.get())
    )
    self.forward_button.grid(
      row = 0, column = 2, padx = 25
    )
    
    #bouton >>
    self.end_button = ctk.CTkButton(
      self,
      text = "", image = self.forward_icon,
      # padx = 15, pady = 15,
      # text_font = font.Font(size = 30)
      command = self.end_state
    )
    self.end_button.grid(
      row = 0, column = 3, padx = 25
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
    state.State.increment_state(increment)
    self.parent.update_display()

  def start_state(self):
    state.State.start_state()
    self.parent.update_display()

  def end_state(self):
    state.State.end_state()
    self.parent.update_display()

  def toggle_display(self):
    self.parent.move_display = not self.parent.move_display
    self.parent.update_display()

import os
import tkinter as tk
import tkinter.font as font

import customtkinter as ctk

import hanoi.logic.state as state

class AutoFrame(ctk.CTkFrame):

  def __init__(self, parent, speed_var, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)

    #grid
    self.columnconfigure(0, weight = 1)
    self.columnconfigure(1, weight = 3)
    self.rowconfigure((0,1,2,3,4), weight = 1)

    self.parent = parent
    self.speed_var = speed_var
    self.auto_mode = False
     
    self.steps = { #speed : (delay, step)
      1 : (1000, 1),
      10 : (100, 1),
      100 : (100, 10),
      1000 : (100, 100)
    }

    self.play_icon = tk.PhotoImage(
      file = os.path.join(os.path.dirname(__file__), "..", "assets", "right.png")
    )

    #titre
    self.title = ctk.CTkLabel(
      self, text = "Auto", 
      text_font = font.Font(size = 30, weight = "bold")
    )
    self.title.grid(
      column = 0, row = 0, columnspan = 2,
      pady = 10, sticky = ctk.W
    )


    self.auto_button = ctk.CTkButton(
      self, 
      image = self.play_icon, 
      text = "Lancer", text_font = font.Font(size = 25),
      command = self.toggle_auto
    )
    self.auto_button.grid(
      column = 0, row = 1, columnspan = 2,
      ipadx = 15, 
      pady = 20
    )


    self.speed_readout = ctk.CTkLabel(
      self, 
      textvariable = self.speed_var,
      text_font = font.Font(size = 35)
    )
    self.speed_readout.grid(
      column = 0, row = 2
    )

    self.speed_unit = ctk.CTkLabel(
      self, text = "mouvement/s",
      text_font = font.Font(size = 25)
    )
    self.speed_unit.grid(
      column = 1, row = 2
    )

    self.speed_slider = ctk.CTkSlider(
      self,
      width = 400, height = 40,
      from_ = 0, to = 3, number_of_steps = 3,
      command = self.update_speed
    )
    self.speed_slider.set(0)
    self.speed_slider.grid(
      column = 0, row = 3, columnspan = 2
    )
  

  def update_speed(self, value):
    self.speed_var.set(int(10**value))
    self.parent.parent.update_display()

  def toggle_auto(self):
    self.auto_mode = not self.auto_mode
    self.auto_button.configure(text = "Arrêter" if self.auto_mode else "Lancer")
    #TODO : toggle icon
    if self.auto_mode is True:
      self.auto_run()

  def auto_run(self):
    speed:int = self.speed_var.get()
    if self.auto_mode:
      state.State.increment_state(self.steps[speed][1])
      self.parent.parent.update_display()
      if state.State.is_end_state():
        self.toggle_auto()
      else:
        self.after(self.steps[speed][0], self.auto_run)
        #self.after(1000, self.auto_run)
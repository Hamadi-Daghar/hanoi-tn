import os
import tkinter as tk
import tkinter.font as font

import customtkinter as ctk

import hanoi.app as app

import hanoi.interface.auto_frame as auto_frame
import hanoi.interface.fil_rouge_frame as fil_rouge_frame
import hanoi.interface.info_frame as info_frame

class RightFrame(ctk.CTkFrame):

  def __init__(self, parent, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)

    self.columnconfigure((0,1), weight = 1)
    self.rowconfigure((0,1,2,3), weight = 1)

    self.parent = parent
    self.fullscreen = True
    self.colors = parent.colors
    self.fontPolicy = parent.fontPolicy

    self.cross_icon = tk.PhotoImage(
      file = os.path.join(os.path.dirname(__file__), "..", "assets", "cross.png"),
    ).subsample(3)
    self.larger_icon = tk.PhotoImage(
      file = os.path.join(os.path.dirname(__file__), "..", "assets", "larger.png"),
    ).subsample(3)
    self.smaller_icon = tk.PhotoImage(
      file = os.path.join(os.path.dirname(__file__), "..", "assets", "smaller.png"),
    ).subsample(3)

    #Boutons fenêtre

    self.window_button = ctk.CTkButton(
      self, text = "",
      corner_radius = 15,
      fg_color = self.colors.get("cyan"),
      hover_color = self.colors.get("darkCyan"),
      image = self.smaller_icon,
      command = self.toggle_window
    )
    self.window_button.grid(
      column = 0, row = 0, 
      sticky = ctk.E + ctk.N, 
      padx = 15, pady = 10
    )

    self.quit_button = ctk.CTkButton(
      self, text = "",
      corner_radius = 15,
      fg_color = self.colors.get("red"),
      hover_color = self.colors.get("darkRed"),
      image = self.cross_icon,
      command = exit
    )
    self.quit_button.grid(
      column = 1, row = 0,
      sticky = ctk.W + ctk.N, 
      padx = 15, pady = 10
    )

    #Info frame

    self.info_frame = info_frame.InfoFrame(self, fg_color = self.colors.get("grey"))
    self.info_frame.stage()

    #Frame dépendant du mode

    #Mode Démo

    self.auto_frame = auto_frame.AutoFrame(self, fg_color = self.colors.get("grey"))

    #Mode Fil rouge

    self.fil_rouge_frame = fil_rouge_frame.FilRougeFrame(self, fg_color = self.colors.get("grey"))
    

    #Switch mode

    ####################
    self.mode_switch = ctk.CTkButton(
      self, text = "Fil Rouge",
      text_font = font.Font(size = 30),
      text_color = self.colors.get("darkBlue"),
      command = self.parent.switch_view
    )
    self.mode_switch.grid(
      column = 0, row = 3, 
      columnspan = 2,
      pady = 50,
      sticky = ctk.S
    )
    ####################

    self.demo_view()



  
  def toggle_window(self):
    if self.fullscreen == True:
      self.parent.attributes("-fullscreen", False)
      self.window_button.configure(image = self.larger_icon)
    else:
      self.parent.attributes("-fullscreen", True)
      self.window_button.configure(image = self.smaller_icon)
    self.fullscreen = not self.fullscreen
  
  def demo_view(self)-> None: 
    """Passe à la vue du mode Démo.
    """
    self.fil_rouge_frame.grid_forget()
    self.auto_frame.stage()
    self.mode_switch.configure(text = "Fil Rouge")
  
  def fil_rouge_view(self)-> None:
    """Passe à la vue du mode Fil Rouge.
    """
    self.auto_frame.grid_forget()
    self.fil_rouge_frame.stage()
    self.mode_switch.configure(text = "Démo")
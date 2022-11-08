import tkinter as tk
import customtkinter as ctk
import tkinter.font as font
import os

from hanoi.interface import info_frame, auto_frame, fil_rouge_frame

class RightFrame(ctk.CTkFrame):

  def __init__(self, parent, speed_var, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)

    self.columnconfigure((0,1), weight = 1)
    self.rowconfigure(0, weight = 1)
    self.rowconfigure((1,2,3), weight = 5)

    self.parent = parent
    self.fullscreen = True

    self.cross_icon = tk.PhotoImage(
      file = os.path.join(os.path.dirname(__file__), "..", "assets", "cross.png"),
    ).subsample(3)
    self.larger_icon = tk.PhotoImage(
      file = os.path.join(os.path.dirname(__file__), "..", "assets", "larger.png"),
    ).subsample(3)
    self.smaller_icon = tk.PhotoImage(
      file = os.path.join(os.path.dirname(__file__), "..", "assets", "smaller.png"),
    ).subsample(3)


    self.window_button = ctk.CTkButton(
      self, text = "",
      corner_radius = 15,
      fg_color = "#00FFFF",
      hover_color = "#40E0D0",
      image = self.smaller_icon,
      command = self.toggle_window
    )
    self.window_button.grid(
      column = 0, row = 0, 
      sticky = ctk.E, padx = 5 
    )

    self.quit_button = ctk.CTkButton(
      self, text = "",
      corner_radius = 15,
      fg_color = "#DC143C",
      hover_color = "#B22222",
      image = self.cross_icon,
      command = exit
    )
    self.quit_button.grid(
      column = 1, row = 0,
      sticky = ctk.W, padx = 5
    )

    self.info_frame = info_frame.InfoFrame(self, fg_color = "#EBEBEC")
    self.info_frame.grid(
      column = 0, row = 1, columnspan = 2,
      sticky = ctk.N + ctk.EW
    )

    self.auto_frame = auto_frame.AutoFrame(self, speed_var, fg_color = "#EBEBEC")
    self.auto_frame.grid(
      column = 0, row = 2, columnspan = 2,
      sticky = ctk.EW
    )

    self.fil_rouge_frame = fil_rouge_frame.FilRougeFrame(self, fg_color = "#EBEBEC")
    self.fil_rouge_frame.grid(
      column = 0, row = 3, columnspan = 2,
      sticky = ctk.EW
    )
  
  def toggle_window(self):
    if self.fullscreen == True:
      self.parent.attributes("-fullscreen", False)
      self.window_button.configure(image = self.larger_icon)
    else:
      self.parent.attributes("-fullscreen", True)
      self.window_button.configure(image = self.smaller_icon)
    self.fullscreen = not self.fullscreen
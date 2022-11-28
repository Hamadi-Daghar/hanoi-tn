import customtkinter as ctk

import hanoi.interface.bottom_frame as bottom_frame
import hanoi.interface.fil_control_frame as fil_control_frame
import hanoi.interface.hanoi_canvas as  hanoi_canvas
import hanoi.interface.right_frame as right_frame 
from hanoi.logic.state import State

class App(ctk.CTk):
  
  def __init__(self):
    super().__init__()

    self.title("Hanoi mockup")
    self.geometry("1920x1080")
    self.resizable(False, False)
    self.attributes("-fullscreen", True)

    self.colors = {
      "blueHover": "#117DBD",
      "lightBlue": "#95D1F5",
      "darkBlue": "#1A182D",
      "darkCyan": "#40E0D0",
      "darkRed": "#B22222",
      "yellow": "#F9BB12",
      "white": "#FFFFFF",
      "green": "#00A19A",
      "grey": "#EBEBEC",
      "cyan": "#00FFFF",
      "blue": "#24A1EB",
      "red": "#DC143C"
    }

    self.fontPolicy = "Poppins"

    self.fg_color = self.colors.get("grey")
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("dark-blue")

    #grid
    self.columnconfigure(0, weight = 0)
    self.columnconfigure(1, weight = 1)
    self.rowconfigure(0, weight = 0)
    self.rowconfigure(1, weight = 1)

    #canvas
    self.canvas = hanoi_canvas.HanoiCanvas(self, width = 1500, height = 950, bg = "#ffffff", cursor = "circle")
    self.canvas.grid(column = 0, row = 0, sticky = ctk.NSEW)

    #bottom frame
    
    self.bottom_frame = bottom_frame.BottomFrame(self, fg_color = self.colors.get("grey"))

    self.fil_control_frame = fil_control_frame.FilControlFrame(self, fg_color = self.colors.get("grey"))

    #right frame
    self.right_frame = right_frame.RightFrame(self, fg_color = self.colors.get("grey"))
    self.right_frame.grid(
      column = 1, row = 0, rowspan = 2, sticky = ctk.NSEW
    )

    
    self.demo_view()
    self.update_display()
    
  
  def update_display(self):
    self.right_frame.info_frame.update_display()
    self.bottom_frame.display_toggle.configure(
      text = ("États" if (State.move_display) else "Mouvements")
    )
    self.canvas.update_display()
  
  def demo_view(self):
    self.fil_control_frame.grid_forget()
    self.bottom_frame.stage()

    self.right_frame.demo_view()

    State.mode = "demo"
  
  def fil_rouge_view(self):
    self.bottom_frame.grid_forget()
    self.fil_control_frame.stage()

    self.right_frame.fil_rouge_view()

    State.mode = "fil rouge"
  
  def switch_view(self):
    if State.mode == "demo":
      self.fil_rouge_view()
    else:
      self.demo_view()
import customtkinter as ctk

from hanoi.interface import bottom_frame, right_frame, hanoi_canvas

class App(ctk.CTk):
  
  def __init__(self):
    super().__init__()

    self.title("Hanoi mockup")
    self.geometry("1920x1080")
    self.resizable(False, False)
    #self.attributes("-fullscreen", True)

    self.fg_color = "#EBEBEC"
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("dark-blue")
    
    self.count = 0
    self.move_display = False
    self.speed_var = ctk.IntVar(self, value = 1)

    #grid
    self.columnconfigure(0, weight = 0)
    self.columnconfigure(1, weight = 1)
    self.rowconfigure(0, weight = 0)
    self.rowconfigure(1, weight = 1)

    #canvas
    self.canvas = hanoi_canvas.HanoiCanvas(self)
    self.canvas.grid(column = 0, row = 0, sticky = ctk.NSEW)

    #bottom frame
    self.bottom_frame = bottom_frame.BottomFrame(self, fg_color = "#EBEBEC")
    self.bottom_frame.grid(
      column = 0, row = 1, 
      padx = 88, pady = 10
    )
    
    #right frame
    self.right_frame = right_frame.RightFrame(self, self.speed_var, fg_color = "#EBEBEC")
    self.right_frame.grid(
      column = 1, row = 0, rowspan = 2, sticky = ctk.NSEW
    )
    
    self.update_display()
    
  
  def update_display(self):
    self.right_frame.info_frame.update_display(self.count, self.move_display)
    self.bottom_frame.display_toggle.configure(
      text = ("États" if (self.move_display) else "Mouvements")
    )
  
  def increment_count(self):
    self.count += 1
    self.update_display()


# if __name__ == "__main__":
#   app = App()
#   app.mainloop()
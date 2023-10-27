import tkinter as tk;
# import function from TK
root = tk.Tk()
# set TK window size 
root.geometry("600x600")

fram = tk.Frame()
# set title of frame
fram.master.title("PNC UI GAME")
cavas = tk.Canvas(fram)
cavas.create_oval(160,160,440,440, fill= "#0000ff")
cavas.create_oval(190,190,410,410, fill= "#ff0000")
cavas.create_oval(220,220,380,380, fill= "#00ff00")
cavas.create_oval(250,250,350,350, fill= "#ffff00")
cavas.create_oval(280,280,320,320, fill= "#00ff00")





# to display all frame
cavas.pack(expand=True, fill='both')
fram.pack(expand=True, fill="both")
root.mainloop()
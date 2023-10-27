# import tkinter as tk;
# # import function from TK
# root = tk.Tk()
# # set TK window size 
# root.geometry("600x600")

# fram = tk.Frame()
# # set title of frame
# fram.master.title("PNC UI GAME")
# cavas = tk.Canvas(fram)
# cavas.create_rectangle(160,160,440,440, fill= "#0000ff")
# cavas.create_rectangle(190,190,410,410, fill= "#ff0000")
# cavas.create_rectangle(220,220,380,380, fill= "#00ff00")
# cavas.create_rectangle(250,250,350,350, fill= "#ffff00")
# cavas.create_rectangle(280,280,320,320, fill= "#00ff00")




# # to display all frame
# cavas.pack(expand=True, fill='both')
# fram.pack(expand=True, fill="both")
# root.mainloop()



# -------------------------

import tkinter as tk;
import random
# import function from TK
root = tk.Tk()
# set TK window size 
root.geometry("600x600")

fram = tk.Frame()
# set title of frame
fram.master.title("PNC UI GAME")
cavas = tk.Canvas(fram)
colors = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 'purple']
x1= 160
y1= 160
x2=440
y2=440
for i in range(5):
    cavas.create_rectangle(x1,y1,x2,y2, fill= random.choice(colors))
    x1+=30
    y1+=30
    x2-=30
    y2-=30








# to display all frame
cavas.pack(expand=True, fill='both')
fram.pack(expand=True, fill="both")
root.mainloop()


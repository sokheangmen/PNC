# import random
# import tkinter as tk

# # Create an empty window
# root = tk.Tk() 
# # Set TK window size to width 600 px and height 200 px
# root.geometry("610x610")
# # Create a frame in the window (frame is a container, like "div" in HTML)
# frame = tk.Frame() 
# # Set the title of the frame
# frame.master.title("Hello PNC")
# canvas = tk.Canvas(frame)



# points=[]
# colors=['#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6', 
#       '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D',
#       '#80B300', '#809900', '#E6B3B3', '#6680B3', '#66991A', 
#       '#FF99E6', '#CCFF1A', '#FF1A66', '#E6331A', '#33FFCC',
#       '#66994D', '#B366CC', '#4D8000', '#B33300', '#CC80CC', 
#       '#66664D', '#991AFF', '#E666FF', '#4DB3FF', '#1AB399',
#       '#E666B3', '#33991A', '#CC9999', '#B3B31A', '#00E680', 
#       '#4D8066', '#809980', '#E6FF80', '#1AFF33', '#999933',
#       '#FF3380', '#CCCC00', '#66E64D', '#4D80CC', '#9900B3', 
#       '#E64D66', '#4DB380', '#FF4D4D', '#99E6E6', '#6666FF']
# def drawCircle(event):
#     canvas.delete("all")
#     points.append(event.x)
#     points.append(event.y)
#     canvas.create_oval(event.x-1,event.y-1,(event.x)+1,(event.y)+1,fill="",outline="black")
#     print("print from draw circle function",points)

# def drawShape(event):
#     global points
#     canvas.create_polygon(points,fill=colors[random.randrange(0,len(colors)-1)])
#     points=[]
# root.bind("<Button-1>", drawCircle) #LEFT CLICK
# root.bind("<Button-3>", drawShape) #RIGHT CLICK

# canvas.pack(expand=True, fill='both')
# frame.pack(expand=True, fill='both')

# root.mainloop()



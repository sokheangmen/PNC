from tkinter import  BOTH, Tk, Canvas, mainloop

### VARIABLES
WIDTH = 900
HEIGHT = 600
VOLOCITY =  {
    1: {
        "xVolocity": 4,
        "yVolocity": 4
    },
    2: {
        "xVolocity": 5,
        "yVolocity": 4
    },
    3: {
        "xVolocity": 3,
        "yVolocity": 5
    },
    4: {
        "xVolocity": 3,
        "yVolocity": 4
    },
    5: {
        "xVolocity": 3,
        "yVolocity": 4
    },
    6: {
        "xVolocity": 3,
        "yVolocity": 4
    }
}

ballSIze = 40

### FUNCTION
def moveBall(canvasBall, xVolocity, yVolocity):
    ### CONDITIONS
    if shape.coords(canvasBall)[0] > WIDTH-ballSIze:
        xVolocity = -xVolocity
    elif shape.coords(canvasBall)[0] < 0:
        xVolocity = -1*xVolocity
    elif shape.coords(canvasBall)[1] > HEIGHT-ballSIze:
        yVolocity = -yVolocity
    elif shape.coords(canvasBall)[1] < 0:
        yVolocity = -1*yVolocity

    ### START THE ANIMATION
    shape.move(canvasBall, xVolocity, yVolocity)
    shape.after(10, lambda:moveBall(canvasBall, xVolocity, yVolocity))

    ### PRINT THE COORDINATION TO TERMINAL
    # print(shape.coords(canvasBall)[0], shape.coords(canvasBall)[2])


### MAIN WINDOW
root = Tk()
root.geometry(str(WIDTH)+"x"+str(HEIGHT))
root.resizable(0,0)

### CANVAS
shape = Canvas(root, background="grey")
ballOne = shape.create_oval(0, 0, ballSIze, ballSIze, fill="red")
ballTwo = shape.create_oval(100, 100, 100+ballSIze, 100+ballSIze, fill="black")
ballThree = shape.create_oval(150, 100, 150+ballSIze, 100+ballSIze, fill="cyan")
ballFour1 = shape.create_oval(150, 90, 150+ballSIze, 90+ballSIze, fill="yellow")
ballFour2 = shape.create_oval(150, 150, 150+ballSIze, 150+ballSIze, fill="navy")
ballFour3 = shape.create_oval(150, 200, 150+ballSIze, 250+ballSIze, fill="orange")
shape.pack(expand=True, fill=BOTH)

listOfBall = [ballOne, ballTwo, ballThree, ballFour1,ballFour2,ballFour3]

### CALLS FUNCTIONS
for i in listOfBall:
     moveBall(i, VOLOCITY[i]["xVolocity"], VOLOCITY[i]["yVolocity"])

root.mainloop()  
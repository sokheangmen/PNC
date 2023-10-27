from cgitb import text
import tkinter as tk

# ---------------------------------------------------------------------------
# Global data
# ---------------------------------------------------------------------------
score = 0
# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------

def onClickOnAdd(event) :
    global score
    setScore(score+2)
    if score==100:
        score=0

def onClickOnMultiply(event) :
    global score
    setScore(score*2)
    if score>100:
        score=0
   

def onClickOnDivide(event) :
    setScore(score/2)


def onClickOnReset(event) :
    setScore(0)

def setScore(newScore):
    global score
    score=newScore
    canvas.itemconfig(scoreLabel,text=score)
# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
root = tk.Tk()
root.geometry("600x500")
canvas = tk.Canvas(root)

# Create the score label
scoreLabel = canvas.create_text(300, 50, text=score, font=('consolas', 50, 'bold') ,fill="navy")

# Create the reset label

minusLabel = canvas.create_text(300, 150, text='RESET', tags="resetLabel", font=('consolas', 24, 'bold'))
canvas.tag_bind("resetLabel","<Button-1>", onClickOnReset)


# Create the Multiply label
minusLabel = canvas.create_text(400, 150, text='x2', tags="multiplyLabel", font=('consolas', 24, 'bold'))
canvas.tag_bind("multiplyLabel","<Button-1>", onClickOnMultiply)

# Create the Divide label
addLabel = canvas.create_text(200, 150, text='/2', tags="divideLabel", font=('consolas', 24, 'bold'))
canvas.tag_bind("divideLabel","<Button-1>", onClickOnDivide)

# Create the add label
addLabel = canvas.create_text(300, 210, text='+2', tags="addLabel", font=('consolas', 24, 'bold'))
canvas.tag_bind("addLabel","<Button-1>", onClickOnAdd)


canvas.pack(expand=True, fill='both')
root.mainloop()



# TIP2     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
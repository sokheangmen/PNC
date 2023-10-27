# from random import shuffle
# students = ["Chanthy","Buthourn","Sreyleak","Nika"]
# shuffle(students)
# print(students)

# # or-------------------
# import random
# students = ["Chanthy","Buthourn","Sreyleak","Nika"]
# random.shuffle(students)
# print(students)

# =============================

# import random
# for i in range(3):
#     print("Number"+str(i+1)+": "+str(random.randrange(0, 100)))



# --------------------
# import random
# studentsList = ["SARETH","SEAVY","RATHTEKA","SREYHON","VANTHORN","SOK","TOUN","SREYTOUCH","CHAINY","SOM","SIMENG","NHORK","SREYNOT","THIN","SEANGHAY","LYHUOY","SOPHANNA","NIMOUT","VOULEAK","CHET","SINY","SOTHEAN","SOPHORN","SREYHIEB","MENGHOUR","NISAI","CHANTHEA","PHEARAK","SOMOUN","SREYNICH","SAOLEE","RIN","ON","SOPHANNA","CHANTHY","MOLIKA","BUNSAL","SOKTHANG","DYNA","SARA","VOUCHLY","SOTHOUN","LYDEN","MONYRA","VUN","LANH","PHALLY","SREYPICH","SENGHIM","DAVY","CHUM","LYHEANG","KOEMSAK","VICHEKA","LAMYAI","CHANTHOU","KUNTHY","SOPHEA","VANTHEAV","SOPHEAK","NARATH","SREYNGIT","MENGHEANG","VUTHY","CHANRY","CHANNARY","LYHOR","THALY","HOUTCHHAY","SOMPHORS","SINET","SREY AEM","THON","PROS"]
# name = input("What is your name ?")
# print(name +" secret lover is "+str(random.choice(studentsList)))

# ------------------------------

import tkinter as tk;
# import function from TK
root = tk.Tk()
# set TK window size 
root.geometry("300x150")

fram = tk.Frame()
# set title of frame
fram.master.title("Sarath2022")
cavas = tk.Canvas(fram)
cavas.create_rectangle(10,20,50,100, fill= "#ff0000")


# to display all frame
cavas.pack(expand=True, fill='both')
fram.pack(expand=True, fill="both")
root.mainloop()
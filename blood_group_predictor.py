import tkinter as ttk
from tkinter import *
import random
import tk
root = Tk()
 
root.geometry("1000x600")

root.title("BLOOD GROUP TYPE PREDICTOR")
 

computer_value = {
    "0":"A+",
    "1":"B+",
    "2":"AB+",
    "3":"O+",
    "4":"A-",
    "6":"B-",
    "7":"AB-",
    "8":"O-"
}
 

def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    b4["state"] = "active"
    b5["state"] = "active"
    b6["state"] = "active"
    b7["state"] = "active"
    b8["state"] = "active"
  
    l1.config(text = "Mother's blood group              ")
    l3.config(text = "Father's blood group")
    l4.config(text = "")
 

def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"
    b4["state"] = "disable"
    b5["state"] = "disable"
    b6["state"] = "disable"
    b7["state"] = "disable"
    b8["state"] = "disable"

def A_positive():
    
    c_v = computer_value[str(random.randint(0,8))]
    if c_v=='A+' :
        match_result="(A -> 93.75% , O -> 6.25%,(+) or (-))"
    elif c_v=='B+':
        match_result="(A -> 18.75% , B -> 18.75% , AB -> 56.25% , O ->6.25%,(+) or (-))"
    elif c_v=='AB+' :
        match_result="(A -> 50% , B -> 12.50% , AB -> 37.50% ,(+) or (-))"
    elif c_v=='O+' :
        match_result= "(A -> 75% , O -> 25%,(+) or (-))"
    elif c_v=='A-' :
        match_result="(A -> 93.75% , O -> 6.25%(+) or (-))"
    elif c_v=='B-':
        match_result="(A -> 18.75% , B -> 18.75% , AB -> 56.25% , O ->6.25%,(+) or (-))"
    elif c_v=='AB-' :
        match_result="(A -> 50% , B -> 12.50% , AB -> 37.50% ,(+) or (-))"
    elif c_v=='O-' :
        match_result= "(A -> 75% , O -> 25%,(+) or (-))"
    l4.config(text = match_result)
    l1.config(text = "A+            ")
    l3.config(text = c_v)
    button_disable()

 
def B_positive():
    c_v = computer_value[str(random.randint(0,8))]
    if c_v=='A+' :
        match_result=("A -> 18.75% ,B -> 18.75%,AB ->56.25%, O -> 6.25%,(+) or (-)")
    elif c_v=='B+' :
        match_result=(" B -> 93.75% , O ->6.25%,(+) or (-)")
    elif c_v=='AB+' :
        match_result=("A -> 50% , B -> 12.50% , AB -> 37.50% ,(+) or (-)")
    elif c_v=='O+' :
        match_result=("A -> 75% , O -> 25%,(+) or (-)")
    elif c_v=='A-' :
        match_result=("A -> 18.75% ,B -> 18.75%,AB ->56.25%, O -> 6.25%,(+) or (-)")
    elif c_v=='B-' :
        match_result=(" B -> 93.75% , O ->6.25%,(+) or (-)")
    elif c_v=='AB-' :
        match_result=("A -> 50% , B -> 12.50% , AB -> 37.50% ,(+) or (-)")
    elif c_v=='O-' :
        match_result=("A -> 75% , O -> 25%,(+) or (-)")
    
    l4.config(text = match_result)
    l1.config(text = "B+            ")
    l3.config(text = c_v)
    button_disable()


def AB_positive():
    f = computer_value[str(random.randint(0,8))]
    if f=='A+' :
        match_result=("A -> 50% ,B -> 12.50% ,AB -> 37.50%,(+) or (-)")
    elif f=='B+' :
        match_result=("A -> 50% , B -> 12.50% , AB -> 37.50% ,(+) or (-)")
    elif f=='AB+' :
        match_result=("A -> 25% , B -> 25% , AB -> 50% ,(+) or (-)")
    elif f=='O+' :
        match_result=("A -> 50% , O -> 50%,(+) or (-)")  
    elif f=='A-' :
        match_result=("A -> 50% ,B -> 12.50% ,AB -> 37.50%,(+) or (-)")
    elif f=='B-' :
        match_result=("A -> 50% , B -> 12.50% , AB -> 37.50% ,(+) or (-)")
    elif f=='AB-' :
        match_result=("A -> 25% , B -> 25% , AB -> 50% ,(+) or (-)")
    elif f=='O-' :
        match_result=("A -> 50% , O -> 50%,(+) or (-)")  
    l4.config(text = match_result)
    l1.config(text = "AB+            ")
    l3.config(text = f)
    button_disable() 

def O_positive():
    f = computer_value[str(random.randint(0,8))]
    if f=='A+':
        match_result=("A -> 75% , O -> 25%,(+) or (-)")
    elif f=='B+':
        match_result=(" B -> 75% , O ->25%,(+) or (-)")
    elif f=='AB+' :
        match_result=("A -> 50% , B -> 50%  ,(+) or (-)")
    elif f=='O+' :
        match_result=(" O -> 100%,(+) or (-)")
    elif f=='A-':
        match_result=("A -> 75% , O -> 25%,(+) or (-)")
    elif f=='B-':
        match_result=(" B -> 75% , O ->25%,(+) or (-)")
    elif f=='AB-' :
        match_result=("A -> 50% , B -> 50%  ,(+) or (-)")
    elif f=='O-' :
        match_result=(" O -> 100%,(+) or (-)")
    l4.config(text = match_result)
    l1.config(text = "O+            ")
    l3.config(text = f)
    button_disable() 



def A_negative():
    
    c_v = computer_value[str(random.randint(0,8))]
    if c_v=='A+' :
        match_result="(A -> 93.75% , O -> 6.25%,(+) or (-))"
    elif c_v=='B+':
        match_result="(A -> 18.75% , B -> 18.75% , AB -> 56.25% , O ->6.25%,(+) or (-))"
    elif c_v=='AB+' :
        match_result="(A -> 50% , B -> 12.50% , AB -> 37.50% ,(+) or (-))"
    elif c_v=='O+' :
        match_result= "(A -> 75% , O -> 25%,(+) or (-))"
    elif c_v=='A-' :
        match_result="(A -> 93.75% , O -> 6.25%, (-))"
    elif c_v=='B-':
        match_result="(A -> 18.75% , B -> 18.75% , AB -> 56.25% , O ->6.25%, (-))"
    elif c_v=='AB+' :
        match_result="(A -> 50% , B -> 12.50% , AB -> 37.50% ,(-))"
    elif c_v=='O-' :
        match_result= "(A -> 75% , O -> 25%, (-))"
    l4.config(text = match_result)
    l1.config(text = "A-            ")
    l3.config(text = c_v)
    button_disable()

 
def B_negative():
    c_v = computer_value[str(random.randint(0,8))]
    if c_v=='A+' :
        match_result=("A -> 18.75% ,B -> 18.75%,AB ->56.25%, O -> 6.25%,(+) or (-)")
    elif c_v=='B+' :
        match_result=(" B -> 93.75% , O ->6.25%,(+) or (-)")
    elif c_v=='AB+' :
        match_result=("A -> 50% , B -> 12.50% , AB -> 37.50% ,(+) or (-)")
    elif c_v=='O+' :
        match_result=("A -> 75% , O -> 25%,(+) or (-)")
    elif c_v=='A-' :
        match_result=("A -> 18.75% ,B -> 18.75%,AB ->56.25%, O -> 6.25%, (-)")
    elif c_v=='B-' :
        match_result=(" B -> 93.75% , O ->6.25%,(+) or (-)")
    elif c_v=='AB-' :
        match_result=("A -> 50% , B -> 12.50% , AB -> 37.50% , (-)")
    elif c_v=='O-' :
        match_result=("A -> 75% , O -> 25%, (-)")
    
    l4.config(text = match_result)
    l1.config(text = "B-            ")
    l3.config(text = c_v)
    button_disable()


def AB_negative():
    f = computer_value[str(random.randint(0,8))]
    if f=='A+' :
        match_result=("A -> 50% ,B -> 12.50% ,AB -> 37.50%,(+) or (-)")
    elif f=='B+' :
        match_result=("A -> 50% , B -> 12.50% , AB -> 37.50% ,(+) or (-)")
    elif f=='AB+' :
        match_result=("A -> 25% , B -> 25% , AB -> 50% ,(+) or (-)")
    elif f=='O+' :
        match_result=("A -> 50% , O -> 50%,(+) or (-)")  
    elif f=='A-' :
        match_result=("A -> 50% ,B -> 12.50% ,AB -> 37.50%,(-)")
    elif f=='B-' :
        match_result=("A -> 50% , B -> 12.50% , AB -> 37.50% , (-)")
    elif f=='AB-' :
        match_result=("A -> 25% , B -> 25% , AB -> 50% ,(-)")
    elif f=='O-' :
        match_result=("A -> 50% , O -> 50%, (-)")  
    l4.config(text = match_result)
    l1.config(text = "AB-            ")
    l3.config(text = f)
    button_disable() 

def O_negative():
    f = computer_value[str(random.randint(0,8))]
    if f=='A+':
        match_result=("A -> 75% , O -> 25%,(+)  or (-)")
    elif f=='B+':
        match_result=(" B -> 75% , O ->25%,(+) or (-)")
    elif f=='AB+' :
        match_result=("A -> 50% , B -> 50%  ,(+) or (-)")
    elif f=='O+' :
        match_result=(" O -> 100%,(+) or (-)")
    elif f=='A-':
        match_result=("A -> 75% , O -> 25%, (-)")
    elif f=='B-':
        match_result=(" B -> 75% , O ->25%, (-)")
    elif f=='AB-' :
        match_result=("A -> 50% , B -> 50%  ,(-)")
    elif f=='O-' :
        match_result=(" O -> 100%,(-)")
    l4.config(text = match_result)
    l1.config(text = "O-            ")
    l3.config(text = f)
    button_disable() 

Label(root,
      text = "BLOOD GROUP PREDICTER",
      font = "normal 30 bold",
      fg = "black").pack(pady =40)
 

Label(root,
      text = "This is a blood group predictor,"+"\n"+"in which we have to select mother's blood group and it take random blood group for father,"+"\n" + "and based on selected blood group of mother and chosen random value for father,"+ "\n" +"it outputs the possible types of blood group of its child  ",
      font = "normal 15 ",
      fg = "red").pack(pady =20)

frame = Frame(root)
frame.pack()
 
l1 = Label(frame,
           text = "Mother's Blood Group             ",
           font = 20)
 
l2 = Label(frame,
           text = "AND           ",
           font = "normal 10 ")
 
l3 = Label(frame, text = "Father's blood Group", font = 20)
 
l1.pack(side = LEFT)
l2.pack(side = LEFT)
l3.pack()
 
 

l4 = Label(root,
           text = "Mother's Blood Group",
           font = "normal 20 bold",
           bg = "white",
           width = 50 ,
           borderwidth = 2,
           relief = "solid")
l4.pack(pady = 20)
 
frame1 = Frame(root)
frame1.pack()
 
b1 = Button(frame1, text = "A",
            font = 10, width = 7,
            command = A_positive)
 
b2 = Button(frame1, text = "B ",
            font = 10, width = 7,
            command = B_positive)
 
b3 = Button(frame1, text = "AB",
            font = 10, width = 7,
            command = AB_positive)

b4 = Button(frame1, text = "O",
            font = 10, width = 7,
            command = O_positive)


b5 = Button(frame1, text = "A- ",
            font = 10, width = 7,
            command = A_negative)
 
b6 = Button(frame1, text = "B-",
            font = 10, width = 7,
            command = B_negative)

 
b7 = Button(frame1, text = "AB-",
            font = 10, width = 7,
            command =AB_negative)
 
b8 = Button(frame1, text = "O- ",
            font = 10, width = 7,
            command = O_negative)
 
 
b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT,padx = 10)
b3.pack(side = LEFT,padx = 10)
b4.pack(side = LEFT, padx = 10)
b5.pack(side = LEFT,padx = 10)
b6.pack(side = LEFT,padx = 10)
b7.pack(side = LEFT, padx = 10)
b8.pack(padx = 10)

 
Button(root, text = "Reset",
       font = 10, fg = "red",
       bg = "black", command = reset_game).pack(pady = 20)
 
root.configure(bg='light blue')

root.mainloop()

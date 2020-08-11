#new new one here
from tkinter import *
import random
import time

score4human = 0
score4comp = 0

def computerrandom():
    global random_choose
    randomval = ["rock","paper","scissor"]
    random_choose = random.choice(randomval)
    
def deletebox1():
    box1.delete(0,END)
def deletebox2():
    box2.delete(0,END)
def deletebox3():
    box3.delete(0,END)

def result():
    global score4human,score4comp
    if score4comp == 5:
        deletebox1()
        deletebox2()
        box3.insert(1,f"You loose the game, computer beat you with {score4comp-score4human} points")
        score4comp = 0
        score4human = 0

    elif score4human == 5:
        deletebox1()
        deletebox2()
        box3.insert(1,f"You won the game, you beat computer you with {score4human-score4comp} points")
        score4comp = 0
        score4human = 0

def rock():
    deletebox3()
    global score4human,score4comp
    InpuT = "rock"
    computerrandom()

    if InpuT == "rock" and random_choose == "scissor":
        deletebox1()
        deletebox2()
        box2.insert(0,"You won computer loose")
        score4human+=1
        box2.insert(1,f"Your Point: {score4human} Computer Point: {score4comp}")
        box1.insert(0,f"YOU: {InpuT} | COMPUTER: {random_choose}")
     
    elif InpuT == "rock" and random_choose == "paper":
        deletebox1()
        deletebox2()
        box2.insert(0,"You lost , computer won")
        score4comp+=1
        box2.insert(1,f"Your Point: {score4human} Computer Point: {score4comp}")
        box1.insert(0,f"YOU: {InpuT} | COMPUTER: {random_choose}")

    elif InpuT == "rock" and random_choose == "rock":
        deletebox1()
        deletebox2()
        box2.insert(0,"Tie")
        box2.insert(1,f"Your Point: {score4human} Computer Point: {score4comp}")
        box1.insert(0,f"YOU: {InpuT} | COMPUTER: {random_choose}")
    result()

def paper():
    deletebox3()
    global score4human,score4comp

    InpuT = "paper"
    computerrandom()
    if InpuT  == "paper" and random_choose == "rock":
        deletebox1()
        deletebox2()
        box2.insert(0,"You won computer loose")
        score4human+=1
        box2.insert(1,f"Your Point: {score4human} Computer Point: {score4comp}")
        box1.insert(0,f"YOU: {InpuT} | COMPUTER: {random_choose}")

    elif InpuT == "paper" and random_choose == "scissor":
        deletebox1()
        deletebox2()
        box2.insert(0,"You lost , computer won")
        score4comp+=1
        box2.insert(1,f"Your Point: {score4human} Computer Point: {score4comp}")
        box1.insert(0,f"YOU: {InpuT} | COMPUTER: {random_choose}")

    elif InpuT == "paper" and random_choose == "paper":
        deletebox1()
        deletebox2()
        box2.insert(0,"Tie")
        box2.insert(1,f"Your Point: {score4human} Computer Point: {score4comp}")
        box1.insert(0,f"YOU: {InpuT} | COMPUTER: {random_choose}")
    result()
    
def scissor():
    deletebox3()
    global score4human,score4comp

    InpuT = "scissor"
    computerrandom()
    if InpuT == "scissor" and random_choose == "paper":
        deletebox1()
        deletebox2()
        box1.insert(0,f"YOU: {InpuT} | COMPUTER: {random_choose}")
        box2.insert(0,"You won computer loose")
        score4human+=1
        box2.insert(1,f"Your Point: {score4human} Computer Point: {score4comp}")

        
    elif InpuT == "scissor" and random_choose == "rock":
        deletebox1()
        deletebox2()
        box1.insert(0,f"YOU: {InpuT} | COMPUTER: {random_choose}")
        box2.insert(0,"You lost , computer won")
        score4comp+=1
        box2.insert(1,f"Your Point: {score4human} Computer Point: {score4comp}")

        
    elif InpuT == "scissor" and random_choose == "scissor":
        deletebox1()
        deletebox2()
        box1.insert(0,f"YOU: {InpuT} | COMPUTER: {random_choose}")
        box2.insert(0,"Tie")
    result()

root=Tk()
#size of window
root.geometry("850x700")
root.configure(bg='black')

#title
root.title("Rock Paper Scissor Game")

#heading
r1= Label(root, text= "Rock , Paper , Scissor Game!",
font= "Helvetica 20 bold underline")
r1.config(anchor=CENTER)
r1.grid(row=0,column=1,pady=5,padx=45)

#button1(ROCK)
b1=Button(root,text="Rock",
font="Constantia 15 bold",width=10,height=2,bg='Chocolate1',command=rock)
b1.grid(row=1,column=0,padx=20,pady=5)

#button2(PAPER)
b2=Button(root,text="Paper",
font="Constantia 15 bold",width=10,height=2,bg='mint cream',fg='blue2',command=paper)
b2.grid(row=2,column=0,padx=20)

#button3(SCISSOR)
b3=Button(root,text="Scissor",
font="Constantia 15 bold",width=10,height=2,bg='green2',command=scissor)
b3.grid(row=3,column=0,padx=20,pady=5)
#info for listbox1
r2=Label(root,text="Your input will be displayed here: ",
font="Constantia 15 bold underline")
r2.grid(row=1,column=1)

#listbox1(for displaying user's input)
box1=Listbox(root,width=55,height=8,font="Helvetica 12 bold")
box1.grid(row=2,column=1)

#Button for(computer's turn)
r3=Label(root,text="Computer's Turn --> ",font="Constantia 15 bold underline")
r3.config(anchor="e")
r3.grid(row=6,column=0,padx=20)

#listbox2(for computer's turn)
box2=Listbox(root,width=60,height=5,font="Helvetica 12 bold")
box2.grid(row=6,column=1)

#SCORE LABEL
o2=Label(root,text="SCORE : ",font="Constantia 15 bold")
o2.grid(row=10,column=0)

#SCORE
box3=Listbox(root,width=60,height=7,font="Helvetica 12 bold")
box3.grid(row=10,column=1,pady=40)

root.mainloop()



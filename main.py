from tkinter import * 
import random
from random import choice

window = Tk()
window.geometry("800x600")
window.title("rock paper scissors")

frame = Frame(window)
frame.place(relx = 0.01,rely=0.01,relwidth=0.98,relheight=0.98)

name = Label(frame,text="rock paper scissors - player vs computer", font=100)
name.place(x=250,y=20)

label1 = Label(frame,text="player",font="normal 15")

label2 = Label(frame,text="vs",font="normal 15")

label3 = Label(frame,text="computer",font="normal 15")

label1.place(x=80,y=50,width=100)
label2.place(x=350,y=50,width=100)
label3.place(x=600,y=50,width=100)

rock_png = PhotoImage(file = "rock.png")
scissors_png = PhotoImage(file = "scissors.png")
paper_png = PhotoImage(file = "paper.png")

user_image = Label(frame, image = "")
user_image.place(x=80,y = 100)

comp_image = Label(frame, image = "")
comp_image.place(x=600,y = 100)

def Rock():
	user = "Rock"
	computer = random.choice(["Rock","Scissors","Paper"])
	user_image.config(image=rock_png)
	if user == computer:
		label4.config(text="draw")
		comp_image.config(image=rock_png)
	elif computer == "Paper":
		label4.config(text="computer win!")
		comp_image.config(image=scissors_png)
	else:
		label4.config(text="U win!")
		comp_image.config(image=paper_png)

label4 = Label(frame, text="",font="normal 20",width = 15, borderwidth = 2,relief = "solid")
label4.place(x=275,y=250)


b1 = Button(frame, text="Rock", font= "10", width =20, command=Rock)
b1.place(x=100,y=300)

b2 = Button(frame, text="scissors", font= "10", width =20)
b2.place(x=300,y=300)

b3 = Button(frame, text="paper", font= "10", width =20)
b3.place(x=500,y=300)

window.mainloop()
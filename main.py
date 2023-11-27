"""import pygame
import random


pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Rock, Paper, Scissors")
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

choices = ["rock", "paper", "scissors"]
player_choice = None
computer_choice = None

running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
            player_choice = "rock"
	


	screen.fill((217,197,161))
	pygame.display.update()"""

from tkinter import * 
import random

window = Tk()
window.geometry("800x600")
window.title("rock paper scissors")

frame = Frame(window,bg="lightblue")
frame.place(relx = 0.01,rely=0.01,relwidth=0.98,relheight=0.98)

name = Label(frame,text="rock paper scissors - player vs computer", font=100)
name.place(x=250,y=20)

label1 = Label(frame,text="player",font="normal 15")

label2 = Label(frame,text="vs",font="normal 15")

label3 = Label(frame,text="computer",font="normal 15")

label1.place(x=80,y=50,width=100)
label1.place(x=80,y=50,width=100)
label1.place(x=80,y=50,width=100)

window.mainloop()
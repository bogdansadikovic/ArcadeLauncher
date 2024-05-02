import os
import sys
import tkinter as tk
import keyboard

root = tk.Tk()
root.configure(background = 'black') #Create a black background
root.title("Main Menu") #Title of the window

# Path: Main_menu_screen/main_menu.py
directory = "/home/gamedev/Downloads" #Directory where the games are stored --> Potentially.
files = os.listdir(directory)

# Filter for game builds with a ".exe":
game_builds = [file for file in files if file.endswith(".exe")]


game_map = {path: i for i, path in enumerate(game_builds)} #All the games are put in a map with such that the according game can be picked by number.


canvas = tk.Canvas(root, width = 500, height = 500, background = 'black') #Create the canvas for the app.
canvas.pack()

squares = [canvas.create_rectangle(i*50, 50, i*50+50, 100, fill='white') for i in range(len(game_map))] #Create a square for each game build.

selected = 0
canvas.itemconfig(squares[selected], fill = 'blue')


def key_press(event):
    global selected
    canvas.itemconfig(squares[selected], fill = 'white')
    if(event.keysym == "Right"):
        selected = (selected + 1) % len(squares)
    elif(event.keysym == "Left"):
        selected = (selected - 1) % len(squares)
    canvas.itemconfig(squares[selected], fill = 'blue')


root.bind("<Key>", key_press)
root.mainloop()




while(True):
    if(keyboard.is_pressed('right') or keyboard.is_pressed('left')):
        event = keyboard.read_key() #check which key is pressed.
        key_press(event)
    
    if(keyboard.is_pressed('enter')): #Using enter as a stand-in key for now:
        os.system(game_map[selected]) #Run the game.
        sys.exit() #End the program.



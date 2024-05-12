"""
File Name: mainwindow.py
Name: Caleb Steelman
DLM: May 12th, 2024
It creates and controlls a class to open up other windows, which allows for the functioning of the whole program.
"""
#Other classes from the sibling files are opened so the windows can be opened.
from chickenwindow import ChickenWindow
from beefwindow import BeefWindow
from porkwindow import PorkWindow
#External content is imported. Tkinter for the gui, Pillow for images.
import tkinter as tk
from PIL import ImageTk, Image
#Mainwindow class is defined, which will open up the other windows and allow the whole program to function.
class MainWindow: 
    #The main class is initialized and defined
    def __init__(self):

        #Tk is called and the mainwindow established geometry wise also.
        self.root = tk.Tk()
        self.root.title("Main Window")
        self.root.geometry("500x400")
        #The window is made unreziable, so the user must use it's intended dimensions.
        self.root.resizable(width=False, height=False)
        #The user is welcomed to the program via a message, it is stylized a little bit.
        self.label = tk.Label(self.root, text="Welcome to the the program! \nClick one of the buttons to see nutritional information: ", font=('Helvetica', 12, 'bold'))
        self.label.pack(pady=10)
        #A button is created for opening the chicken window, also stylized.
        self.button = tk.Button(self.root, text="Chicken", command=self.open_chicken_window, bg="green", font=('Helvetica', 12, 'bold'))
        self.button.pack(pady=10, fill='x', expand=True)
        #A button is created for opening the beef window, also stylized.
        self.button = tk.Button(self.root, text="Beef", command=self.open_beef_window, bg="green", font=('Helvetica', 12, 'bold'))
        self.button.pack(pady=10, fill='x', expand=True)
        #A button is created for opening the pork window, also stylized.
        self.button = tk.Button(self.root, text="Pork", command=self.open_pork_window, bg="green", font=('Helvetica', 12, 'bold'))
        self.button.pack(pady=10, fill='x', expand=True)
        #An exit button is made, and also stylized.
        self.button_exit = tk.Button(self.root, text="Exit", command=self.root.quit, bg="red", font=('Helvetica', 12, 'bold'))
        self.button_exit.pack(pady=10, fill='x', expand=True)
    #run is defined and established so that the whole thing works.
    def run(self):
        self.root.mainloop()
    #open_chicken_window is defined so that the chicken window will open.
    def open_chicken_window(self):
        self.chicken_window = ChickenWindow(self.root, self)
    #open_beef_window is defined so that the beef window will open.
    def open_beef_window(self):
        self.beef_window = BeefWindow(self.root, self)
    #open_pork_window is defined so that the pork window will open.
    def open_pork_window(self):
        self.beef_window = PorkWindow(self.root, self)


#Runs the whole program through a loop, so it will work.
MainWindow().root.mainloop()
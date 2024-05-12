"""
File Name: chickenwindow.py
Name: Caleb Steelman
DLM: May 12th, 2024
Defines and creates a class called ChickenWindow, which is used to open a window to calculate the calories, protein, and fat of chicken based on poundage.
"""
#Pillow is used to import ImageTK and image, which are both used.
from PIL import ImageTk, Image
#The class is created.
class ChickenWindow:
    #The class is defined and initialized.
    def __init__(self, master, main_window):
        #tkinter is imported as tk, within the class so calling it from mainwindow.py works.
        import tkinter as tk
        #master is established.
        self.master = master
        self.main_window = main_window
        #From there the window is established and framed.
        self.top = tk.Toplevel(self.master)
        self.top.title("Chicken Window")
        self.top.geometry("300x200")
        #The window is made unreziable, so the user must use it's intended dimensions.
        self.top.resizable(width=False, height=False)
        #the image "chicken.png" is opened, resized, and then antialised using LANCZOS, set as image.
        image = Image.open("chicken.png")
        image = image.resize((300, 200), Image.Resampling.LANCZOS)
        #chicken.png is set as photo via image.
        self.photo = ImageTk.PhotoImage(image)
        #Try and except are used to set up alt-text, with it backing up text if it does not work.
        try:
            #The backround is set to photo, which is chicken.png, and then modified slightly. This all makes it the background image.
            self.background_label = tk.Label(self.top, image=self.photo)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            self.background_label = tk.Label(self.top, text="Picture of a Chicken") #Alternate Text
        #A label is set to tell the user what to do, also stylized slightly.
        self.label_weight = tk.Label(self.top, text="Enter weight (lbs): ", bg="white")
        self.label_weight.pack(pady=5)
        #An entry area is created to enter the weight.
        self.weight_var = tk.StringVar() 
        self.entry_weight = tk.Entry(self.top, textvariable=self.weight_var)
        self.entry_weight.pack(pady=5)
        #label_calories is created, and displays a placeholder.
        self.label_calories = tk.Label(self.top, text="Calories: ")
        self.label_calories.pack(pady=5)
        #label_protein is created, and displays a placeholder.
        self.label_protein = tk.Label(self.top, text="Grams of Protein: ")
        self.label_protein.pack(pady=5)
        #label_fat is created, and displays a placeholder.
        self.label_fat = tk.Label(self.top, text="Grams of Fat: ")
        self.label_fat.pack(pady=5)
        #A button is created to be clicked to calculate the above variables.
        self.button = tk.Button(self.top, text="Calculate", command=self.calculate)
        self.button.pack(pady=5)
        #A exit button is created, with the text "X," placed in the upper left corner, and stylized as red.
        self.button = tk.Button(self.top, text="X", command=self.top.destroy, bg="red")
        self.button.place(x=0, y=0)
    #calculate is now defined so the program works.
    def calculate(self):
         """
         The "calculate" part of the program, where the users inputted information is used to calculate the final output.
         It's calculation is used to replace the labels already created with new ones displaying the final output.

         :return: calories, pgrams, fgrams
         """
         #weight is first set to what the user entered.
         weight = self.weight_var.get()
         #An if-else loop is used. Specifically if weight is numeric or not.
         if weight.isnumeric():
            #weight is got as a float value.
            weight = float(self.weight_var.get())
            #Each value, first calories, then protein (pgrams), then fat f(grams) are calculated by multiplying weight by their value per pound. It is stylized a little bit,
            #The previous placeholder labels also then change to display the new values.
            calories = 649 * weight
            self.label_calories.config(text=f"Calories: {calories:.2f}")
            pgrams = 79 * weight
            self.label_protein.config(text=f"Grams of Protein: {pgrams:.2f}")
            fgrams = 37 * weight
            self.label_fat.config(text=f"Grams of Fat: {fgrams:.2f}")
         #If weight is not numeric, then "invalid input!" is printed in the placeholder labels.
         else:
            self.label_calories.config(text="Invalid input!")
            self.label_protein.config(text="Invalid input!")
            self.label_fat.config(text="Invalid input!")
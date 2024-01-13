import tkinter as tk
from PIL import Image, ImageTk
from tkinter import *;
mainWin = Tk()
#mainWin.title("Program functionality")c

def plantClicked():
    messagebox.showinfo("What was the color of the plant?")

def animalClicked():
    messagebox.showinfo("What was the color of the animal?")

mainWin.geometry("600x700")
myApp = Frame(mainWin)
myApp.grid()
lab = Label(myApp, text = "Did you see a plant or an animal?")
#lab.grid();
mainWin.mainloop()

mainWin = Tk()  
mainWin.geometry("300x200");  
buttonPlant = Button(mainWin,text = "Plant");  
buttonPlant = Button(top, text = "green", command = plantClicked, activeforeground = "green", pady = 10)
buttonAnimal = Button(top, text = "blue", command = animalClicked, activeforeground = "blue", pady = 10)
buttonAnimal = Button(mainWin, text = "Animal")
buttonPlant.pack()  
buttonAnimal.pack()
mainWin.mainloop()
buttonPlant.pack(side = LEFT)
buttonAnimal.pack(side = RIGHT)

# mainWin.geometry("300x200");  
# buttonAnimal = Button(mainWin,text = "Animal");  
# buttonAnimal.pack();  
# mainWin.mainloop();
# buttonPlant.pack(side = RIGHT)



print("This is working \n ")
# root = tk.Tk()
# root.title("Wildsurf Tech")
# root.minsize(800,800)

# canvas = tk.Canvas(root)
# canvas.pack()



# pythonI = Image.open("python clipart")
# pythonI = ImageTk.PhotoImage(pythonI)

# plantOrAnimal_text = tk.StringVar()
# plantOrAnimal_button = tk.Button(root, textvariable=plantOrAnimal_text, font = "Century Gothic")
# plantOrAnimal_text.set("Did you see a plant or animal")



upper_frame = tk.Frame(root, bg='blue', bd=2)
upper_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.2)

entry = tk.Entry(upper_frame, bg='white', font=('Courier', 10))
entry.place(relx=0, rely=0, relwidth=0.4, relheight=1)

lower_frame = tk.Frame(root, bg='green', bd=5)
lower_frame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.5)

label = tk.Label(lower_frame, bg='white')
label.place(relwidth=1, relheight=1)

root.mainloop()


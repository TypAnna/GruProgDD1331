# Visar hur man lägger upp knappar i en grid

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Matris(Frame): #our class Matris inherits the Frame class
    """Knappmatris"""
    def skapaKnappar(self):
        self.knapplista = []
        #create 12 buttons and add to grid
        for nr in range(12):
            ny = ttk.Button(self, text = str(nr+1))
            ny.grid(row=nr//3, column=nr%3)
            self.knapplista.append(ny)

        #set the command (the function to be executed) of the 3rd button
        self.knapplista[2]["command"] = self.quit
        self.knapplista[3]["text"] = "katt"

        #set the command (function)  of 4th button using anonymous function
        #see for yourself what happens when we remove the 'lambda:' part
        self.knapplista[3]["command"] = lambda: print(4)

        self.knapplista[4]["command"] = lambda: messagebox.showinfo( "A pop-up", "Hello all")


    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.grid() #grid-function for Frames. Can do this due to inheritance
        self.skapaKnappar()


def main():
    rot = Tk()
    m = Matris(rot) #the __init__ function is called
    m.mainloop()
    rot.destroy()


#if we run this file, call the main method. If using this file somewhere else,
#dont call the main method (for example if we import it)
if __name__ == '__main__':
    main()

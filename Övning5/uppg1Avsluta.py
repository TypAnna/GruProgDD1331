from tkinter import *
from tkinter import ttk #in order for things to work on mac...

class Ram(Frame):#our class Ram inherits the class Frame, which comes from tkinter
    """Ett fönster med en knapp för att avsluta."""

    #when we write the __init__method, the child (Ram) will no longer inherit
    #the parents contructor (__init__-method)...
    def __init__(self, master=None): #master represents the parent window
        #... to keep the inheritance (of the contructor), we need to add a call
        #to the parents constructor
        Frame.__init__(self, master, width=150, height=50, background="#ffc0cb")
        self.pack()
        #Button is a class defined in tkinter. Note the use of named args
        self.avsluta = ttk.Button(self, text="Avsluta", command=self.quit)
        self.avsluta.pack()

    def whatever(self):
        print(self.avsluta)



def main():
    roten = Tk()
    t = Ram(roten)
    #by default, tk frames shrink or grow to fit their contents. If we want to
    #avoid that, we can write t.pack_propagate(0)
    t.pack_propagate(0)
    t.whatever()
    t.mainloop()
    roten.destroy()


main()

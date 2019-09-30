from tkinter import *
from tkinter import ttk

#use caps+underscore for constants
STARTER_POKEMONS = ["Squirtle", "Pikachu", "Bulbasaur", "Charmander"]

def kommando(meny):
    #curselection gets a list of the currently selected alternatives
    print("Du valde:" + STARTER_POKEMONS[int(meny.curselection()[0])])


def main():
    ram = Frame(height=700, width=100)
    ram.pack(side=TOP)

    rubrik = Label(ram, text = "Välj din favoritpokémon", bg="#fae7d4")
    #add rubrik add make it fill the full width
    rubrik.pack(side=TOP, fill=X)


    meny = Listbox(ram, height=10, width=30, bg="#ffc0cb", bd=0)
    meny.pack(side=LEFT, fill=Y)

    for i in STARTER_POKEMONS:
        #use END to append items to the list
        meny.insert(END, str(i))

    knapp = ttk.Button(text="Välj", command=lambda: kommando(meny))
    knapp.pack()

    # mainloop()


main()

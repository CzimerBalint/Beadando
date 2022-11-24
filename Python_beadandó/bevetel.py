import tkinter
import mysql.connector
from tkinter import *


# Database
my_connect = mysql.connector.connect(
  host="localhost",
  user="budget",
  passwd="123",
  database="mydatabase"
)
my_cursor = my_connect.cursor()



def bevet_top():

    bevetel_top = Toplevel()
    bevetel_top.title("Bevétel felvétele")


    bevetel_frame = tkinter.Frame(bevetel_top)
    bevetel_frame.pack()


    #Felhasználói grid
    name_label =tkinter.Label(bevetel_frame, text="Név:")
    name_label.grid(row= 0, column=0, padx=5, pady=5)
    name_entry = tkinter.Entry(bevetel_frame)
    name_entry.grid(row= 1, column=1, padx=5, pady=5)

    amount_label =tkinter.Label(bevetel_frame, text="Összeg:")
    amount_label.grid(row= 2, column=0, padx=5, pady=5)
    amount_entry = tkinter.Entry(bevetel_frame)
    amount_entry.grid(row= 3, column=1, padx=5, pady=5)

    my_cursor.execute("SELECT bevet_kategoria.megnevezes FROM bevet_kategoria")
    my_result = my_cursor.fetchone()

    options=[]
    clicked = StringVar()
    while my_result is not None:
        options.append(my_result)
        my_result = my_cursor.fetchone()


    clicked.set( "Válassz kategóriát" )

    dropdown_label =tkinter.Label(bevetel_frame, text="Kategória:")
    dropdown_label.grid(row= 4, column=0, padx=5, pady=5)
    dropdown_menu = OptionMenu(bevetel_frame, clicked , *options )
    dropdown_menu.grid(row= 5, column=1, padx=5, pady=5)



    bevetel_top.mainloop()
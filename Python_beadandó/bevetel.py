import time
from datetime import datetime
import tkinter
import mysql.connector
from tkinter import *
import classes as cls
import main


# Database
my_connect = mysql.connector.connect(
  host="localhost",
  user="budget",
  passwd="123",
  database="mydatabase"
)
my_cursor = my_connect.cursor()


def bevet_top():


    def input_get():

        name = name_entry.get()
        amount = amount_entry.get()
        datum = datum_entry.get()

        ##Converter
        category = str(clicked.get()).replace('(','').replace(')','').replace(",","").replace("'","")

        ##data=cls.BevetData(name,amount,category,datum)

        ##main.income_list.insert(END,data)

        querry = """SELECT bevet_kategoria.id FROM bevet_kategoria WHERE bevet_kategoria.megnevezes = %s"""
        my_result = tuple(map(str, category.split(', ')))
        my_cursor.execute(querry,my_result)
        eredmeny= my_cursor.fetchall()

        ##Converter
        eredmeny= str(eredmeny).replace('(','').replace(')','').replace(",","").replace("'","")
        print(eredmeny)


        bevetel_top.destroy()


    bevetel_top = Toplevel()
    bevetel_top.title("Bevétel felvétele")


    bevetel_frame = tkinter.Frame(bevetel_top)
    bevetel_frame.pack()


    #Felhasználói grid
    name_label =tkinter.Label(bevetel_frame, text="Név:")
    name_label.grid(row= 0, column=0, padx=5, pady=5)
    name_entry = tkinter.Entry(bevetel_frame)
    name_entry.insert(0,"pl. Nagy József")
    name_entry.grid(row= 1, column=1, padx=5, pady=5)

    amount_label =tkinter.Label(bevetel_frame, text="Összeg:")
    amount_label.grid(row= 2, column=0, padx=5, pady=5)
    amount_entry = tkinter.Entry(bevetel_frame)
    amount_entry.insert(0,"pl. 100 vagy 1000000")
    amount_entry.grid(row= 3, column=1, padx=5, pady=5)


    #Dropdown menü
    my_cursor.execute("SELECT bevet_kategoria.megnevezes FROM bevet_kategoria")
    my_result = my_cursor.fetchone()

    options=[]

    while my_result is not None:
        options.append(my_result)
        my_result = my_cursor.fetchone()

    clicked = StringVar()
    clicked.set(options[0])
    dropdown_label =tkinter.Label(bevetel_frame, text="Kategória:")
    dropdown_label.grid(row= 4, column=0, padx=5, pady=5)
    dropdown_menu = OptionMenu(bevetel_frame, clicked , *options )
    dropdown_menu.grid(row= 5, column=1, padx=5, pady=5)
    #----------------------------------------------------------------

    #Datetime
    now = datetime.today().isoformat()
    now=time.strftime("%Y-%m-%d %H:%M:%S")

    datum_label =tkinter.Label(bevetel_frame, text="Dátum és idő:")
    datum_label.grid(row= 6, column=0, padx=5, pady=5)
    datum_entry = tkinter.Entry(bevetel_frame)
    datum_entry.insert(0,now)
    datum_entry.grid(row= 7, column=1, padx=5, pady=5)

    bevetel_button=tkinter.Button(bevetel_frame, text="Bevétel rögzítése", command=input_get)
    bevetel_button.grid(row=8, column=2, padx=20, pady=20)





    bevetel_top.mainloop()







##        my_result = tuple(map(str, category.split(', ')))
##        sql="""SELECT bevet_kategoria.id FROM bevet_kategoria WHERE bevet_kategoria.megnevezes = %s"""
##        my_cursor.execute(sql,my_result)
##        my_result_2 = my_cursor.fetchall()
##        print(my_result_2)
##        #my_cursor.execute("INSERT INTO bevetel (sorszam,nev,osszeg,bevet_kategoria_id,datum) VALUES ('','name','amount','my_result_2','datum')")
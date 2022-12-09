import time
from datetime import datetime
import tkinter
import mysql.connector
from tkinter import *
import main


# Database
my_connect = mysql.connector.connect(
  host="localhost",
  user="budget",
  passwd="123",
  database="mydatabase"
)
my_cursor = my_connect.cursor()


def kiadas_top():


    def input_get():

        name = name_entry.get()
        amount = amount_entry.get()
        datum = datum_entry.get()

        ##Converter
        category = str(clicked.get()).replace('(','').replace(')','').replace(",","").replace("'","")

        querry = """SELECT kiadas_kategoria.id FROM kiadas_kategoria WHERE kiadas_kategoria.megnevezes = %s"""
        my_result = tuple(map(str, category.split(', ')))
        my_cursor.execute(querry,my_result)
        eredmeny= my_cursor.fetchall()

        ##Converter
        eredmeny= str(eredmeny).replace('(','').replace(')','').replace(",","").replace("'","")


        ##Insert to database
        sorszam=0
        category_id=str(eredmeny).replace('[','').replace(']','')
        querry="""INSERT INTO kiadas (sorszam,nev,osszeg,kiadas_kategoria_id,datum) VALUES (%s,%s,%s,%s,%s)"""
        val= (sorszam,name,amount,category_id,datum)
        my_cursor.execute(querry,val)
        my_connect.commit()


        main.outcome_list.delete(0, END)
        my_cursor.execute("SELECT kiadas.sorszam,kiadas.nev,kiadas.osszeg,kiadas_kategoria.megnevezes,kiadas.datum FROM kiadas INNER JOIN kiadas_kategoria ON kiadas.kiadas_kategoria_id=kiadas_kategoria.id")
        my_result = my_cursor.fetchone()

        while my_result is not None:
            main.outcome_list.insert(END,my_result)
            my_result = my_cursor.fetchone()


        kiadas_top.destroy()


    kiadas_top = Toplevel()
    kiadas_top.title("Kiadás felvétele")


    kiadas_frame = tkinter.Frame(kiadas_top)
    kiadas_frame.pack()


    #Felhasználói grid
    name_label =tkinter.Label(kiadas_frame, text="Név:")
    name_label.grid(row= 0, column=0, padx=5, pady=5)
    name_entry = tkinter.Entry(kiadas_frame)
    name_entry.insert(0,"pl. Nagy József")
    name_entry.grid(row= 1, column=1, padx=5, pady=5)

    amount_label =tkinter.Label(kiadas_frame, text="Összeg:")
    amount_label.grid(row= 2, column=0, padx=5, pady=5)
    amount_entry = tkinter.Entry(kiadas_frame)
    amount_entry.insert(0,"pl. 100 vagy 1000000")
    amount_entry.grid(row= 3, column=1, padx=5, pady=5)


    #Dropdown menü
    my_cursor.execute("SELECT kiadas_kategoria.megnevezes FROM kiadas_kategoria")
    my_result = my_cursor.fetchone()

    options=[]

    while my_result is not None:
        options.append(my_result)
        my_result = my_cursor.fetchone()

    clicked = StringVar()
    clicked.set(options[0])
    dropdown_label =tkinter.Label(kiadas_frame, text="Kategória:")
    dropdown_label.grid(row= 4, column=0, padx=5, pady=5)
    dropdown_menu = OptionMenu(kiadas_frame, clicked , *options )
    dropdown_menu.grid(row= 5, column=1, padx=5, pady=5)
    #----------------------------------------------------------------

    #Datetime
    now = datetime.today().isoformat()
    now=time.strftime("%Y-%m-%d %H:%M:%S")

    datum_label =tkinter.Label(kiadas_frame, text="Dátum és idő:")
    datum_label.grid(row= 6, column=0, padx=5, pady=5)
    datum_entry = tkinter.Entry(kiadas_frame)
    datum_entry.insert(0,now)
    datum_entry.grid(row= 7, column=1, padx=5, pady=5)

    bevetel_button=tkinter.Button(kiadas_frame, text="Bevétel rögzítése", command=input_get)
    bevetel_button.grid(row=8, column=2, padx=20, pady=20)





    kiadas_top.mainloop()
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


def bevet_torles_top():

    def submit_yes():

        if main.income_list.curselection() == ():
            top= Toplevel()
            top.geometry("250x150")
            top.title("Info")
            Label(top, text= "Válassz ki egy elemet a listából!").pack()
            Button(top,text="OK",command=top.destroy).pack()
            bevet_torles_top.destroy()

        else:
            list_item=main.income_list.get(main.income_list.curselection())
            list_item_tuple=(list_item[0],)
            sql = "DELETE FROM bevetel WHERE sorszam = %s"
            my_cursor.execute(sql,list_item_tuple)
            my_connect.commit()

            selected_checkboxs = main.income_list.curselection()

            for selected_checkbox in selected_checkboxs[::-1]:
                main.income_list.delete(selected_checkbox)

            bevet_torles_top.destroy()

    def submit_no():

        bevet_torles_top.destroy()

    bevet_torles_top = Toplevel()
    bevet_torles_top.title("Bevétel törlése")


    bevetel_torles_frame = tkinter.Frame(bevet_torles_top)
    bevetel_torles_frame.pack()


    #Törlés grid
    name_label =tkinter.Label(bevetel_torles_frame, text="Biztos törölni szeretnél?")
    name_label.grid(row= 0, column=0, padx=5, pady=5)

    bevetel_torles_yes_button=tkinter.Button(bevetel_torles_frame, text="Igen", width=10,command=submit_yes)
    bevetel_torles_yes_button.grid(row=1, column=0, padx=20, pady=20)

    bevetel_torles_no_button=tkinter.Button(bevetel_torles_frame, text="Nem", width=10, command=submit_no)
    bevetel_torles_no_button.grid(row=1, column=1, padx=20, pady=20)

    bevet_torles_top.mainloop()
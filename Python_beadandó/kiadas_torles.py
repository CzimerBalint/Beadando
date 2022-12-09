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


def kiadas_torles_top():

    def submit_yes():

        if main.outcome_list.curselection() == ():
            top= Toplevel()
            top.geometry("250x150")
            top.title("Info")
            Label(top, text= "Válassz ki egy elemet a listából!").pack()
            Button(top,text="OK",command=top.destroy).pack()
            kiadas_torles_top.destroy()

        else:
            list_item=main.outcome_list.get(main.outcome_list.curselection())
            list_item_tuple=(list_item[0],)
            sql = "DELETE FROM kiadas WHERE sorszam = %s"
            my_cursor.execute(sql,list_item_tuple)
            my_connect.commit()

            selected_checkboxs = main.outcome_list.curselection()

            for selected_checkbox in selected_checkboxs[::-1]:
                main.outcome_list.delete(selected_checkbox)

            kiadas_torles_top.destroy()

    def submit_no():

        kiadas_torles_top.destroy()

    kiadas_torles_top = Toplevel()
    kiadas_torles_top.title("Kiadás törlése")


    kiadas_torles_frame = tkinter.Frame(kiadas_torles_top)
    kiadas_torles_frame.pack()


    #Törlés grid
    name_label =tkinter.Label(kiadas_torles_frame, text="Biztos törölni szeretnél?")
    name_label.grid(row= 0, column=0, padx=5, pady=5)

    kiadas_torles_yes_button=tkinter.Button(kiadas_torles_frame, text="Igen", width=10,command=submit_yes)
    kiadas_torles_yes_button.grid(row=1, column=0, padx=20, pady=20)

    kiadas_torles_no_button=tkinter.Button(kiadas_torles_frame, text="Nem", width=10, command=submit_no)
    kiadas_torles_no_button.grid(row=1, column=1, padx=20, pady=20)

    kiadas_torles_top.mainloop()
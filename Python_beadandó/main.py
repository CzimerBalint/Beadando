import tkinter
from tkinter import *
import mysql.connector
from bevetel import *
from kiadas import *
from bevetel_torles import *
from kiadas_torles import *

# Database
my_connect = mysql.connector.connect(
  host="localhost",
  user="budget",
  passwd="123",
  database="mydatabase"
)
my_cursor = my_connect.cursor()


window = tkinter.Tk()
window.title("Cashtp")
background_image= tkinter.PhotoImage(file='./img/bg.png')
background_label= tkinter.Label(window, image=background_image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

welcomeText = tkinter.Label(text="Költségvetés Manager",font=('Verdana', 40, 'bold'),pady=10, padx=10)
welcomeText.pack()



frame = tkinter.Frame(window)
frame.pack()

income_button=tkinter.Button(frame,text="Bevétel hozzáadás", command=bevet_top)
income_button.grid(row=0, column=0, padx=5, pady=5)

outcome_button=tkinter.Button(frame, text="Kiadás hozzáadás", command=kiadas_top)
outcome_button.grid(row=0, column=2, padx=5, pady=5)

outcome_button=tkinter.Button(frame, text="Bevétel törlése", command=bevet_torles_top)
outcome_button.grid(row=0, column=1, padx=5, pady=5)

outcome_button=tkinter.Button(frame, text="Kiadás törlése", command=kiadas_torles_top)
outcome_button.grid(row=0, column=3, padx=5, pady=5)

frame2 = tkinter.Frame(window)
frame2.pack()

income_label=tkinter.Label(frame2, text="Bevételek listája")
income_label.grid(row=2, column=2, padx=10, pady=10)

income_list=tkinter.Listbox(frame2, background="black", fg="lime",width=100,height=20)
income_list.grid(row=3, column=2,padx=10,pady=10)

my_cursor.execute("SELECT bevetel.sorszam,bevetel.nev,bevetel.osszeg,bevet_kategoria.megnevezes,bevetel.datum FROM `bevetel`INNER JOIN bevet_kategoria ON bevetel.bevet_kategoria_id=bevet_kategoria.id")
my_result = my_cursor.fetchone()

while my_result is not None:
    income_list.insert(END,my_result)
    my_result = my_cursor.fetchone()

outcome_label=tkinter.Label(frame2, text="Kiadások listája")
outcome_label.grid(row=2, column=3, padx=10, pady=10)

outcome_list=tkinter.Listbox(frame2, background="black", fg="red",width=100,height=20)
outcome_list.grid(row=3, column=3,padx=10,pady=10)

my_cursor.execute("SELECT kiadas.sorszam,kiadas.nev,kiadas.osszeg,kiadas_kategoria.megnevezes,kiadas.datum FROM kiadas INNER JOIN kiadas_kategoria ON kiadas.kiadas_kategoria_id=kiadas_kategoria.id")
my_result = my_cursor.fetchone()

while my_result is not None:
    outcome_list.insert(END,my_result)
    my_result = my_cursor.fetchone()


window.mainloop()
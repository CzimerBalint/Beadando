import tkinter
from tkinter import *
import mysql.connector
import bevetel as bev

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

welcomeText = tkinter.Label(text="Költéség Manager",font=('Verdana', 40, 'bold'),pady=10, padx=10)
welcomeText.pack()



frame = tkinter.Frame(window)
frame.pack()

income_button=tkinter.Button(frame,text="Bevétel hozzáadás", command=bev.bevet_top)
income_button.grid(row=0, column=0, padx=5, pady=5)

outcome_button=tkinter.Button(frame, text="Kiadás hozzáadás")
outcome_button.grid(row=0, column=1, padx=5, pady=5)

outcome_button=tkinter.Button(frame, text="Bevétel törlése")
outcome_button.grid(row=0, column=2, padx=5, pady=5)

outcome_button=tkinter.Button(frame, text="Kiadás törlése")
outcome_button.grid(row=0, column=3, padx=5, pady=5)

frame2 = tkinter.Frame(window)
frame2.pack()

income_label=tkinter.Label(frame2, text="Bevételek listája")
income_label.grid(row=2, column=2, padx=10, pady=10)

income_list=tkinter.Listbox(frame2, background="black", fg="red",width=100,height=20)
income_list.grid(row=3, column=2,padx=10,pady=10)

my_cursor.execute("SELECT bevetel.sorszam,bevetel.nev,bevetel.osszeg,bevet_kategoria.megnevezes,bevetel.datum FROM `bevetel`INNER JOIN bevet_kategoria ON bevetel.bevet_kategoria_id=bevet_kategoria.id")
my_result = my_cursor.fetchone()

while my_result is not None:
    income_list.insert(1,my_result)
    my_result = my_cursor.fetchone()

outcome_label=tkinter.Label(frame2, text="Kiadások listája")
outcome_label.grid(row=2, column=3, padx=10, pady=10)

outcome_list=tkinter.Listbox(frame2, background="black", fg="red",width=100,height=20)
outcome_list.grid(row=3, column=3,padx=10,pady=10)

my_cursor.execute("SELECT kiadas.sorszam,kiadas.nev,kiadas.osszeg,kiadas_kategoria.megnevezes,kiadas.datum FROM kiadas INNER JOIN kiadas_kategoria ON kiadas.kiadas_kategoria_id=kiadas_kategoria.id")
my_result = my_cursor.fetchone()

while my_result is not None:
    outcome_list.insert(1,my_result)
    my_result = my_cursor.fetchone()




window.mainloop()


##
## SELECT kiadas.sorszam,kiadas.nev,kiadas.osszeg,kiadas_kategoria.megnevezes,kiadas.datum FROM kiadas INNER JOIN kiadas_kategoria ON kiadas.kiadas_kategoria_id=kiadas_kategoria.id
##
###Felhasználói grid
##user_info_frame =tkinter.LabelFrame(frame, text="Felhasználó adatai")
##user_info_frame.grid(row= 0, column=0, padx=20, pady=10)
##
##first_name_label = tkinter.Label(user_info_frame, text="Vezeték név:")
##first_name_label.grid(row=0, column=0)
##last_name_label = tkinter.Label(user_info_frame, text="Kereszt név:")
##last_name_label.grid(row=0, column=1)
##
##first_name_entry = tkinter.Entry(user_info_frame)
##last_name_entry = tkinter.Entry(user_info_frame)
##first_name_entry.grid(row=1, column=0)
##last_name_entry.grid(row=1, column=1)
###---------------------------------------------------------------------
##
##
###Pénzügyi grid
##budget_frame =tkinter.LabelFrame(frame, text="Pénzügyi adatok")
##budget_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)
##
##income_label = tkinter.Label(budget_frame, text="Bevétel:")
##income_label.grid(row=0, column=0)
##outcome_label = tkinter.Label(budget_frame, text="Kiadás:")
##outcome_label.grid(row=0, column=1)
##
##income_entry = tkinter.Entry(budget_frame)
##outcome_entry = tkinter.Entry(budget_frame)
##income_entry.grid(row=1, column=0)
##outcome_entry.grid(row=1, column=1)
###---------------------------------------------------------------------
import mysql.connector
from tkinter import *
import tkinter


window = tkinter.Tk()
window.title("Cashtp")

# Database
my_connect = mysql.connector.connect(
  host="localhost",
  user="budget",
  passwd="123",
  database="mydatabase"
)
my_cursor = my_connect.cursor()

querry = """SELECT bevet_kategoria.id FROM bevet_kategoria WHERE bevet_kategoria.megnevezes = %s"""
text="Fizetés"
my_result = tuple(map(str, text.split(', ')))
print(my_result)

my_cursor.execute(querry,my_result)
eredmeny= my_cursor.fetchall()

print(eredmeny)



window.mainloop()
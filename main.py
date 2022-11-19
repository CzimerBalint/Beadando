import tkinter



window = tkinter.Tk()
window.title("Cashtp")
background_image= tkinter.PhotoImage(file='./img/bg.png')
background_label= tkinter.Label(window, image=background_image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

frame = tkinter.Frame(window)
frame.pack()

#Felhasználói grid
user_info_frame =tkinter.LabelFrame(frame, text="Felhasználó adatai")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="Vezeték név:")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Kereszt név:")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)
#---------------------------------------------------------------------


#Pénzügyi grid
courses_frame =tkinter.LabelFrame(frame, text="Pénzügyi adatok")
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

income_label = tkinter.Label(courses_frame, text="Bevétel:")
income_label.grid(row=0, column=0)
outcome_label = tkinter.Label(courses_frame, text="Kiadás:")
outcome_label.grid(row=0, column=1)

income_entry = tkinter.Entry(courses_frame)
outcome_entry = tkinter.Entry(courses_frame)
income_entry.grid(row=1, column=0)
outcome_entry.grid(row=1, column=1)
#---------------------------------------------------------------------


window.mainloop()
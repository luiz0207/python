#importar a biblioteca
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#Criar nossa janela
jan = Tk()
jan.title("Dp systems = Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)


#carregando imagem

logo = PhotoImage(file="icons/logo.png")


#widgets

leftFrame = Frame(jan, width=200, height=100, bg="MIDNIGHTBLUE", relief="raise")
leftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

logoLabel = Label(leftFrame, image=logo, bg="MIDNIGHTBLUE")
logoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="USERNAME:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=5, y=100)

UserEntry = Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text="PASSWORD:" , font=("Centuary Gothic" , 20), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=150, y=150)

PassEntry = Entry(RightFrame, width=30)
PassEntry.place(x=150, y=160)

#botões

LoginButton = ttk.Button(RightFrame, text="Login", width=30)
LoginButton.place(x=100, y=225)

#botão de registro
RegisterButton = ttk.Button(RightFrame, text="Register", width=20)
RegisterButton.place(x=125, y=260)


jan.mainloop()
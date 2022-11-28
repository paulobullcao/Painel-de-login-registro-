#Importando as bibliotecas
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.font import BOLD

#Criando a janela do programa
janela = Tk()
janela.title("MOSTRE O SEU JEITO BULC DE SER")
janela.geometry("600x300")
janela.configure(background ="white")
janela.resizable(width=False,height=False)
janela.attributes("-alpha", 0.9)

# Carregando algumas imagens para o programa


#.......Widgets............     
#Configurações de background
LeftFrame = Frame(janela, width = 200, height = 300, bg ='BLACK', relief = 'raise')
LeftFrame.pack(side=LEFT)

RightFrame = Frame(janela, width = 395, height = 300, bg ='RED', relief = 'raise')
RightFrame.pack(side=RIGHT)

'''
Logolabel = Label(LeftFrame, image = logo, bg ="RED")
Logolabel.place(x= 50, y= 100)
'''
#Campo Título

UserLabel = Label(RightFrame, text = 'BULC ', font =('century Gothic', 20), bg ='RED',fg='white')
UserLabel.place(x = 150, y = 50)


#Campo de login
UserLabel = Label(RightFrame, text = 'Username: ', font =('century Gothic', 20), bg ='RED',fg='white')
UserLabel.place(x = 5, y = 100)


UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x = 160, y = 112)

#Campo de senha
PassLabel = Label(RightFrame, text ="Password:", font = ("century Gothic", 20 ), bg ="RED", fg = "white",)
PassLabel.place(x = 5, y = 150)

PassEntry = ttk.Entry(RightFrame, width = 30, show = "*") 
PassEntry.place(x = 160, y = 160)

#Botões 

LoginButton = ttk.Button(RightFrame, text="Login", width = 20)
LoginButton.place(x = 160, y = 200 ) 

RegisterButton = ttk.Button(RightFrame, text="Register", width = 20)
RegisterButton.place(x = 160, y = 240 ) 

janela.mainloop()

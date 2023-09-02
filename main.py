# importando o Tkinter

from tkinter import *
from tkinter import ttk


#cores

cor1 = '#3b3b3b' #preto
cor2 = '#feffff' #branco
cor3 = '#38576b' #azul
cor4 = '#eceff1' #cinza
cor5 = '#ffab40' #laranja

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)


#criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#variavel vazia todos valores
todos_valores = ''

#criando função
def entrar_valor(e):

    global todos_valores

    todos_valores = todos_valores + str(e)

    #passando valor para leitor
    valor_leitor.set(todos_valores)


#funcao para calcular

def calcular():

    global todos_valores

    resultado = eval(todos_valores)
    valor_leitor.set(str(resultado))

#funcao limpar tela
def limpar_tela():

    global todos_valores

    todos_valores=""
    valor_leitor.set("")

#criando leitor

valor_leitor = StringVar()

app_leitor = Label(frame_tela, textvariable=valor_leitor, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_leitor.place(x=0, y=0)


#criando botoes

btn1 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn1.place(x=0, y=0)

btn2 = Button(frame_corpo, command=lambda: entrar_valor('%'), text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn2.place(x=118, y=0)

btn3 = Button(frame_corpo, command=lambda: entrar_valor('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn3.place(x=177, y=0)

btn4 = Button(frame_corpo, command=lambda: entrar_valor('7'), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn4.place(x=0, y=52)
btn4 = Button(frame_corpo, command=lambda: entrar_valor('8'), text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn4.place(x=59, y=52)
btn4 = Button(frame_corpo, command=lambda: entrar_valor('9'), text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn4.place(x=118, y=52)
btn5 = Button(frame_corpo, command=lambda: entrar_valor('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn5.place(x=177, y=52)

btn6 = Button(frame_corpo, command=lambda: entrar_valor('4'), text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn6.place(x=0, y=103)
btn6 = Button(frame_corpo, command=lambda: entrar_valor('5'), text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn6.place(x=59, y=103)
btn6 = Button(frame_corpo, command=lambda: entrar_valor('6'), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn6.place(x=118, y=103)
btn7 = Button(frame_corpo, command=lambda: entrar_valor('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn7.place(x=177, y=103)

btn8 = Button(frame_corpo, command=lambda: entrar_valor('1'), text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn8.place(x=0, y=156)
btn8 = Button(frame_corpo, command=lambda: entrar_valor('2'), text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn8.place(x=59, y=156)
btn8 = Button(frame_corpo, command=lambda: entrar_valor('3'), text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn8.place(x=118, y=156)
btn9 = Button(frame_corpo, command=lambda: entrar_valor('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn9.place(x=177, y=156)

btn10 = Button(frame_corpo, command=lambda: entrar_valor('0'), text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn10.place(x=0, y=208)
btn10 = Button(frame_corpo, command=lambda: entrar_valor('.'), text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn10.place(x=118, y=208)
btn11 = Button(frame_corpo, command=calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn11.place(x=177, y=208)





janela.mainloop()
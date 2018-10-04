#from tkinter import *
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here

import os

root = Tk(className = 'reconhecimento_facial_principal')
root.title('Reconhecimento Facial')
svalue = StringVar() 
dvalue = IntVar()

l = Label(root, text="Adicionar Nova Pessoa")
l.config(font=("Courier", 15))
l.pack()

Label(root, text="Nome: ").pack()
w1 = Entry(root, textvariable=svalue).pack()

Label(root, text="Idade: ").pack()
w2 = Entry(root, textvariable=dvalue).pack()


def prepara_dados_LBPH_btn():
    Nome = svalue.get()
    os.system('python3 PreparaDadosLBPH.py %s'%Nome)

def reconhecimento_facial_LBPH_btn():
    os.system('python3 ReconhecimentoFacialLBPH.py')

def adiciona_pessoa_btn():
    Nome = svalue.get()
    Idade = dvalue.get()
    os.system('python3 AdicionarPessoa.py %s %d' %(Nome, Idade))

add_btn = Button(root,text="Adicionar", command=adiciona_pessoa_btn)
add_btn.pack()

f=Frame(root,height=1, width=400, bg="black")
f.pack()

l = Label(root, text="Preparar Dados")
l.config(font=("Courier", 15))
l.pack()

recogL_btn = Button(root,text="Preparar Dados (LBPH)", command=prepara_dados_LBPH_btn)
recogL_btn.pack()

f=Frame(root,height=1, width=400, bg="black")
f.pack()

l = Label(root, text="Reconhecimento Facial")
l.config(font=("Courier", 15))
l.pack()

recogL_btn = Button(root,text="Reconhecimento Facial (LBPH)", command=reconhecimento_facial_LBPH_btn)
recogL_btn.pack()

root.mainloop()
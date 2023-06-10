import webbrowser
from tkinter import *

root =Tk( )

root.title('Abrir browser')
root.geometry('300X200')

def google():
    webbrowser.open('www.google.com')

mygoogle = Button(root, text="Abrir o Google", command=google).pack(pady=20)
root.mainloop
from tkinter import *

class Tela_venda2(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.geometry("400x400+550+100")
        self.title("Civic")
        self["bg"]= "aquamarine2"
        self.grab_set()
        self.font = ('14')

        self.lb = Label(self, text='Marca: \nValor: 100.000\n', font=self.font, bg='aquamarine2', fg='black')
        self.lb.place(x=130, y=30)
import tkinter as tk
import random

class GeneradorNumeros:
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.title("Generador de números")

        self.etiqueta_num1 = tk.Label(self.raiz, text="Número 1")
        self.etiqueta_num1.pack()

        self.spinbox_num1 = tk.Spinbox(self.raiz, from_=0, to=100)
        self.spinbox_num1.pack()

        self.etiqueta_num2 = tk.Label(self.raiz, text="Número 2")
        self.etiqueta_num2.pack()

        self.spinbox_num2 = tk.Spinbox(self.raiz, from_=0, to=100)
        self.spinbox_num2.pack()

        self.etiqueta_generado = tk.Label(self.raiz, text="Número generado")
        self.etiqueta_generado.pack()

        self.entry_generado = tk.Entry(self.raiz, width=10)
        self.entry_generado.config(state="readonly")
        self.entry_generado.pack()

        self.boton_generar = tk.Button(self.raiz, text="Generar", command=self.generar_numero)
        self.boton_generar.pack()

        self.raiz.mainloop()

    def generar_numero(self):
        num1 = int(self.spinbox_num1.get())
        num2 = int(self.spinbox_num2.get())
        numero_generado = random.randint(num1, num2)
        self.entry_generado.config(state="normal")
        self.entry_generado.delete(0, tk.END)
        self.entry_generado.insert(0, str(numero_generado))
        self.entry_generado.config(state="readonly")

if __name__ == "__main__":
    GeneradorNumeros()
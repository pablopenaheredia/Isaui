import tkinter as tk
import random

class GeneradorNumeros:
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.title("Generador de números")

        # Columna 1
        self.frame_izquierda = tk.Frame(self.raiz)
        self.frame_izquierda.grid(row=0, column=0, padx=10, pady=10)

        self.etiqueta_num1 = tk.Label(self.frame_izquierda, text="Número 1")
        self.etiqueta_num1.grid(row=0, column=0, padx=5, pady=5)

        self.etiqueta_num2 = tk.Label(self.frame_izquierda, text="Número 2")
        self.etiqueta_num2.grid(row=1, column=0, padx=5, pady=5)

        self.etiqueta_generado = tk.Label(self.frame_izquierda, text="Número generado")
        self.etiqueta_generado.grid(row=2, column=0, padx=5, pady=5)

        # Columna 2
        self.frame_derecha = tk.Frame(self.raiz)
        self.frame_derecha.grid(row=0, column=1, padx=10, pady=10)

        self.spinbox_num1 = tk.Spinbox(self.frame_derecha, from_=0, to=100)
        self.spinbox_num1.grid(row=0, column=0, padx=5, pady=5)

        self.spinbox_num2 = tk.Spinbox(self.frame_derecha, from_=0, to=100)
        self.spinbox_num2.grid(row=1, column=0, padx=5, pady=5)

        self.entry_generado = tk.Entry(self.frame_derecha, width=10)
        self.entry_generado.config(state="readonly")
        self.entry_generado.grid(row=2, column=0, padx=5, pady=5)

        # Botón generar
        self.boton_generar = tk.Button(self.raiz, text="Generar", command=self.generar_numero)
        self.boton_generar.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

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

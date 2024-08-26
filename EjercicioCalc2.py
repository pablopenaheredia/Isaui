import tkinter as tk

class Calculadora2:
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.title("Calculadora 2")

        self.etiqueta_valor1 = tk.Label(self.raiz, text="Valor 1")
        self.etiqueta_valor1.pack()

        self.entry_valor1 = tk.Entry(self.raiz, width=10)
        self.entry_valor1.pack()

        self.etiqueta_valor2 = tk.Label(self.raiz, text="Valor 2")
        self.etiqueta_valor2.pack()

        self.entry_valor2 = tk.Entry(self.raiz, width=10)
        self.entry_valor2.pack()

        self.etiqueta_operacion = tk.Label(self.raiz, text="Operación")
        self.etiqueta_operacion.pack()

        self.valor_operacion = tk.StringVar()
        self.valor_operacion.set("Sumar")

        self.radiobutton_sumar = tk.Radiobutton(self.raiz, text="Sumar", variable=self.valor_operacion, value="Sumar")
        self.radiobutton_sumar.pack()

        self.radiobutton_restar = tk.Radiobutton(self.raiz, text="Restar", variable=self.valor_operacion, value="Restar")
        self.radiobutton_restar.pack()

        self.radiobutton_multiplicar = tk.Radiobutton(self.raiz, text="Multiplicar", variable=self.valor_operacion, value="Multiplicar")
        self.radiobutton_multiplicar.pack()

        self.radiobutton_dividir = tk.Radiobutton(self.raiz, text="Dividir", variable=self.valor_operacion, value="Dividir")
        self.radiobutton_dividir.pack()

        self.etiqueta_resultado = tk.Label(self.raiz, text="Resultado")
        self.etiqueta_resultado.pack()

        self.entry_resultado = tk.Entry(self.raiz, width=10)
        self.entry_resultado.config(state="readonly")
        self.entry_resultado.pack()

        self.boton_calcular = tk.Button(self.raiz, text="Calcular", command=self.calcular)
        self.boton_calcular.pack()

        self.raiz.mainloop()

    def calcular(self):
        try:
            valor1 = float(self.entry_valor1.get())
            valor2 = float(self.entry_valor2.get())
            operacion = self.valor_operacion.get()
            if operacion == "Sumar":
                resultado = valor1 + valor2
            elif operacion == "Restar":
                resultado = valor1 - valor2
            elif operacion == "Multiplicar":
                resultado = valor1 * valor2
            elif operacion == "Dividir":
                if valor2 != 0:
                    resultado = valor1 / valor2
                else:
                    resultado = "Error: División por cero"
            self.entry_resultado.config(state="normal")
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, str(resultado))
            self.entry_resultado.config(state="readonly")
        except ValueError:
            self.entry_resultado.config(state="normal")
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, "Error: Valores inválidos")
            self.entry_resultado.config(state="readonly")

if __name__ == "__main__":
    Calculadora2()
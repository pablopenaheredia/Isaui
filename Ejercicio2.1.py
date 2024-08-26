import tkinter as tk

class Calculadora:
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.title("Calculadora")

        self.etiqueta_num1 = tk.Label(self.raiz, text="Primer número")
        self.etiqueta_num1.pack()

        self.entry_num1 = tk.Entry(self.raiz, width=10)
        self.entry_num1.pack()

        self.etiqueta_num2 = tk.Label(self.raiz, text="Segundo número")
        self.etiqueta_num2.pack()

        self.entry_num2 = tk.Entry(self.raiz, width=10)
        self.entry_num2.pack()

        self.etiqueta_resultado = tk.Label(self.raiz, text="Resultado")
        self.etiqueta_resultado.pack()

        self.entry_resultado = tk.Entry(self.raiz, width=10)
        self.entry_resultado.config(state="readonly")
        self.entry_resultado.pack()

        self.boton_suma = tk.Button(self.raiz, text="+", command=lambda: self.operacion("+"))
        self.boton_suma.pack(side=tk.LEFT)

        self.boton_resta = tk.Button(self.raiz, text="-", command=lambda: self.operacion("-"))
        self.boton_resta.pack(side=tk.LEFT)

        self.boton_multiplicacion = tk.Button(self.raiz, text="*", command=lambda: self.operacion("*"))
        self.boton_multiplicacion.pack(side=tk.LEFT)

        self.boton_division = tk.Button(self.raiz, text="/", command=lambda: self.operacion("/"))
        self.boton_division.pack(side=tk.LEFT)

        self.boton_porcentaje = tk.Button(self.raiz, text="%", command=lambda: self.operacion("%"))
        self.boton_porcentaje.pack(side=tk.LEFT)

        self.boton_reset = tk.Button(self.raiz, text="RESET", command=self.reset)
        self.boton_reset.pack(side=tk.LEFT)

        self.raiz.mainloop()

    def operacion(self, operador):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            if operador == "+":
                resultado = num1 + num2
            elif operador == "-":
                resultado = num1 - num2
            elif operador == "*":
                resultado = num1 * num2
            elif operador == "/":
                resultado = num1 / num2
            elif operador == "%":
                resultado = num1 % num2
            self.entry_resultado.config(state="normal")
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, str(resultado))
            self.entry_resultado.config(state="readonly")
        except ValueError:
            self.entry_resultado.config(state="normal")
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, "Error")
            self.entry_resultado.config(state="readonly")

    def reset(self):
        self.entry_num1.delete(0, tk.END)
        self.entry_num2.delete(0, tk.END)
        self.entry_resultado.config(state="normal")
        self.entry_resultado.delete(0, tk.END)
        self.entry_resultado.config(state="readonly")

if __name__ == "__main__":
    Calculadora()
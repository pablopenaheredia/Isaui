import tkinter as tk

class Calculadora:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora")

        self.etiqueta_num1 = tk.Label(self.ventana, text="Primer número")
        self.etiqueta_num1.grid(row=0, column=0, padx=5, pady=5)

        self.entry_num1 = tk.Entry(self.ventana, width=20)
        self.entry_num1.grid(row=0, column=1, padx=5, pady=5)

        self.etiqueta_num2 = tk.Label(self.ventana, text="Segundo número")
        self.etiqueta_num2.grid(row=1, column=0, padx=5, pady=5)

        self.entry_num2 = tk.Entry(self.ventana, width=20)
        self.entry_num2.grid(row=1, column=1, padx=5, pady=5)

        self.etiqueta_resultado = tk.Label(self.ventana, text="Resultado")
        self.etiqueta_resultado.grid(row=2, column=0, padx=5, pady=5)

        self.entry_resultado = tk.Entry(self.ventana, width=20)
        self.entry_resultado.config(state="readonly")
        self.entry_resultado.grid(row=2, column=1, padx=5, pady=5)

        self.boton_suma = tk.Button(self.ventana, text="+", command=lambda: self.operacion("+"), width=10)
        self.boton_suma.grid(row=3, column=0, padx=5, pady=5)

        self.boton_multiplicacion = tk.Button(self.ventana, text="*", command=lambda: self.operacion("*"), width=10)
        self.boton_multiplicacion.grid(row=4, column=0, padx=5, pady=5)

        self.boton_porcentaje = tk.Button(self.ventana, text="%", command=lambda: self.operacion("%"), width=10)
        self.boton_porcentaje.grid(row=5, column=0, padx=5, pady=5)

        self.boton_resta = tk.Button(self.ventana, text="-", command=lambda: self.operacion("-"), width=10)
        self.boton_resta.grid(row=3, column=1, padx=5, pady=5)

        self.boton_division = tk.Button(self.ventana, text="/", command=lambda: self.operacion("/"), width=10)
        self.boton_division.grid(row=4, column=1, padx=5, pady=5)

        self.boton_reset = tk.Button(self.ventana, text="Limpiar", command=self.reset, width=20)
        self.boton_reset.grid(row=5, column=1, padx=5, pady=5)

        self.ventana.mainloop()

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

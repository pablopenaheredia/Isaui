import tkinter as tk

class Calculadora2:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora 2")

        # Columna 1
        self.frame_izquierda = tk.Frame(self.ventana)
        self.frame_izquierda.grid(row=0, column=0, padx=10, pady=10)

        self.etiqueta_valor1 = tk.Label(self.frame_izquierda, text="Valor 1")
        self.etiqueta_valor1.grid(row=0, column=0, padx=5, pady=5)

        self.etiqueta_valor2 = tk.Label(self.frame_izquierda, text="Valor 2")
        self.etiqueta_valor2.grid(row=1, column=0, padx=5, pady=5)

        self.etiqueta_resultado = tk.Label(self.frame_izquierda, text="Resultado")
        self.etiqueta_resultado.grid(row=2, column=0, padx=5, pady=5)

        # Columna 2
        self.frame_centro = tk.Frame(self.ventana)
        self.frame_centro.grid(row=0, column=1, padx=10, pady=10)

        self.entry_valor1 = tk.Entry(self.frame_centro, width=10)
        self.entry_valor1.grid(row=0, column=0, padx=5, pady=5)

        self.entry_valor2 = tk.Entry(self.frame_centro, width=10)
        self.entry_valor2.grid(row=1, column=0, padx=5, pady=5)

        self.entry_resultado = tk.Entry(self.frame_centro, width=10)
        self.entry_resultado.config(state="readonly")
        self.entry_resultado.grid(row=2, column=0, padx=5, pady=5)

        # Columna 3
        self.frame_derecha = tk.Frame(self.ventana)
        self.frame_derecha.grid(row=0, column=2, padx=10, pady=10)

        self.etiqueta_operacion = tk.Label(self.frame_derecha, text="Operaciones")
        self.etiqueta_operacion.grid(row=0, column=0, padx=5, pady=5)

        self.valor_operacion = tk.StringVar()
        self.valor_operacion.set("Sumar")

        self.radiobutton_sumar = tk.Radiobutton(self.frame_derecha, text="Sumar", variable=self.valor_operacion, value="Sumar")
        self.radiobutton_sumar.grid(row=1, column=0, padx=5, pady=5)

        self.radiobutton_restar = tk.Radiobutton(self.frame_derecha, text="Restar", variable=self.valor_operacion, value="Restar")
        self.radiobutton_restar.grid(row=2, column=0, padx=5, pady=5)

        self.radiobutton_multiplicar = tk.Radiobutton(self.frame_derecha, text="Multiplicar", variable=self.valor_operacion, value="Multiplicar")
        self.radiobutton_multiplicar.grid(row=3, column=0, padx=5, pady=5)

        self.radiobutton_dividir = tk.Radiobutton(self.frame_derecha, text="Dividir", variable=self.valor_operacion, value="Dividir")
        self.radiobutton_dividir.grid(row=4, column=0, padx=5, pady=5)

        # Botón calcular
        self.boton_calcular = tk.Button(self.ventana, text="Calcular", command=self.calcular)
        self.boton_calcular.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.ventana.mainloop()

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

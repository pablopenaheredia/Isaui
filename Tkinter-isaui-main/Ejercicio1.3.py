import tkinter as tk

def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, x+1):
            resultado *= i
        return resultado

class Factorial:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Factorial")
        self.n = 2

        self.titulo = tk.Label(self.ventana, text="n")
        self.titulo.grid(row=0, column=0, padx=5, pady=5)

        self.titulo_factorial = tk.Label(self.ventana, text="Factorial(n)")
        self.titulo_factorial.grid(row=0, column=2, padx=5, pady=5)

        self.entry_n = tk.Entry(self.ventana, width=10)
        self.entry_n.insert(0, "2")
        self.entry_n.config(state="readonly")
        self.entry_n.grid(row=0, column=1, padx=5, pady=5)

        self.entry_factorial = tk.Entry(self.ventana, width=10)
        self.entry_factorial.insert(0, "2")
        self.entry_factorial.config(state="readonly")
        self.entry_factorial.grid(row=0, column=3, padx=5, pady=5)

        self.boton = tk.Button(self.ventana, text="Siguiente", command=self.boton_siguiente)
        self.boton.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

        self.ventana.mainloop()

    def boton_siguiente(self):
        self.n += 1
        self.entry_n.config(state="normal")
        self.entry_n.delete(0, tk.END)
        self.entry_n.insert(0, str(self.n))
        self.entry_n.config(state="readonly")

        resultado_factorial = factorial(self.n)
        self.entry_factorial.config(state="normal")
        self.entry_factorial.delete(0, tk.END)
        self.entry_factorial.insert(0, str(resultado_factorial))
        self.entry_factorial.config(state="readonly")

if __name__ == "__main__":
    Factorial()

import tkinter as tk

class Factorial:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Factorial")
        self.n = 2

        self.etiqueta_n = tk.Label(self.ventana, text="n")
        self.etiqueta_n.grid(row=0, column=0, padx=5, pady=5)

        self.etiqueta_factorial = tk.Label(self.ventana, text="Factorial(n)")
        self.etiqueta_factorial.grid(row=0, column=2, padx=5, pady=5)

        self.entry_n = tk.Entry(self.ventana, width=10)
        self.entry_n.insert(0, "2")
        self.entry_n.config(state="readonly")
        self.entry_n.grid(row=0, column=1, padx=5, pady=5)

        self.entry_factorial = tk.Entry(self.ventana, width=10)
        self.entry_factorial.insert(0, "2")
        self.entry_factorial.config(state="readonly")
        self.entry_factorial.grid(row=0, column=3, padx=5, pady=5)

        self.boton = tk.Button(self.ventana, text="Siguiente", command=self.siguiente)
        self.boton.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

        self.ventana.mainloop()

    def siguiente(self):
        self.n += 1
        self.entry_n.config(state="normal")
        self.entry_n.delete(0, tk.END)
        self.entry_n.insert(0, str(self.n))
        self.entry_n.config(state="readonly")

        factorial = 1
        for i in range(1, self.n + 1):
            factorial *= i
        self.entry_factorial.config(state="normal")
        self.entry_factorial.delete(0, tk.END)
        self.entry_factorial.insert(0, str(factorial))
        self.entry_factorial.config(state="readonly")

if __name__ == "__main__":
    Factorial()

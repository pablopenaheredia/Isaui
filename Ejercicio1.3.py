import tkinter as tk

class Factorial:
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.title("Factorial")
        self.n = 2

        self.etiqueta_n = tk.Label(self.raiz, text="n")
        self.etiqueta_n.pack()

        self.entry_n = tk.Entry(self.raiz, width=10)
        self.entry_n.insert(0, "2")
        self.entry_n.config(state="readonly")
        self.entry_n.pack()

        self.etiqueta_factorial = tk.Label(self.raiz, text="Factorial(n)")
        self.etiqueta_factorial.pack()

        self.entry_factorial = tk.Entry(self.raiz, width=10)
        self.entry_factorial.insert(0, "2")
        self.entry_factorial.config(state="readonly")
        self.entry_factorial.pack()

        self.boton = tk.Button(self.raiz, text="Siguiente", command=self.siguiente)
        self.boton.pack()

        self.raiz.mainloop()

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
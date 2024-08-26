import tkinter as tk

class ContDecreciente:
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.title("Contador Decreciente")
        self.contador = 88

        self.etiqueta = tk.Label(self.raiz, text="Contador")
        self.etiqueta.pack()

        self.entry = tk.Entry(self.raiz, width=10)
        self.entry.insert(0, "88")
        self.entry.config(state="readonly")
        self.entry.pack()

        self.boton = tk.Button(self.raiz, text="-", command=self.decrementar)
        self.boton.pack()

        self.raiz.mainloop()

    def decrementar(self):
        self.contador -= 1
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(self.contador))
        self.entry.config(state="readonly")

if __name__ == "__main__":
    ContDecreciente()
import tkinter as tk

class ContCreciente:
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.title("Contador Creciente")
        self.contador = 0

        self.etiqueta = tk.Label(self.raiz, text="Contador")
        self.etiqueta.pack()

        self.entry = tk.Entry(self.raiz, width=10)
        self.entry.insert(0, "0")
        self.entry.config(state="readonly")
        self.entry.pack()

        self.boton = tk.Button(self.raiz, text="+", command=self.incrementar)
        self.boton.pack()

        self.raiz.mainloop()

    def incrementar(self):
        self.contador += 1
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(self.contador))
        self.entry.config(state="readonly")

if __name__ == "__main__":
    ContCreciente()
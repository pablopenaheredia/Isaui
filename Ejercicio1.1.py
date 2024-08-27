import tkinter as tk

class ContCreciente:
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.title("Contador Creciente")
        self.contador = 0

        # Creamos los widgets
        self.etiqueta = tk.Label(self.raiz, text="Contador")
        self.entry = tk.Entry(self.raiz, width=10)
        self.entry.insert(0, "0")
        self.entry.config(state="readonly")
        self.boton = tk.Button(self.raiz, text="+", command=self.incrementar)

        # Los colocamos en la ventana utilizando grid
        self.etiqueta.grid(row=0, column=0, padx=5, pady=5)
        self.entry.grid(row=0, column=1, padx=5, pady=5)
        self.boton.grid(row=0, column=2, padx=5, pady=5)

        self.raiz.mainloop()

    def incrementar(self):
        self.contador += 1
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(self.contador))
        self.entry.config(state="readonly")

if __name__ == "__main__":
    ContCreciente()

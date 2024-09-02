import tkinter as tk

class ContDecreciente:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Contador Decreciente")
        self.contador = 88

        # widgets
        self.titulo = tk.Label(self.ventana, text="Contador")
        self.entry = tk.Entry(self.ventana, width=10)
        self.entry.insert(0, "88")
        self.entry.config(state="readonly")
        self.boton_restar = tk.Button(self.ventana, text="-", command=self.decrementar)

        # estructura
        self.titulo.grid(row=0, column=0, padx=5, pady=5)
        self.entry.grid(row=0, column=1, padx=5, pady=5)
        self.boton_restar.grid(row=0, column=2, padx=5, pady=5)

        self.ventana.mainloop()

    def decrementar(self):
        self.contador -= 1
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(self.contador))
        self.entry.config(state="readonly")

if __name__ == "__main__":
    ContDecreciente()

import tkinter as tk

class ContCreciente:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Contador Creciente")
        self.contador = 0

        # widgets
        self.titulo = tk.Label(self.ventana, text="Contador")
        self.entry = tk.Entry(self.ventana, width=10)
        self.entry.insert(0, "0")
        self.entry.config(state="readonly")
        self.boton_sumar = tk.Button(self.ventana, text="+", command=self.incrementar)

        # estructura
        self.titulo.grid(row=0, column=0, padx=5, pady=5)
        self.entry.grid(row=0, column=1, padx=5, pady=5)
        self.boton_sumar.grid(row=0, column=2, padx=5, pady=5)

        self.ventana.mainloop() 

    def incrementar(self):
        self.contador += 1
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(self.contador))
        self.entry.config(state="readonly")

if __name__ == "__main__":
    ContCreciente()

import tkinter as tk

class Contador:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Contador")
        self.contador = 0

        self.titulo = tk.Label(self.ventana, text="Contador")
        self.titulo.grid(row=0, column=0, padx=5, pady=5)

        self.entry = tk.Entry(self.ventana, width=10)
        self.entry.insert(0, "0")
        self.entry.config(state="readonly")
        self.entry.grid(row=0, column=1, padx=5, pady=5)

        self.boton_up = tk.Button(self.ventana, text="Count Up", command=self.incrementar)
        self.boton_up.grid(row=0, column=2, padx=5, pady=5)

        self.boton_down = tk.Button(self.ventana, text="Count Down", command=self.decrementar)
        self.boton_down.grid(row=0, column=3, padx=5, pady=5)

        self.boton_reset = tk.Button(self.ventana, text="Reset", command=self.reset)
        self.boton_reset.grid(row=0, column=4, padx=5, pady=5)

        self.ventana.mainloop()

    def incrementar(self):
        self.contador += 1
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(self.contador))
        self.entry.config(state="readonly")

    def decrementar(self):
        self.contador -= 1
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(self.contador))
        self.entry.config(state="readonly")

    def reset(self):
        self.contador = 0
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.entry.insert(0, "0")
        self.entry.config(state="readonly")

if __name__ == "__main__":
    Contador()

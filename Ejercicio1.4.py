import tkinter as tk

class Contador:
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.title("Contador")
        self.contador = 0

        self.etiqueta = tk.Label(self.raiz, text="Contador")
        self.etiqueta.pack()

        self.entry = tk.Entry(self.raiz, width=10)
        self.entry.insert(0, "0")
        self.entry.config(state="readonly")
        self.entry.pack()

        self.boton_up = tk.Button(self.raiz, text="Count Up", command=self.incrementar)
        self.boton_up.pack()

        self.boton_down = tk.Button(self.raiz, text="Count Down", command=self.decrementar)
        self.boton_down.pack()

        self.boton_reset = tk.Button(self.raiz, text="Reset", command=self.reset)
        self.boton_reset.pack()

        self.raiz.mainloop()

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
        
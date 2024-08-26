import tkinter as tk

class Notas:
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.title("Notas")

        self.etiqueta_titulo = tk.Label(self.raiz, text="Título")
        self.etiqueta_titulo.pack()

        self.entry_titulo = tk.Entry(self.raiz, width=20)
        self.entry_titulo.pack()

        self.etiqueta_nota = tk.Label(self.raiz, text="Nota")
        self.etiqueta_nota.pack()

        self.text_nota = tk.Text(self.raiz, width=20, height=10)
        self.text_nota.pack()

        self.boton_anadir = tk.Button(self.raiz, text="Añadir", command=self.anadir_nota)
        self.boton_anadir.pack()

        self.listbox_notas = tk.Listbox(self.raiz, width=40)
        self.listbox_notas.pack()

        self.raiz.mainloop()

    def anadir_nota(self):
        titulo = self.entry_titulo.get()
        nota = self.text_nota.get("1.0", tk.END)
        nota_completa = f"{titulo}\n{nota}"
        self.listbox_notas.insert(tk.END, nota_completa)
        self.entry_titulo.delete(0, tk.END)
        self.text_nota.delete("1.0", tk.END)

if __name__ == "__main__":
    Notas()
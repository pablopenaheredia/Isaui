import tkinter as tk

class Peliculas:
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.title("Películas")

        self.etiqueta_titulo = tk.Label(self.raiz, text="Escribe el título de una película")
        self.etiqueta_titulo.pack()

        self.entry_titulo = tk.Entry(self.raiz, width=20)
        self.entry_titulo.pack()

        self.etiqueta_peliculas = tk.Label(self.raiz, text="Películas")
        self.etiqueta_peliculas.pack()

        self.listbox_peliculas = tk.Listbox(self.raiz, width=20)
        self.listbox_peliculas.pack()

        self.boton_anadir = tk.Button(self.raiz, text="Añadir", command=self.anadir_pelicula)
        self.boton_anadir.pack()

        self.raiz.mainloop()

    def anadir_pelicula(self):
        titulo = self.entry_titulo.get()
        self.listbox_peliculas.insert(tk.END, titulo)
        self.entry_titulo.delete(0, tk.END)

if __name__ == "__main__":
    Peliculas()
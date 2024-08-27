import tkinter as tk

class Peliculas:
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.title("Películas")

        # Columna 1
        self.frame_izquierda = tk.Frame(self.raiz)
        self.frame_izquierda.grid(row=0, column=0, padx=10, pady=10)

        self.etiqueta_titulo = tk.Label(self.frame_izquierda, text="Escribe el título de una película")
        self.etiqueta_titulo.grid(row=0, column=0, padx=5, pady=5)

        self.entry_titulo = tk.Entry(self.frame_izquierda, width=20)
        self.entry_titulo.grid(row=1, column=0, padx=5, pady=5)

        self.boton_anadir = tk.Button(self.frame_izquierda, text="Añadir", command=self.anadir_pelicula)
        self.boton_anadir.grid(row=2, column=0, padx=5, pady=5)

        # Columna 2
        self.frame_derecha = tk.Frame(self.raiz)
        self.frame_derecha.grid(row=0, column=1, padx=10, pady=10)

        self.etiqueta_peliculas = tk.Label(self.frame_derecha, text="Películas")
        self.etiqueta_peliculas.grid(row=0, column=0, padx=5, pady=5)

        self.listbox_peliculas = tk.Listbox(self.frame_derecha, width=20)
        self.listbox_peliculas.grid(row=1, column=0, padx=5, pady=5)

        self.raiz.mainloop()

    def anadir_pelicula(self):
        titulo = self.entry_titulo.get()
        self.listbox_peliculas.insert(tk.END, titulo)
        self.entry_titulo.delete(0, tk.END)

if __name__ == "__main__":
    Peliculas()

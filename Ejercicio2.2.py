import tkinter as tk

class Peliculas:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Películas")

        # Panel de entrada
        self.panel_entrada = tk.Frame(self.ventana)
        self.panel_entrada.grid(row=0, column=0, padx=10, pady=10)

        self.label_titulo = tk.Label(self.panel_entrada, text="Escribe el título de una película")
        self.label_titulo.grid(row=0, column=0, padx=5, pady=5)

        self.entry_titulo = tk.Entry(self.panel_entrada, width=20)
        self.entry_titulo.grid(row=1, column=0, padx=5, pady=5)

        self.boton_anadir = tk.Button(self.panel_entrada, text="Añadir", command=self.anadir_pelicula)
        self.boton_anadir.grid(row=2, column=0, padx=5, pady=5)

        # Panel de salida
        self.panel_salida = tk.Frame(self.ventana)
        self.panel_salida.grid(row=0, column=1, padx=10, pady=10)

        self.etiqueta_peliculas = tk.Label(self.panel_salida, text="Películas")
        self.etiqueta_peliculas.grid(row=0, column=0, padx=5, pady=5)

        self.listbox_peliculas = tk.Listbox(self.panel_salida, width=20)
        self.listbox_peliculas.grid(row=1, column=0, padx=5, pady=5)

        self.ventana.mainloop()

    def anadir_pelicula(self):
        titulo = self.entry_titulo.get().strip()
        if titulo:  # verificar que el titulo no este vacio
            if titulo not in self.listbox_peliculas.get(0, tk.END):  # verificar que el titulo no este ya en la lista
                self.listbox_peliculas.insert(tk.END, titulo)
                self.entry_titulo.delete(0, tk.END)
            else:
                #titulo ya existe
                self.entry_titulo.delete(0, tk.END)
                self.entry_titulo.insert(0, "Error: Título ya existe")
        else:
            #titulo vacio
            self.entry_titulo.delete(0, tk.END)
            self.entry_titulo.insert(0, "Error: Título vacío")

if __name__ == "__main__":
    Peliculas()

import tkinter as tk

class Agenda:
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.title("Agenda")

        self.etiqueta_nombre = tk.Label(self.raiz, text="Nombre")
        self.etiqueta_nombre.pack()

        self.entry_nombre = tk.Entry(self.raiz, width=20)
        self.entry_nombre.pack()

        self.etiqueta_telefono = tk.Label(self.raiz, text="Teléfono")
        self.etiqueta_telefono.pack()

        self.entry_telefono = tk.Entry(self.raiz, width=20)
        self.entry_telefono.pack()

        self.etiqueta_direccion = tk.Label(self.raiz, text="Dirección")
        self.etiqueta_direccion.pack()

        self.entry_direccion = tk.Entry(self.raiz, width=20)
        self.entry_direccion.pack()

        self.boton_anadir = tk.Button(self.raiz, text="Añadir", command=self.anadir_contacto)
        self.boton_anadir.pack()

        self.listbox_contactos = tk.Listbox(self.raiz, width=40)
        self.listbox_contactos.pack()

        self.raiz.mainloop()

    def anadir_contacto(self):
        nombre = self.entry_nombre.get()
        telefono = self.entry_telefono.get()
        direccion = self.entry_direccion.get()
        contacto = f"{nombre} - {telefono} - {direccion}"
        self.listbox_contactos.insert(tk.END, contacto)
        self.entry_nombre.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.entry_direccion.delete(0, tk.END)

if __name__ == "__main__":
    Agenda()
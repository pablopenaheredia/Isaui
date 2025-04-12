import tkinter as tk
from tkinter import LabelFrame, Entry, Button 
from tkinter import PhotoImage
from conexionbd import conectar_db

# Ventana
class AltaProducto(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Alta de producto") 
        self.geometry("1200x500")
        self.configure(bg="#40E0D0")
        self.resizable(False, False)
        ruta_imagen = 'C:/Users/GUILLERMINA\Desktop/Interfaces_Peluqueria/imagen3.png'
        self.imagen = PhotoImage(file=ruta_imagen)
        
        self.label_imagen = tk.Label(self, image=self.imagen,bg=self.cget('bg'))
        self.label_imagen.grid(row=2, column=4, rowspan=3, padx=20, pady=10)
        # Marco
        frame_datos = LabelFrame(self, text="Ingrese los datos:", bg="#48D1CC", font=('Calibri', 20), borderwidth=5)
        frame_datos.grid(row=1, column=0, columnspan=9,  ipady=10)

        # Etiquetas
        label_nombre = tk.Label(frame_datos, text="Nombre: ", bg="#48D1CC", fg="black", font=('Calibri', 15))
        label_nombre.grid(row=1, column=1, pady=10)

        label_marca = tk.Label(frame_datos, text="Marca: ", bg="#48D1CC", fg="black", font=('Calibri', 15))
        label_marca.grid(row=2, column=1, pady=10)

        label_cantidad = tk.Label(frame_datos, text="Cantidad: ", bg="#48D1CC", fg="black", font=('Calibri', 15))
        label_cantidad.grid(row=3, column=1, pady=10)

        label_precio = tk.Label(frame_datos, text="Precio: ", bg="#48D1CC", fg="black", font=('Calibri', 15))
        label_precio.grid(row=4, column=1, pady=10)

        # Entradas
        self.entry_nombre = Entry(frame_datos, bg="white", font=('Calibri', 15))
        self.entry_nombre.grid(row=1, column=2, ipadx=400)

        self.entry_marca = Entry(frame_datos, bg="white", font=('Calibri', 15))
        self.entry_marca.grid(row=2, column=2, ipadx=400)

        self.entry_cantidad = Entry(frame_datos, bg="white", font=('Calibri', 15))
        self.entry_cantidad.grid(row=3, column=2, ipadx=400)

        self.entry_precio = Entry(frame_datos, bg="white", font=('Calibri', 15))
        self.entry_precio.grid(row=4, column=2, ipadx=400)


        # Botón de Envío
        btn_guardar = Button(frame_datos, text="Guardar", command=self.guardar_datos, bg="green", font=('Calibri', 15))
        btn_guardar.grid(row=9, column=1, columnspan=2, pady=20)

    def guardar_datos(self):
        cnx = conectar_db()
        cursor = cnx.cursor()

        nombre = self.entry_nombre.get()
        marca = self.entry_marca.get()
        cantidad = self.entry_cantidad.get()
        precio = self.entry_precio.get()

        query = "INSERT INTO producto (nombre, marca, cantidad, precio) VALUES (%s, %s, %s, %s)"
        valores = (nombre, marca, cantidad, precio)

        cursor.execute(query, valores)
        cnx.commit()

        print("Datos Guardados")
        cursor.close()
        cnx.close() 

if __name__ == "__main__":
    app = AltaProducto()
    app.mainloop()

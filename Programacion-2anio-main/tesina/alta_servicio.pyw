import tkinter as tk
from tkinter import LabelFrame, Entry, Button, StringVar, PhotoImage,messagebox
from conexionbd import conectar_db
import mysql.connector


def insertar_servicio(descripcion,tiempo_estimado,nombre):
    mydb = conectar_db()
    if mydb is None:
        return  # Si no se pudo conectar, salimos

    mycursor = mydb.cursor()
    try:
         sql = "INSERT INTO servicio (descripcion, tiempo_estimado,nombre) VALUES (%s, %s, %s)"
         val = (descripcion,tiempo_estimado,nombre)
         mycursor.execute(sql, val)
         mydb.commit()
         print("Registro insertado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al insertar en la base de datos: {err}")
    finally:
        mycursor.close()
        mydb.close()


# Ventana
class AltaServicio(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__()
        self.title("Alta de persona") 
        self.geometry("1250x500")
        self.configure(bg="#40E0D0")
        self.resizable(False, False)
        ruta_imagen = 'C:/Users/GUILLERMINA/Desktop/Interfaces_Peluqueria/imagen3.png'
        self.imagen = PhotoImage(file=ruta_imagen)
        
        self.label_imagen = tk.Label(self, image=self.imagen, bg=self.cget('bg'))
        self.label_imagen.grid(row=2, column=4, rowspan=3, padx=20, pady=10)

        # Marco
        frame_datos = LabelFrame(self, text="Ingrese los datos:", bg="#48D1CC", font=('Calibri', 20), borderwidth=5)
        frame_datos.grid(row=1, column=0, columnspan=9, ipady=10)

        # Etiquetas
        label_nombre = tk.Label(frame_datos, text="Nombre: ", bg="#48D1CC", fg="black", font=('Calibri', 15))
        label_nombre.grid(row=1, column=1, pady=10)

        label_descripcion= tk.Label(frame_datos, text="Descripcion: ", bg="#48D1CC", fg="black", font=('Calibri', 15))
        label_descripcion.grid(row=2, column=1, pady=10)
        
        label_tiempoestimado = tk.Label(frame_datos, text="Tiempo Estimado: ", bg="#48D1CC", fg="black", font=('Calibri', 15))
        label_tiempoestimado.grid(row=3, column=1, pady=10)
       
        # Entradas
        self.entry_nombre = Entry(frame_datos, bg="white", font=('Calibri', 15))
        self.entry_nombre.grid(row=1, column=2, ipadx=400)

        self.entry_descripcion= Entry(frame_datos, bg="white", font=('Calibri', 15))
        self.entry_descripcion.grid(row=2, column=2, ipadx=400)
        
        self.entry_tiempoestimado = Entry(frame_datos, bg="white", font=('Calibri', 15))
        self.entry_tiempoestimado.grid(row=3, column=2, ipadx=400)

        # Botón de Envío
        self.btn_guardar = Button(frame_datos, text="Guardar", command=self.guardar_datos, bg="light grey", font=('Calibri', 15))
        self.btn_guardar.grid(row=9, column=1, columnspan=2, pady=20)
        self.btn_guardar = Button(frame_datos, text="Limpiar", command=self.limpiar_campos, bg="light grey", font=('Calibri', 15))
        self.btn_guardar.grid(row=9, column=2, columnspan=2, padx=500,pady=20)
    

    
    
    def guardar_datos(self):
        self.btn_guardar.config(state=tk.DISABLED)
        Nombre= self.entry_nombre.get()
        Descripcion = self.entry_descripcion.get()
        Tiempo_Estimado = self.entry_tiempoestimado.get()
        
        if Nombre and Descripcion and Tiempo_Estimado:        
            insertar_servicio(Descripcion,Tiempo_Estimado,Nombre)
            messagebox.showinfo("Éxito", "Registro guardado en la base de datos.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
    
        # Reactivar el botón después de un breve tiempo (opcional)
        self.after(2000, lambda: self.btn_guardar.config(state=tk.NORMAL))
    def limpiar_campos( entries):
        for entry in entries:
            entry.delete(0, tk.END)

if __name__ == "__main__":
    app = AltaServicio()
    app.mainloop()

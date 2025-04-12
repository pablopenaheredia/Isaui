import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage  
from Menu import Menu
from conexionbd import conectar_db
import mysql.connector  # Agregué esta línea

class Sesion(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("500x300")  
        self.resizable(False, False)
        self.configure(bg="#40E0D0")  
        self.title("Inicio de Sesión")

        
        ruta_imagen = 'C:/Users/lauta/OneDrive/Desktop/Facultad/Interfaces_Peluqueria/imagen3.png'
        self.imagen = PhotoImage(file=ruta_imagen)
        
        self.label_imagen = tk.Label(self, image=self.imagen,bg=self.cget('bg'))
        self.label_imagen.grid(row=2, column=1, rowspan=3, padx=20, pady=40)
        
        self.etiqueta1 = tk.Label(self, text="Usuario", font=("Calibri", 20), bg=self.cget('bg'), fg="black")
        self.etiqueta1.grid(row=0, column=0, padx=20, pady=20)
        self.etiqueta2 = tk.Label(self, text="Contraseña", font=("Calibri", 20), bg=self.cget('bg'), fg="black")
        self.etiqueta2.grid(row=1, column=0, padx=20, pady=20)

        
        self.mostrador_usuario = tk.Entry(self, state="normal", font=("Calibri", 15))
        self.mostrador_usuario.grid(row=0, column=1, padx=20, pady=20)
        self.mostrador_contraseña = tk.Entry(self, show="*", state="normal", font=("Calibri", 15))
        self.mostrador_contraseña.grid(row=1, column=1, padx=20, pady=20)

        
        self.boton = tk.Button(self, text="Ingresar", command=self.verificar_sesion, font=("Calibri", 12))
        self.boton.grid(row=2, column=1, padx=10, pady=1)
        self.conn = mysql.connector.connect(
            user='root',
            password='123',  # Reemplaza 'tu_contraseña' con la contraseña real
            host='localhost',
            database='base_peluqueria'
            )
    

    def verificar_sesion(self):
        mydb = conectar_db()
        if mydb is None:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos")
            return

        cursor = mydb.cursor()
        usuario_ingresado = self.mostrador_usuario.get()
        contraseña_ingresada = self.mostrador_contraseña.get()

        query = "SELECT * FROM usuarios WHERE nombre_usuario = %s AND contraseña = %s"
        cursor.execute(query, (usuario_ingresado, contraseña_ingresada))

        if cursor.fetchone():
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
            self.abrir_menu_principal()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

        cursor.close()
        mydb.close()

    def abrir_menu_principal(self):
        self.destroy()  # Cierra la ventana de inicio de sesión
        menu = Menu()  # Abre el menú principal desde el otro archivo
        menu.mainloop()

ventana = Sesion()
ventana.mainloop()

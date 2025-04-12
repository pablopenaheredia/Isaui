import re
import tkinter as tk
from tkinter import LabelFrame, Entry, Button, StringVar, PhotoImage,messagebox
from tkinter.ttk import Combobox  
from conexionbd import insertar_persona


# Ventana
class AltaPersona(tk.Toplevel):
    def __init__(self,master=None, actualizar_treeview=None):
        super().__init__(master)
        self.parent=master
        self.title("Alta de persona") 
        self.geometry("1180x610")
        self.configure(bg="#40E0D0")
        self.actualizar_treeview = actualizar_treeview
        self.resizable(False, False)
        ruta_imagen = 'C:/Users/GUILLERMINA\Desktop/Interfaces_Peluqueria/imagen3.png'
        self.imagen = PhotoImage(file=ruta_imagen)
        
        self.label_imagen = tk.Label(self, image=self.imagen, bg=self.cget('bg'))
        self.label_imagen.grid(row=2, column=4, rowspan=3, padx=20, pady=10)
        self.tipo_to_id = {
            "Cliente": 1,  # ID correspondiente a Cliente
            "Empleado": 2  # ID correspondiente a Empleado
        }

        # Marco
        frame_datos = LabelFrame(self, text="Ingrese los datos:", bg="#48D1CC", font=('Calibri', 20), borderwidth=5)
        frame_datos.grid(row=1, column=0, columnspan=9, ipady=10)

        # Etiquetas
        label_nombre = tk.Label(frame_datos, text="Nombre: ", bg="#48D1CC", fg="black", font=('Calibri', 15))
        label_nombre.grid(row=1, column=1, pady=10)

        label_apellido = tk.Label(frame_datos, text="Apellido: ", bg="#48D1CC", fg="black", font=('Calibri', 15))
        label_apellido.grid(row=2, column=1, pady=10)

        label_dni = tk.Label(frame_datos, text="DNI: ", bg="#48D1CC", fg="black", font=('Calibri', 15))
        label_dni.grid(row=3, column=1, pady=10)

        label_contacto = tk.Label(frame_datos, text="Contacto: ", bg="#48D1CC", fg="black", font=('Calibri', 15))
        label_contacto.grid(row=4, column=1, pady=10)

        label_correo = tk.Label(frame_datos, text="Correo: ", bg="#48D1CC", fg="black", font=('Calibri', 15))
        label_correo.grid(row=5, column=1, pady=10)
        
        label_tipo = tk.Label(frame_datos, text="Tipo: ", bg="#48D1CC", fg="black", font=('Calibri', 15))
        label_tipo.grid(row=6, column=1, pady=10)

        label_activo = tk.Label(frame_datos, text="Activo: ", bg="#48D1CC", fg="black", font=('Calibri', 15))
        label_activo.grid(row=7, column=1, pady=10)


        # Entradas
        self.entry_nombre = Entry(frame_datos, bg="white", font=('Calibri', 15))
        self.entry_nombre.grid(row=1, column=2, ipadx=400)

        self.entry_apellido = Entry(frame_datos, bg="white", font=('Calibri', 15))
        self.entry_apellido.grid(row=2, column=2, ipadx=400)

        self.entry_dni = Entry(frame_datos, bg="white", font=('Calibri', 15))
        self.entry_dni.grid(row=3, column=2, ipadx=400)

        self.entry_contacto = Entry(frame_datos, bg="white", font=('Calibri', 15))
        self.entry_contacto.grid(row=4, column=2, ipadx=400)

        self.entry_correo = Entry(frame_datos, bg="white", font=('Calibri', 15))
        self.entry_correo.grid(row=5, column=2, ipadx=400)

        
        # Combobox para seleccionar tipo de persona
        tipo_var = StringVar(self)
        self.tipo_combobox = Combobox(frame_datos, textvariable=tipo_var, state="readonly", font=('Calibri', 15))
        self.tipo_combobox['values'] = ("Cliente", "Empleado")  # Opciones del combobox
        self.tipo_combobox.set("")  
        self.tipo_combobox.grid(row=6, column=2, ipadx=390)

        self.activo_var = StringVar(value="1")
        self.radio_si = tk.Radiobutton(frame_datos, text="Sí", variable=self.activo_var, value="1", bg="#48D1CC", font=('Calibri', 15))
        self.radio_no = tk.Radiobutton(frame_datos, text="No", variable=self.activo_var, value="0", bg="#48D1CC", font=('Calibri', 15),state="disabled")
        self.radio_si.grid(row=7, column=2, sticky="w", padx=400)
        self.radio_no.grid(row=7, column=2,  padx=10)
        
        self.btn_guardar = Button(frame_datos, text="Guardar", command=self.guardar_datos, bg="light grey", font=('Calibri', 15))
        self.btn_guardar.grid(row=9, column=2, columnspan=2, padx=400,pady=20,sticky="w")
        self.btn_Limpiar = Button(frame_datos, text="Limpiar", command=self.limpiar_campos, bg="light grey", font=('Calibri', 15))
        self.btn_Limpiar.grid(row=9, column=2, columnspan=3,padx=500,  pady=20,sticky="e")
    
        self.cursor = self.conn.cursor()
    
    def guardar_datos(self):
     print("Guardar datos llamado")
    # Desactivar el botón para evitar múltiples clics
     self.btn_guardar.config(state=tk.DISABLED)

     nombre = self.entry_nombre.get()
     apellido = self.entry_apellido.get()
     dni = self.entry_dni.get()
     contacto = self.entry_contacto.get()
     correo = self.entry_correo.get() 
     tipo = self.tipo_combobox.get()
     activo = 1 if self.activo_var.get() == "1" else 0 

    # Validaciones
     if not self.validar_dni(dni):
        self.btn_guardar.config(state=tk.NORMAL)
        return
     if not self.verificar_correo(correo):
        self.btn_guardar.config(state=tk.NORMAL)
        return
     if not self.validar_telefono(contacto):
        self.btn_guardar.config(state=tk.NORMAL)
        return
    
     if nombre and apellido and dni and contacto and tipo:
        id_tipo_p = self.tipo_to_id[tipo]  # Obtener el id_tipo_p correspondiente
        insertar_persona(nombre, apellido, dni, contacto, activo, tipo, id_tipo_p, correo)
        self.parent.mydb.commit()
        
        # Llama a load_personas para actualizar la lista en ViewPersonas
        self.parent.load_personas()
        messagebox.showinfo("Éxito", "Registro guardado en la base de datos.")
        
     else:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
     

     # Reactivar el botón después de un breve tiempo (opcional)
     self.after(2000, lambda: self.btn_guardar.config(state=tk.NORMAL))
    
 
    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellido.delete(0, tk.END)
        self.entry_dni.delete(0, tk.END)
        self.entry_contacto.delete(0, tk.END)
        self.entry_correo.delete(0, tk.END)
        self.tipo_combobox.set("") 
        self.activo_var.set("1") 
            
#Funciones de validacion
    def verificar_correo(self,correo):
    # Expresión regular para validar el formato del correo electrónico
     patron = r'^[a-zA-ZñÑ0-9._%+-]+@[a-zA-ZñÑ0-9.-]+\.[a-zA-ZñÑ]{2,}$'

    # Comprobar si el correo cumple con el patrón
     if not re.match(patron, correo):
        messagebox.showerror("Error", f"{correo} : no es una dirección de correo válida.")
        return False
     return True
    
    def validar_dni(self,dni):
    
     if not dni.isdigit():  # Verifica si el DNI tiene solo números
        messagebox.showerror("Error", "Solamente se aceptan dígitos en el dni")
        return False
     elif len(dni) < 7 or len(dni) > 8:  # Verifica que el DNI tenga 7 u 8 dígitos
        messagebox.showerror("Error", "El número del dni debe tener 7 u 8 dígitos")
        return   False   
     return True

    def validar_telefono(self,contacto):
      if not contacto.isdigit():  
        messagebox.showerror("Error", "Solamente se aceptan dígitos en contacto")
        return False
      elif len(contacto) < 6 or len(contacto) > 10:
        messagebox.showerror("Error", "El número de teléfono debe tener entre 6 y 10 dígitos")
        return False
      return True

if __name__ == "__main__":
    app = AltaPersona()
    app.mainloop()



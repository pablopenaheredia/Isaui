import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox
import mysql.connector

class ViewPersonas(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#008B8B", width=1366, height=768)
        self.master = master
        self.grid_propagate(False)  # Evita que el frame cambie de tamaño
        self.grid(row=0, column=0, sticky="nsew")
        ruta_imagen = 'C:/Users/GUILLERMINA/Desktop/Interfaces_Peluqueria/imagen3.png'
        self.imagen = PhotoImage(file=ruta_imagen)
        
        self.label_imagen = tk.Label(self, image=self.imagen, bg=self.cget('bg'))
        self.label_imagen.grid(row=4, column=0, rowspan=3, padx=20, pady=10)

        # Conectar a la base de datos y crear un cursor
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",  # Cambia esto por tu usuario
            password="",  # Cambia esto por tu contraseña
            database="base_peluquerias"  # Cambia esto por tu base de datos
        )
        self.mycursor = self.mydb.cursor()

        self.create_widgets()

    def create_widgets(self):
        # Frame de búsqueda
        search_frame = tk.LabelFrame(self, text="Buscar por DNI", bg="#008B8B", font=('Calibri', 20), borderwidth=5)
        search_frame.grid(row=0, column=0, padx=70, pady=20, sticky="ew")

        # Entrada de búsqueda
        self.search_entry = tk.Entry(search_frame, width=20, font=('Calibri', 15))
        self.search_entry.grid(row=0, column=0, padx=10, pady=10)

        # Botones de acción
        search_button = tk.Button(search_frame, text="Buscar", command=self.search_personas, bg="#ffffff", font=('Calibri', 15), width=8)
        search_button.grid(row=0, column=1, padx=10, pady=10)
        
        search_button = tk.Button(search_frame, text="+ Agregar", command=self.abrir_altap, bg="#ffffff", font=('Calibri', 15), width=8)
        search_button.grid(row=0, column=2, padx=10, pady=10)

        search_button = tk.Button(search_frame, text="Modificar", command=self.modificar_persona, bg="#ffffff", font=('Calibri', 15), width=8)
        search_button.grid(row=0, column=3, padx=10, pady=10)
        
        search_button = tk.Button(search_frame, text="Eliminar", command=self.eliminar_persona, bg="#ffffff", font=('Calibri', 15), width=8)
        search_button.grid(row=0, column=4, padx=10, pady=10)

        back_button = tk.Button(self, text="Volver", command=self.volver_menu, bg="#ffffff", font=('Calibri', 15), width=8)
        back_button.grid(row=2, column=0, padx=10, pady=10)

        style = ttk.Style()
        style.configure("Treeview",
                        background="#ffffff",
                        foreground="#000000",
                        rowheight=25,
                        fieldbackground="#ffffff")
        
        # Treeview de personas
        self.personas_treeview = ttk.Treeview(self, columns=("dni", "nombre", "apellido", "contacto", "correo", "tipo", "activo", "id_tipo_p", "id_turno"), show="headings")
        self.personas_treeview.grid(row=1, column=0, sticky="nsew", padx=70, pady=10)

        # Configuración del Treeview
        self.personas_treeview.heading("nombre", text="Nombre")
        self.personas_treeview.heading("apellido", text="Apellido")
        self.personas_treeview.heading("dni", text="DNI")
        self.personas_treeview.heading("contacto", text="Contacto")
        self.personas_treeview.heading("correo", text="Correo")
        self.personas_treeview.heading("tipo", text="Tipo")
        self.personas_treeview.heading("activo", text="Activo")
        self.personas_treeview.heading("id_tipo_p", text="Tipo ID")
        self.personas_treeview.heading("id_turno", text="Turno ID")

        # Ancho de las columnas y datos centrados
        self.personas_treeview.column("nombre", anchor='center', width=150)
        self.personas_treeview.column("apellido", anchor='center', width=150)
        self.personas_treeview.column("dni", anchor='center', width=150)
        self.personas_treeview.column("contacto", anchor='center', width=150)
        self.personas_treeview.column("correo", anchor='center', width=150)
        self.personas_treeview.column("tipo", anchor='center', width=150)
        self.personas_treeview.column("activo", anchor='center', width=100)
        self.personas_treeview.column("id_tipo_p", anchor='center', width=100)
        self.personas_treeview.column("id_turno", anchor='center', width=100)

        # Carga los datos iniciales
        self.load_personas()

    def load_personas(self):
        self.mycursor.execute("SELECT * FROM persona WHERE activo = 'si'")  # Filtrar solo activos
        personas = self.mycursor.fetchall()
        self.personas_treeview.delete(*self.personas_treeview.get_children())  # Limpiar el Treeview antes de cargar
        for persona in personas:
            values = (persona[3], persona[1], persona[2], persona[4], persona[9], persona[5], persona[6], persona[7], persona[8])
            self.personas_treeview.insert("", "end", values=values)

    def search_personas(self):
        dni = self.search_entry.get()
        if dni:
            self.mycursor.execute("SELECT * FROM persona WHERE dni = %s", (dni,))  
            personas = self.mycursor.fetchall()
            self.personas_treeview.delete(*self.personas_treeview.get_children())  
            for persona in personas:
                values = (persona[3], persona[1], persona[2], persona[4], persona[9], persona[5], persona[6], persona[7], persona[8])
                self.personas_treeview.insert("", "end", values=values)

    def modificar_persona(self):
        selected_item = self.personas_treeview.selection()  # Obtiene el item seleccionado
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una persona para modificar.")
            return  

        persona_dni = self.personas_treeview.item(selected_item, 'values')[0]  # Obtiene el DNI del item seleccionado
        self.mycursor.execute("SELECT * FROM persona WHERE dni = %s", (persona_dni,))
        persona = self.mycursor.fetchone()  #Datos de persona

        if persona:
            ModificarPersona(self, persona)  # Abrir la ventana de modificación
        else:
            messagebox.showerror("Error", "Persona no encontrada.")
        

    def eliminar_persona(self): 
        selected_item = self.personas_treeview.selection()  
        if not selected_item:  # Verifica si no hay selección
            messagebox.showwarning("Advertencia", "Por favor, selecciona una persona para eliminar.")  
            return  # Salir si no hay selección

        persona_dni = self.personas_treeview.item(selected_item, 'values')[0]  
        confirm = messagebox.askyesno("Confirmar Eliminación", f"¿Estás seguro de que deseas eliminar a la persona con DNI {persona_dni}?")
        if confirm:
            self.mycursor.execute("UPDATE persona SET activo = 'no' WHERE dni = %s", (persona_dni,))
            self.mydb.commit()  #
           
        self.load_personas() 
    def abrir_altap(self):
        from alta_persona2 import AltaPersona
        alta = AltaPersona(self)  # Crea una nueva ventana de alta persona
        alta.transient(self)  # Hacer que sea una ventana secundaria
        alta.grab_set()
        

    def volver_menu(self):
        self.mycursor.close()
        self.mydb.close()
        self.master.destroy()  # Cierra la ventana actual
        from Menu import Menu  # Importa la clase Menu
        menu = Menu()  # Crea una instancia de Menu
        menu.mainloop()

class ModificarPersona:
    def __init__(self, parent, persona):
        self.parent = parent
        self.persona = persona

        # Crear la ventana de modificación
        self.window = tk.Toplevel(parent.master)
        self.window.title("Modificar Persona")
        self.window.geometry("400x400")
        self.window.configure(bg="#008B8B")

        self.create_widgets()

    def create_widgets(self):
        
        tk.Label(self.window, text="Nombre:", bg="#008B8B").pack(pady=5)
        self.nombre_entry = tk.Entry(self.window)
        self.nombre_entry.insert(0, self.persona[1])  # Cargar el nombre actual
        self.nombre_entry.pack(pady=5)

        tk.Label(self.window, text="Apellido:", bg="#008B8B").pack(pady=5)
        self.apellido_entry = tk.Entry(self.window)
        self.apellido_entry.insert(0, self.persona[2])  # Cargar el apellido actual
        self.apellido_entry.pack(pady=5)

        tk.Label(self.window, text="Contacto:", bg="#008B8B").pack(pady=5)
        self.contacto_entry = tk.Entry(self.window)
        self.contacto_entry.insert(0, self.persona[4])  # Cargar el contacto actual
        self.contacto_entry.pack(pady=5)

        tk.Label(self.window, text="Correo:", bg="#008B8B").pack(pady=5)
        self.correo_entry = tk.Entry(self.window)
        self.correo_entry.insert(0, self.persona[9])  # Cargar el correo actual
        self.correo_entry.pack(pady=5)
        
        tk.Label(self.window, text="Activo:", bg="#008B8B").pack(pady=5)
        self.activo_var = tk.StringVar(value="1" if self.persona[7] == 1 else "0")  
        self.radio_si = tk.Radiobutton(self.window, text="Sí", variable=self.activo_var, value="1", bg="#008B8B")
        self.radio_si.pack(pady=5)

        self.activo_var.set("1")  
        # Botón para confirmar modificación
        modificar_button = tk.Button(self.window, text="Modificar", command=self.modificar_persona)
        modificar_button.pack(pady=20)

    def modificar_persona(self):
        # Recoge los datos de las entradas
        nuevo_nombre = self.nombre_entry.get()
        nuevo_apellido = self.apellido_entry.get()
        nuevo_contacto = self.contacto_entry.get()
        nuevo_correo = self.correo_entry.get()
        
        nuevo_activo = "sí"

        # Actualizar en la base de datos
        self.parent.mycursor.fetchall() 
        self.parent.mycursor.execute("""
            UPDATE persona SET nombre = %s, apellido = %s, contacto = %s, correo = %s , activo=%s
            WHERE dni = %s
        """, (nuevo_nombre, nuevo_apellido, nuevo_contacto, nuevo_correo,nuevo_activo, self.persona[3]))  # Usar el DNI para identificar a la persona
        self.parent.mydb.commit()

        messagebox.showinfo("Éxito", "Persona modificada con éxito.")
        self.parent.load_personas()  # Recargar la lista de personas
        self.window.destroy()  # Cerrar la ventana de modificación

if __name__ == "__main__":
    root = tk.Tk()
    app = ViewPersonas(master=root)
    app.mainloop()

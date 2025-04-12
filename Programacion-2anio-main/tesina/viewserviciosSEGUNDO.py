import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

class VerServicios(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#40E0D0", width=1280, height=720)
        self.master = master
        self.grid_propagate(False)
        self.grid(row=0, column=0, sticky="nsew")

        # Conectar a la base de datos y crear un cursor
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="base_peluquerias"
        )
        self.mycursor = self.mydb.cursor()

        self.crear_widgets()

    def crear_widgets(self):
        # Frame de búsqueda
        marco_busqueda = tk.LabelFrame(self, text="Buscar por nombre", bg="#40E0D0", font=('Calibri', 20), borderwidth=5)
        marco_busqueda.grid(row=0, column=0, padx=10, pady=20, sticky="nsew")

        # Entrada de búsqueda
        self.entrada_busqueda = tk.Entry(marco_busqueda, width=20, font=('Calibri', 15))
        self.entrada_busqueda.grid(row=0, column=0, padx=10, pady=10)

        # Botón de búsqueda
        boton_buscar = tk.Button(marco_busqueda, text="Buscar", command=self.buscar_servicios, bg="#ffffff", font=('Calibri', 15), width=8)
        boton_buscar.grid(row=0, column=1, padx=10, pady=10)

        # Botón de agregar
        boton_agregar = tk.Button(marco_busqueda, text="+Agregar", command=self.abrir_alta, bg="#ffffff", font=('Calibri', 15), width=8)
        boton_agregar.grid(row=0, column=2, padx=10, pady=10)

        # Botón de eliminar
        boton_eliminar = tk.Button(marco_busqueda, text="Eliminar", command=self.eliminar_servicio, bg="#ffffff", font=('Calibri', 15), width=8)
        boton_eliminar.grid(row=0, column=3, padx=10, pady=10)

        # Botón de modificar
        boton_modificar = tk.Button(marco_busqueda, text="Modificar", command=self.modificar_servicio, bg="#ffffff", font=('Calibri', 15), width=8)
        boton_modificar.grid(row=0, column=4, padx=10, pady=10)

        # Treeview de servicios
        self.treeview_servicios = ttk.Treeview(self, columns=("nombre", "descripcion", "Tiempo Estimado"), show="headings")
        self.treeview_servicios.grid(row=1, column=0, sticky="nsew", padx=130, pady=10)

        # Configuración del Treeview
        self.treeview_servicios.heading("nombre", text="Nombre")
        self.treeview_servicios.heading("descripcion", text="Descripción")
        self.treeview_servicios.heading("Tiempo Estimado", text="Tiempo Estimado")

        # Ancho de las columnas y datos centrados
        self.treeview_servicios.column("nombre", anchor='center', width=150)
        self.treeview_servicios.column("descripcion", anchor='center', width=200)
        self.treeview_servicios.column("Tiempo Estimado", anchor='center', width=100)

        # Botón Volver
        boton_volver = tk.Button(self, text="Volver", command=self.volver_menu, bg="#ffffff", font=('Calibri', 15), width=8)
        boton_volver.grid(row=2, column=0, padx=10, pady=20)

        # Carga los servicios
        self.cargar_servicios()

    def cargar_servicios(self):
        self.mycursor.execute("SELECT * FROM servicio")
        servicios = self.mycursor.fetchall()
        self.treeview_servicios.delete(*self.treeview_servicios.get_children())
        for servicio in servicios:
            self.treeview_servicios.insert("", "end", values=(servicio[3], servicio[1], servicio[2]))

    def buscar_servicios(self):
     nombre = self.entrada_busqueda.get().upper()  # Normalizar a mayúsculas
     if nombre:
        # Cambiar la consulta para usar LIKE y buscar por el prefijo
        self.mycursor.execute("SELECT * FROM servicio WHERE nombre LIKE %s", (nombre + '%',))
        servicios = self.mycursor.fetchall()
        self.treeview_servicios.delete(*self.treeview_servicios.get_children())
    
        for servicio in servicios:
            self.treeview_servicios.insert("", "end", values=(servicio[3], servicio[1], servicio[2]))
        self.entrada_busqueda.delete(0, tk.END)  # Limpiar el campo de búsqueda
     else:
        # Si el campo de búsqueda está vacío, recargar todos los servicios
        self.cargar_servicios()
    def eliminar_servicio(self):
        item_seleccionado = self.treeview_servicios.selection()
        if item_seleccionado:
            servicio_nombre = self.treeview_servicios.item(item_seleccionado, 'values')[0]
            self.mycursor.execute("DELETE FROM servicio WHERE nombre = %s", (servicio_nombre,))
            self.mydb.commit()
            self.treeview_servicios.delete(item_seleccionado)
            messagebox.showinfo("Éxito", "Servicio eliminado correctamente.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un servicio para eliminar.")

    def modificar_servicio(self):
        item_seleccionado = self.treeview_servicios.selection()
        if item_seleccionado:
            servicio_nombre = self.treeview_servicios.item(item_seleccionado, 'values')[0]
            # Abrir un cuadro de diálogo para modificar el servicio
            self.abrir_dialogo_modificar(servicio_nombre)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un servicio para modificar.")

    def abrir_dialogo_modificar(self, servicio_nombre):
    # Obtener los detalles del servicio seleccionado
     self.mycursor.execute("SELECT * FROM servicio WHERE nombre = %s", (servicio_nombre,))
     servicio = self.mycursor.fetchone()

    # Crear una nueva ventana para modificar el servicio
     ventana_modificar = tk.Toplevel(self)
     ventana_modificar.title("Modificar Servicio")
     ventana_modificar.geometry("400x400")
     ventana_modificar.configure(bg="#40E0D0")
     ventana_modificar.protocol("WM_DELETE_WINDOW", lambda: None)  # Deshabilitar el botón de cerrar

     tk.Label(ventana_modificar, text="Nombre:", font=('Calibri', 12), bg="#40E0D0").pack(pady=10)
     entrada_nombre = tk.Entry(ventana_modificar, font=('Calibri', 12))
     entrada_nombre.insert(0, servicio[3])  # nombre
     entrada_nombre.pack(pady=10)

     tk.Label(ventana_modificar, text="Descripción:", font=('Calibri', 12), bg="#40E0D0").pack(pady=10)
     entrada_descripcion = tk.Text(ventana_modificar, font=('Calibri', 12), height=5, width=40)  # Especificar el ancho
     entrada_descripcion.insert(tk.END, servicio[1])  # descripción
     entrada_descripcion.pack(pady=10, padx=10)  # Agregar padding horizontal

     tk.Label(ventana_modificar, text="Tiempo Estimado:", font=('Calibri', 12), bg="#40E0D0").pack(pady=10)
     entrada_tiempo = tk.Entry(ventana_modificar, font=('Calibri', 12))
     entrada_tiempo.insert(0, servicio[2])  # tiempo estimado
     entrada_tiempo.pack(pady=10)

     def guardar_cambios():
        nuevo_nombre = entrada_nombre.get().upper()  # Normalizar a mayúsculas
        nueva_descripcion = entrada_descripcion.get("1.0", tk.END).strip()  # Obtener texto del campo de texto
        nuevo_tiempo = entrada_tiempo.get()

        # Validar que no existan campos vacíos
        if not nuevo_nombre or not nueva_descripcion or not nuevo_tiempo:
            messagebox.showwarning("Advertencia", "Todos los campos deben ser llenados.")
            return

        # Validar que no exista un servicio con el mismo nombre
        self.mycursor.execute("SELECT * FROM servicio WHERE nombre = %s", (nuevo_nombre,))
        if self.mycursor.fetchone() and nuevo_nombre != servicio[3]:
            messagebox.showwarning("Advertencia", "El servicio ya existe con ese nombre.")
            return

        # Actualizar el servicio en la base de datos
        self.mycursor.execute("UPDATE servicio SET nombre = %s, descripcion = %s, tiempo_estimado = %s WHERE nombre = %s",
                              (nuevo_nombre, nueva_descripcion, nuevo_tiempo, servicio[3]))
        self.mydb.commit()
        ventana_modificar.destroy()
        self.cargar_servicios()
        messagebox.showinfo("Éxito", "Servicio modificado correctamente.")

     boton_guardar = tk.Button(ventana_modificar, text="Guardar Cambios", command=guardar_cambios)
     boton_guardar.pack(pady=20)
    def abrir_alta(self):
        ventana_alta = tk.Toplevel(self)
        ventana_alta.title("Agregar Servicio")
        ventana_alta.geometry("400x350")
        ventana_alta.configure(bg="#40E0D0")
        ventana_alta.resizable(False,False)
        #ventana_alta.protocol("WM_DELETE_WINDOW", lambda: None)  # Deshabilitar el botón de cerrar

        tk.Label(ventana_alta, text="Nombre:", font=('Calibri', 12), bg="#40E0D0").pack(pady=10)
        entrada_nombre = tk.Entry(ventana_alta, font=('Calibri', 12))
        entrada_nombre.pack(pady=10)

        tk.Label(ventana_alta, text="Descripción:", font=('Calibri', 12), bg="#40E0D0").pack(pady=10)
        entrada_descripcion = tk.Entry(ventana_alta, font=('Calibri', 12))
        entrada_descripcion.pack(pady=10)

        tk.Label(ventana_alta, text="Tiempo Estimado:", font=('Calibri', 12), bg="#40E0D0").pack(pady=10)
        entrada_tiempo = tk.Entry(ventana_alta, font=('Calibri', 12))
        entrada_tiempo.pack(pady=10)

        def guardar_servicio():
            nombre = entrada_nombre.get().upper()  # Normalizar a mayúsculas
            descripcion = entrada_descripcion.get().upper()
            tiempo_estimado = entrada_tiempo.get()

            # Validar que no existan campos vacíos
            if not nombre or not descripcion or not tiempo_estimado:
                messagebox.showwarning("Advertencia", "Todos los campos deben ser llenados.")
                return

            # Validar que no exista un servicio con el mismo nombre
            self.mycursor.execute("SELECT * FROM servicio WHERE nombre = %s", (nombre,))
            if self.mycursor.fetchone():
                messagebox.showwarning("Advertencia", "Ya existe un servicio con ese nombre.")
                return

            # Insertar el nuevo servicio en la base de datos
            self.mycursor.execute("INSERT INTO servicio (nombre, descripcion, tiempo_estimado) VALUES (%s, %s, %s)",
                                  (nombre, descripcion, tiempo_estimado))
            self.mydb.commit()
            ventana_alta.destroy()
            self.cargar_servicios()
            messagebox.showinfo("Éxito", "Servicio agregado correctamente.")

        boton_guardar = tk.Button(ventana_alta, text="Guardar Servicio", command=guardar_servicio)
        boton_guardar.pack(pady=20)

    def volver_menu(self):
        # Implementar la lógica para volver al menú principal
        pass

# Crear la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = VerServicios(master=root)
    app.mainloop()

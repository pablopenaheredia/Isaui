import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import mysql.connector
from tkinter import messagebox
from datetime import datetime  # Importar datetime

# Conexión a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
    database="base_peluqueria"
)
cursor = db.cursor()

# Función para mostrar turnos filtrados por fecha
def mostrar_turnos(fecha=None):
    for row in tree.get_children():
        tree.delete(row)

    if fecha:
        cursor.execute("SELECT fecha, hora, nombre_cliente, nombre FROM turno JOIN servicio ON turno.id_servicio = servicio.id_servicio WHERE fecha = %s", (fecha,))
    else:
        cursor.execute("SELECT fecha, hora, nombre_cliente, nombre FROM turno JOIN servicio ON turno.id_servicio = servicio.id_servicio")
    
    turnos = cursor.fetchall()
    
    for turno in turnos:
        tree.insert("", "end", values=turno)

# Función para filtrar turnos por la fecha seleccionada
def filtrar_por_fecha():
    fecha_seleccionada = cal.get_date()
    mostrar_turnos(fecha_seleccionada)

def registrar_turno():
    fecha = cal.get_date()
    hora = entry_hora.get()
    nombre_cliente = entry_cliente.get()
    servicio = combo_servicio.get()

    # Validar que la fecha no sea anterior a hoy
    fecha_actual = datetime.now().date()
    fecha_turno = datetime.strptime(fecha, "%Y-%m-%d").date()

    if fecha_turno < fecha_actual:
        messagebox.showerror("Error", "No se pueden registrar turnos en fechas anteriores a hoy.")
        return

    # Obtener el id del servicio seleccionado
    cursor.execute("SELECT id_servicio FROM servicio WHERE nombre = %s", (servicio,))
    id_servicio = cursor.fetchone()

    if id_servicio:
        cursor.execute(
            "INSERT INTO turno (fecha, hora, id_servicio, nombre_cliente) VALUES (%s, %s, %s, %s)",
            (fecha, hora, id_servicio[0], nombre_cliente)
        )
        db.commit()
        messagebox.showinfo("Éxito", "Turno registrado correctamente")
        mostrar_turnos()
    else:
        messagebox.showerror("Error", "Servicio no encontrado")

def cargar_turno_seleccionado(event):
    selected_item = tree.selection()
    if selected_item:
        item_values = tree.item(selected_item, 'values')
        entry_hora.delete(0, tk.END)
        entry_hora.insert(0, item_values[1])  # Hora
        entry_cliente.delete(0, tk.END)
        entry_cliente.insert(0, item_values[2])  # Nombre del Cliente
        combo_servicio.set(item_values[3])  # Servicio
        global turno_id
        # Obtener el id del turno seleccionado
        cursor.execute("SELECT id_turno FROM turno WHERE fecha = %s AND hora = %s AND nombre_cliente = %s", (item_values[0], item_values[1], item_values[2]))
        turno_id = cursor.fetchone()[0]  # Guardar el ID del turno seleccionado

def modificar_turno():
    if not turno_id:
        messagebox.showerror("Error", "No se ha seleccionado ningún turno para modificar.")
        return

    fecha = cal.get_date()
    hora = entry_hora.get()
    nombre_cliente = entry_cliente.get()
    servicio = combo_servicio.get()

    # Obtener el id del servicio seleccionado
    cursor.execute("SELECT id_servicio FROM servicio WHERE nombre = %s", (servicio,))
    id_servicio = cursor.fetchone()

    if id_servicio:
        cursor.execute(
            "UPDATE turno SET fecha = %s, hora = %s, id_servicio = %s, nombre_cliente = %s WHERE id_turno = %s",
            (fecha, hora, id_servicio[0], nombre_cliente, turno_id)
        )
        db.commit()
        messagebox.showinfo("Éxito", "Turno modificado correctamente")
        mostrar_turnos()
    else:
        messagebox.showerror("Error", "Servicio no encontrado")

def eliminar_turno():
    global turno_id
    if not turno_id:
        messagebox.showerror("Error", "No se ha seleccionado ningún turno para eliminar.")
        return

    # Confirmar la eliminación
    confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar este turno?")
    if confirm:
        cursor.execute("DELETE FROM turno WHERE id_turno = %s", (turno_id,))
        db.commit()
        messagebox.showinfo("Éxito", "Turno eliminado correctamente")
        mostrar_turnos()
        turno_id = None  # Reiniciar el ID del turno seleccionado

# Ventana principal
root = tk.Tk()
root.title("Gestor de Turnos")
root.geometry("1280x720")

# Sección izquierda : Ingreso de datos
frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, padx=10, pady=10)

label_fecha = tk.Label(frame_left, text="Fecha:")
label_fecha.pack()
cal = Calendar(frame_left, date_pattern='y-mm-dd')
cal.pack(pady=5)

# Mover el botón de filtrar debajo del calendario
button_filtrar = tk.Button(frame_left, text="Filtrar Turnos por Fecha", command=filtrar_por_fecha)
button_filtrar.pack(pady=10)

label_hora = tk.Label(frame_left, text="Hora (HH:MM):")
label_hora.pack()

entry_hora = tk.Entry(frame_left)
entry_hora.insert(0, "HH:MM")  # Establecer el valor inicial
entry_hora.pack(pady=5)

label_cliente = tk.Label(frame_left, text="Nombre del Cliente:")
label_cliente.pack()
entry_cliente = tk.Entry(frame_left)
entry_cliente.pack(pady=5)

label_servicio = tk.Label(frame_left, text="Servicio:")
label_servicio.pack()
combo_servicio = ttk.Combobox(frame_left)
combo_servicio.pack(pady=5)

# Obtener los servicios disponibles de la base de datos
cursor.execute("SELECT nombre FROM servicio")
servicios = cursor.fetchall()
combo_servicio['values'] = [servicio[0] for servicio in servicios]

button_registrar = tk.Button(frame_left, text="Registrar Turno", command=registrar_turno)
button_registrar.pack(pady=20)

# Botón para modificar el turno
button_modificar = tk.Button(frame_left, text="Modificar Turno", command=modificar_turno)
button_modificar.pack(pady=20)
#Boton Eliminar el turno
button_eliminar = tk.Button(frame_left, text="Eliminar Turno", command=eliminar_turno)
button_eliminar.pack(pady=20)

# Sección derecha: Grilla de turnos
frame_right = tk.Frame(root)
frame_right.pack(side=tk.RIGHT, padx=10, pady=10)

label_turnos = tk.Label(frame_right, text="Turnos Registrados", font=("Arial", 14))
label_turnos.pack(pady=5)

# Configuración de la grilla (Treeview)
columns = ("Fecha", "Hora", "Nombre Cliente", "Servicio")
tree = ttk.Treeview(frame_right, columns=columns, show='headings')
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Nombre Cliente", text="Nombre Cliente")
tree.heading("Servicio", text="Servicio")
tree.pack()

# Asignar evento de selección de fila
tree.bind("<<TreeviewSelect>>", cargar_turno_seleccionado)

# Mostrar todos los turnos al iniciar
mostrar_turnos()

# Variable global para almacenar el ID del turno seleccionado
turno_id = None

root.mainloop()
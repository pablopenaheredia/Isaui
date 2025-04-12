import tkinter as tk
from cuadratica_tkinter import iniciar_cuadratica
from matrices_tkinter import iniciar_matrices

def abrir_cuadratica():
    iniciar_cuadratica()

def abrir_matrices():
    iniciar_matrices()

root = tk.Tk()
root.title("Menú Principal")
root.resizable(False, False)
root.geometry("600x150")

bg_color = "#A7C6ED"  # Color de fondo azul claro
button_color = "#4B9CD3"  # Color de botones azul oscuro

root.configure(bg=bg_color)  # Aplicar el color de fondo a la ventana

# Label superior
label_instrucciones = tk.Label(root, text="Seleccione alguna de las dos operaciones que aparecen en pantalla", 
                                bg=bg_color, font=("Arial", 14), fg="#2C2C2C")  # Color de texto gris oscuro
label_instrucciones.pack(pady=(20, 0))  # Espaciado arriba

# Frame para los botones
frame_botones = tk.Frame(root, bg=bg_color)  # Mantener el mismo color de fondo
frame_botones.pack(pady=20)  # Espaciado vertical para el marco

# Botones dentro del frame
boton_cuadratica = tk.Button(frame_botones, text="Función Cuadrática", command=abrir_cuadratica, width=20,
                             bg=button_color, fg="white", font=("Arial", 12))  # Color de fondo diferente
boton_cuadratica.pack(side=tk.LEFT, padx=10) 
boton_matrices = tk.Button(frame_botones, text="Matrices", command=abrir_matrices, width=20,
                           bg=button_color, fg="white", font=("Arial", 12))  # Color de fondo diferente
boton_matrices.pack(side=tk.LEFT, padx=10)  
root.mainloop()

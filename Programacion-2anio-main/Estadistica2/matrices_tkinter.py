import tkinter as tk
from tkinter import messagebox
from matrices import gauss_jordan

def iniciar_matrices():
    def obtener_dimensiones():
        try:
            dimension = entry_n.get().split('x')
            n = int(dimension[0])  # Filas
            m = int(dimension[1])  # Columnas
            return n, m
        except ValueError:
            messagebox.showerror("Error", "Debes ingresar un número entero válido en el formato nxm.")
            return None, None

    def validar_dimensiones(n, m):
        if n <= 0 or n > 6 or m <= 0 or m > 6:
            messagebox.showerror("Error", "Las dimensiones de la matriz deben ser números enteros entre 1 y 6.")
            return False
        return True

    def crear_entradas():
        n, m = obtener_dimensiones()
        if n is None or m is None or not validar_dimensiones(n, m):
            return
        if n > m:
            messagebox.showerror("Error", "La matriz ingresada tiene más filas que columnas (n > m).\n"
                                        "El programa solo admite matrices cuadradas (n = m) o matrices "
                                        "con más columnas que filas (n < m).\n"
                                        "Por favor, ingresa una matriz válida.")
            return
        
        # Limpiar el marco de la matriz
        for widget in frame_matriz.winfo_children():
            widget.destroy()

        global entry_matriz
        global entry_resultados
        entry_matriz = []
        entry_resultados = []
        variables = ['x', 'y', 'z', 'w', 'v', 'u']  # Lista de variables para las etiquetas
        subindices = ['\u2081', '\u2082', '\u2083', '\u2084', '\u2085', '\u2086']  # Subíndices Unicode

        for i in range(n):
            fila = []
            for j in range(m):
                # Cambiar a aij con subíndice
                label = tk.Label(frame_matriz, text=f"{variables[j]}{subindices[i]}", bg="#A7C6ED")  
                label.grid(row=i, column=j*2, padx=5, pady=5)
                entry = tk.Entry(frame_matriz)
                entry.grid(row=i, column=j*2+1, padx=5, pady=5)
                fila.append(entry)
            entry_matriz.append(fila)
            label_resultado = tk.Label(frame_matriz, text=f"b{subindices[i]}", bg="#A7C6ED")
            label_resultado.grid(row=i, column=m*2, padx=5, pady=5)
            entry_resultado_i = tk.Entry(frame_matriz)
            entry_resultado_i.grid(row=i, column=m*2+1, padx=5, pady=5)
            entry_resultados.append(entry_resultado_i)

    def obtener_matriz_y_resultados():
        n, m = obtener_dimensiones()
        if n is None or m is None or not validar_dimensiones(n, m):
            return

        try:
            matriz = []
            resultados = []
            for i in range(n):
                fila = []
                for j in range(m):
                    fila.append(float(entry_matriz[i][j].get()))
                matriz.append(fila)
                resultados.append(float(entry_resultados[i].get()))

            soluciones = gauss_jordan(matriz, resultados)
            if soluciones is not None:
                variables = ['x', 'y', 'z', 'w', 'v', 'u']
                mensaje = "Sistema Compatible Determinado\n"
                for i in range(n):
                    mensaje += f"{variables[i]} = {round(soluciones[i], 4)}\n"
                messagebox.showinfo("Resultados", mensaje)
        except ValueError:
            messagebox.showerror("Error", "Debes ingresar números válidos.")

    root = tk.Tk()
    root.title("Método de Gauss-Jordan")
    root.configure(bg="#A7C6ED")
    root.resizable(False, False)

    label_n = tk.Label(root, text="Tamaño de la matriz (nxm):", bg="#A7C6ED", fg="black")
    label_n.grid(row=0, column=0, padx=10, pady=10)

    entry_n = tk.Entry(root, width=5)
    entry_n.grid(row=0, column=1, padx=10, pady=10)

    boton_crear_entradas = tk.Button(root, text="Crear entradas", command=crear_entradas, bg="#A7C6ED", fg="black")
    boton_crear_entradas.grid(row=0, column=2, padx=10, pady=10)

    frame_matriz = tk.Frame(root, bg="#A7C6ED")
    frame_matriz.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    boton_calcular = tk.Button(root, text="Calcular", command=obtener_matriz_y_resultados, bg="#A7C6ED", fg="black")
    boton_calcular.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    # Hacer la GUI responsiva
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)

    root.mainloop()

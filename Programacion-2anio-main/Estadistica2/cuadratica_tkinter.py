import tkinter as tk
from tkinter import messagebox
from cuadratica import calcular_area_cuadratica, graficar_funcion

def iniciar_cuadratica():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Cálculo de área de una función cuadrática")
    root.configure(bg="#A7C6ED")
    root.resizable(False, False)

    # Área de texto para mostrar resultados
    texto_resultado = tk.Text(root, width=30, height=15)
    texto_resultado.grid(row=0, rowspan=6, column=2, padx=10, pady=10)

    def obtener_texto_resultado():
        return texto_resultado.get("1.0", tk.END)

    def actualizar_texto_resultado(suma_inferior, suma_superior, area_real, error, a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos):
        texto_resultado.delete(1.0, tk.END)
        texto_resultado.insert(tk.END, f"Suma inferior: {suma_inferior:.2f}\n")
        texto_resultado.insert(tk.END, f"Suma superior: {suma_superior:.2f}\n")
        texto_resultado.insert(tk.END, f"Área real: {area_real:.2f}\n")
        texto_resultado.insert(tk.END, f"Error de cálculo: {error:.2f}%\n")

        # Obtener el contenido del texto_resultado
        contenido_texto = obtener_texto_resultado()

        # Llamar a la función de graficación pasando el contenido del texto
        graficar_funcion(a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos, contenido_texto)

    def obtener_parametros():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())
            intervalo_inicio = float(entry_intervalo_inicio.get())
            intervalo_fin = float(entry_intervalo_fin.get())
            num_rectangulos = int(entry_num_rectangulos.get())

            suma_inferior, suma_superior, area_real, error = calcular_area_cuadratica(a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos)
            actualizar_texto_resultado(suma_inferior, suma_superior, area_real, error, a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos)
        except ValueError as e:
            texto_resultado.delete(1.0, tk.END)
            texto_resultado.insert(tk.END, f"Error: {str(e)}. Por favor, ingrese valores válidos.")

    # Definición de otros widgets
    label_a = tk.Label(root, text="Coeficiente cuadrático:", bg="#A7C6ED", fg="black")
    label_a.grid(row=0, column=0, padx=10, pady=10)
    entry_a = tk.Entry(root)
    entry_a.grid(row=0, column=1, padx=10, pady=10)

    label_b = tk.Label(root, text="Coeficiente lineal:", bg="#A7C6ED", fg="black")
    label_b.grid(row=1, column=0, padx=10, pady=10)
    entry_b = tk.Entry(root)
    entry_b.grid(row=1, column=1, padx=10, pady=10)

    label_c = tk.Label(root, text="Coeficiente independiente:", bg="#A7C6ED", fg="black")
    label_c.grid(row=2, column=0, padx=10, pady=10)
    entry_c = tk.Entry(root)
    entry_c.grid(row=2, column=1, padx=10, pady=10)  # Aquí se agregó el método grid()

    label_intervalo_inicio = tk.Label(root, text="Inicio del intervalo:", bg="#A7C6ED", fg="black")
    label_intervalo_inicio.grid(row=3, column=0, padx=10, pady=10)
    entry_intervalo_inicio = tk.Entry(root)
    entry_intervalo_inicio.grid(row=3, column=1, padx=10, pady=10)

    label_intervalo_fin = tk.Label(root, text="Fin del intervalo:", bg="#A7C6ED", fg="black")
    label_intervalo_fin.grid(row=4, column=0, padx=10, pady=10)
    entry_intervalo_fin = tk.Entry(root)
    entry_intervalo_fin.grid(row=4, column=1, padx=10, pady=10)

    label_num_rectangulos = tk.Label(root, text="Cantidad de rectángulos:", bg="#A7C6ED", fg="black")
    label_num_rectangulos.grid(row=5, column=0, padx=10, pady=10)
    entry_num_rectangulos = tk.Entry(root)
    entry_num_rectangulos.grid(row=5, column=1, padx=10, pady=10)

    # Botón para calcular y graficar
    boton_calcular = tk.Button(root, text="Calcular área", command=obtener_parametros, bg="#A7C6ED", fg="black")
    boton_calcular.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from estadisticos import *


def mostrar_resultados(resultados):
    # Crear una nueva ventana para mostrar los resultados
    ventana_resultados = tk.Toplevel()
    ventana_resultados.title("Resultados")
    ventana_resultados.grab_set()

    # Crear una tabla utilizando Treeview
    tree = ttk.Treeview(ventana_resultados, columns=("Operacion", "Resultado"), show="headings")
    tree.heading("Operacion", text="Operación")
    tree.heading("Resultado", text="Resultado")
    tree.pack(expand=True, fill="both")

    # Insertar los resultados en la tabla
    for operacion, resultado in resultados:
        tree.insert("", "end", values=(operacion, resultado))

    # Botón para cerrar la ventana de resultados
    btn_cerrar = ttk.Button(ventana_resultados, text="Cerrar", command=ventana_resultados.destroy)
    btn_cerrar.pack()

    ventana_resultados.wait_window()

def menu_estadistico(numeros):
    opciones = simpledialog.askstring("Opciones Estadísticas", 
                                      "Ingrese las opciones deseadas (separadas por comas):\n"
                                      "1. MEDIA\n"
                                      "2. MODA\n"
                                      "3. MEDIANA\n"
                                      "4. DESVIACIÓN ESTÁNDAR\n"
                                      "5. VARIANZA\n"
                                      "6. FRECUENCIA ABSOLUTA\n"
                                      "7. FRECUENCIA RELATIVA\n"
                                      "8. FRECUENCIA PORCENTUAL\n"
                                      "9. FRECUENCIA ABSOLUTA ACUMULADA\n"
                                      "10. FRECUENCIA RELATIVA ACUMULADA\n"
                                      "11. FRECUENCIA PORCENTUAL ACUMULADA\n"
                                      "12. COEFICIENTE DE CURTOSIS\n"
                                      "13. TODOS\n"
                                      "0. Regresar")
    if opciones is None:
        return

    opciones = [opcion.strip() for opcion in opciones.split(',')]
    resultados = []

    for opcion in opciones:
        if opcion == '1':
            resultados.append(["MEDIA", calcular_media(numeros)])
        elif opcion == '2':
            moda, frecuencia = calcular_moda(numeros)
            if moda is None:
                resultados.append(["MODA", "No hay moda en los datos."])
            else:
                resultados.append(["MODA", f"{moda} (Frecuencia: {frecuencia})"])
        elif opcion == '3':
            resultados.append(["MEDIANA", calcular_mediana(numeros)])
        elif opcion == '4':
            resultados.append(["DESVIACIÓN ESTÁNDAR", calcular_desviacion(numeros)])
        elif opcion == '5':
            resultados.append(["VARIANZA", calcular_varianza(numeros)])
        elif opcion == '6':
            resultados.append(["FRECUENCIA ABSOLUTA", frecuencia_absoluta(numeros)])
        elif opcion == '7':
            resultados.append(["FRECUENCIA RELATIVA", frecuencia_relativa(numeros)])
        elif opcion == '8':
            resultados.append(["FRECUENCIA PORCENTUAL", frecuencia_porcentual(numeros)])
        elif opcion == '9':
            resultados.append(["FRECUENCIA ABSOLUTA ACUMULADA", frecuencia_absoluta_acumulada(numeros)])
        elif opcion == '10':
            resultados.append(["FRECUENCIA RELATIVA ACUMULADA", frecuencia_relativa_acumulada(numeros)])
        elif opcion == '11':
            resultados.append(["FRECUENCIA PORCENTUAL ACUMULADA", frecuencia_porcentual_acumulada(numeros)])
        elif opcion == '12':
            resultados.append(["COEFICIENTE DE CURTOSIS", coeficiente_curtosis(numeros)])
        elif opcion == '13':
            resultados.extend([
                ["MEDIA", calcular_media(numeros)],
                ["MODA", calcular_moda(numeros)],
                ["MEDIANA", calcular_mediana(numeros)],
                ["DESVIACIÓN ESTÁNDAR", calcular_desviacion(numeros)],
                ["VARIANZA", calcular_varianza(numeros)],
                ["FRECUENCIA ABSOLUTA", frecuencia_absoluta(numeros)],
                                ["FRECUENCIA RELATIVA", frecuencia_relativa(numeros)],
                ["FRECUENCIA PORCENTUAL", frecuencia_porcentual(numeros)],
                ["FRECUENCIA ABSOLUTA ACUMULADA", frecuencia_absoluta_acumulada(numeros)],
                ["FRECUENCIA RELATIVA ACUMULADA", frecuencia_relativa_acumulada(numeros)],
                ["FRECUENCIA PORCENTUAL ACUMULADA", frecuencia_porcentual_acumulada(numeros)],
                ["COEFICIENTE DE CURTOSIS", coeficiente_curtosis(numeros)]
            ])
        else:
            messagebox.showerror("Error", f"Opción {opcion} no válida.")
    
    if resultados:
        mostrar_resultados(resultados)

def menu_distribuciones():
    while True:
        opcion = simpledialog.askstring("Distribuciones",
                                        "Seleccione una opción:\n"
                                        "1. Distribución Binomial\n"
                                        "2. Distribución de Poisson\n"
                                        "3. Distribución Hipergeométrica\n"
                                        "4. Distribución Normal\n"
                                        "5. Distribución de Zipf\n"
                                        "6. Distribución Uniforme Continua\n"
                                        "7. Distribución de Weibull\n"
                                        "8. Distribución de Pareto\n"
                                        "0. Regresar")
        if opcion is None:
            return

        try:
            opcion = int(opcion)
            if opcion == 0:
                return
            elif opcion == 1:
                n = simpledialog.askinteger("Binomial", "Ingrese el número de ensayos (n):")
                p = simpledialog.askfloat("Binomial", "Ingrese la probabilidad de éxito (p):")
                k = simpledialog.askstring("Binomial", "Ingrese el número de éxitos deseados (k):")
                k_values = parse_k_values(k)
                resultados = []
                for k_val in k_values:
                    probabilidad = distribucion_binomial(n, p, k_val)
                    resultados.append([f"Binomial P(X={k_val})", probabilidad])
                mostrar_resultados(resultados)
            elif opcion == 2:
                lambd = simpledialog.askfloat("Poisson", "Ingrese el valor de lambda (λ):")
                k = simpledialog.askstring("Poisson", "Ingrese el número de ocurrencias deseadas (k):")
                k_values = parse_k_values(k)
                resultados = []
                for k_val in k_values:
                    probabilidad = distribucion_poisson(lambd, k_val)
                    resultados.append([f"Poisson P(X={k_val})", probabilidad])
                mostrar_resultados(resultados)
            elif opcion == 3:
                N = simpledialog.askinteger("Hipergeométrica", "Ingrese el tamaño de la población (N):")
                M = simpledialog.askinteger("Hipergeométrica", "Ingrese el número de éxitos en la población (M):")
                n = simpledialog.askinteger("Hipergeométrica", "Ingrese el tamaño de la muestra (n):")
                k = simpledialog.askstring("Hipergeométrica", "Ingrese el número de éxitos deseados (k):")
                k_values = parse_k_values(k)
                resultados = []
                for k_val in k_values:
                    probabilidad = distribucion_hipergeometrica(n, M, N, k_val)
                    resultados.append([f"Hipergeométrica P(X={k_val})", probabilidad])
                mostrar_resultados(resultados)
            elif opcion == 4:
                mu = simpledialog.askfloat("Normal", "Ingrese la media (μ):")
                sigma = simpledialog.askfloat("Normal", "Ingrese la desviación estándar (σ):")
                x = simpledialog.askstring("Normal", "Ingrese el valor o rango de x (separado por comas):")
                x_values = parse_x_values(x)
                resultados = []
                for x_val in x_values:
                    densidad = distribucion_normal(x_val, mu, sigma)
                    resultados.append([f"Normal f(X={x_val})", densidad])
                mostrar_resultados(resultados)
            
            elif opcion == 5:
                N = simpledialog.askinteger("Zipf", "Ingrese el número total de elementos (N):")
                s = simpledialog.askfloat("Zipf", "Ingrese el parámetro s:")
                k = simpledialog.askstring("Zipf", "Ingrese la(s) posición(es) k (ej: 1,2,5) o un rango (ej: 2-7):")
                
                # Lista para almacenar todas las posiciones k
                k_list = []
            
                # Procesar entrada del usuario
                valores = k.split(',')
                for valor in valores:
                    if '-' in valor:
                        # Procesar rango
                        inicio, fin = map(int, valor.split('-'))
                        k_list.extend(range(inicio, fin + 1))
                    else:
                        # Procesar número individual
                        k_list.append(int(valor))
            
                resultados = []
                
                # Calcular probabilidades individuales usando la función de estadisticos.py
                for k_val in k_list:
                    if 1 <= k_val <= N:
                        prob = distribucion_zipf(k_val, s, N)
                        resultados.append([f"Zipf P(k={k_val})", prob])
            
                # Si hay más de un valor k, calcular la probabilidad acumulada
                if len(k_list) > 1:
                    prob_acumulada = probabilidad_acumulada_zipf(k_list, s, N)
                    resultados.append(["Probabilidad acumulada", prob_acumulada])
                
                mostrar_resultados(resultados)

            elif opcion == 6:  # Opción para la Distribución Uniforme Continua
                 

                 a = simpledialog.askfloat("Uniforme Continua", "Ingrese el valor de a (inicio del intervalo):")
                 b = simpledialog.askfloat("Uniforme Continua", "Ingrese el valor de b (fin del intervalo):")
    
                 if a is None or b is None:
                   messagebox.showwarning("Advertencia", "Valores a y b son necesarios.")
                   continue
    
                 if a >= b:
                  messagebox.showerror("Error", "El valor de 'a' debe ser menor que el valor de 'b'.")
                  continue
    
    # Pide el valor de x1 para calcular la probabilidad
                 x1 = simpledialog.askfloat("Uniforme Continua", "Ingrese el valor de x1:")
                 if x1 is None:
                  messagebox.showwarning("Advertencia", "El valor de x1 es necesario.")
                  continue

                 if x1 < a or x1 > b:
                    messagebox.showerror("Error", f"x1 debe estar entre {a} y {b}.")
                    continue
    
     # Llamada a la función distribucion_uniforme para obtener los resultados
                 probabilidad, valor_esperado, varianza, desviacion_estandar = distribucion_uniforme(a, b, x1)

                 resultado = f"Valor esperado (E): {valor_esperado:.2f}\nVarianza (V): {varianza:.2f}\nDesviación estándar (D): {desviacion_estandar:.2f}\n"
    
                 # Mostrar probabilidad de x1
                 resultado += f"P(a <= X <= {x1}): {probabilidad:.2f}"
                 x2 = None
                 # Preguntar si quiere calcular para un intervalo
                 calcular_x2 = messagebox.askyesno("Uniforme Continua", "¿Desea calcular la probabilidad entre dos valores (x1 y x2)?")
                 if calcular_x2:
                   x2 = simpledialog.askfloat("Uniforme Continua", "Ingrese el valor de x2:")
                   if x2 is None or x2 < a or x2 > b or x1 >= x2:
                    messagebox.showerror("Error", f"x2 debe estar entre {a} y {b}, y debe ser mayor que x1.")
                    continue
        # Calcular probabilidad entre x1 y x2
                   prob_intervalo = distribucion_uniforme(a, b, x1, x2)[0]
                   resultado += f"\nP({x1} <= X <= {x2}): {prob_intervalo:.2f}"
     # Mostrar todos los resultados en un cuadro de mensaje
                 messagebox.showinfo("Resultados", resultado)
                
            elif opcion == 7:  # Opción para la distribución de Weibull
                k = simpledialog.askfloat("Weibull", "Ingrese el parámetro de forma (k):")
                λ = simpledialog.askfloat("Weibull", "Ingrese el parámetro de escala (λ):")
                if k is None or λ is None:
                    messagebox.showwarning("Advertencia", "Ambos parámetros son necesarios.")
                    continue
                plot_weibull(k, λ)  # Llama a la función que grafica
            
            elif opcion == 8:  # Nueva opción para la Distribución de Pareto
                x_m = simpledialog.askfloat("Pareto", "Ingrese el valor mínimo (x_m):")
                alpha = simpledialog.askfloat("Pareto", "Ingrese el parámetro de forma (alpha):")
                num_samples = simpledialog.askinteger("Pareto", "Ingrese el número de muestras a generar:")
                muestras = distribucion_pareto(x_m, alpha, num_samples)
                resultados = [[f"Muestra {i+1}", muestra] for i, muestra in enumerate(muestras)]
                mostrar_resultados(resultados)
        
            else:
                messagebox.showerror("Error", "Opción no válida.")
        except ValueError as e:
            messagebox.showerror("Error", f"Entrada no válida: {e}")
           

def parse_k_values(k):
    if '-' in k:
        start, end = map(int, k.split('-'))
        return range(start, end + 1)
    return [int(k)]

def parse_x_values(x):
    if '-' in x:
        start, end = map(float, x.split('-'))
        return [i for i in range(int(start), int(end) + 1)]
    return [float(val.strip()) for val in x.split(',')]

def ingresar_datos():
    numeros_str = simpledialog.askstring("Datos", "Ingrese los números separados por comas:")
    if numeros_str is None:
            return None

    try:
        numeros = [float(num.strip()) for num in numeros_str.split(',')]
        return numeros
    except ValueError:
        messagebox.showerror("Error", "Entrada no válida. Asegúrese de ingresar números separados por comas.")
        return None

def main():
    global root
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    while True:
        opcion_principal = simpledialog.askstring("Menú Principal",
                                                  "Seleccione una opción:\n"
                                                  "A. Cálculos Estadísticos\n"
                                                  "B. Distribuciones de Probabilidad\n"
                                                  "0. Salir")
        if opcion_principal is None or opcion_principal == "0":
            break
        elif opcion_principal.upper() == "A":
            numeros = ingresar_datos()
            if numeros:
                menu_estadistico(numeros)
        elif opcion_principal.upper() == "B":
            menu_distribuciones()
        else:
            messagebox.showerror("Error", "Opción no válida. Intente nuevamente.")

    root.quit()

if __name__ == "__main__":
    main()
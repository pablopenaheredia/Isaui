from tkinter import messagebox

def gauss_jordan(matriz, resultados, umbral=1e-10):
    n = len(matriz)  # Número de filas
    m = len(matriz[0])  # Número de columnas (coeficientes)

    for i in range(n):
        # Buscar fila pivote
        max_valor = abs(matriz[i][i])
        fila_pivote = i
        for k in range(i + 1, n):
            if abs(matriz[k][i]) > max_valor:
                max_valor = abs(matriz[k][i])
                fila_pivote = k

        # Intercambiar filas si es necesario
        if fila_pivote != i:
            matriz[i], matriz[fila_pivote] = matriz[fila_pivote], matriz[i]
            resultados[i], resultados[fila_pivote] = resultados[fila_pivote], resultados[i]

        # Verificar si el pivote es muy cercano a cero
        if abs(matriz[i][i]) < umbral:
            # Si el resultado correspondiente también es cercano a cero, el sistema es indeterminado
            if abs(resultados[i]) < umbral:
                messagebox.showinfo("Resultado", "El sistema es compatible indeterminado y tiene infinitas soluciones.")
                return
            else:
                # Si no, es inconsistente
                messagebox.showerror("Error", "El sistema es incompatible y no tiene solución.")
                return

        # Normalizar la fila pivote
        pivote = matriz[i][i]
        for j in range(i, m):
            matriz[i][j] /= pivote
        resultados[i] /= pivote

        # Hacer cero los elementos debajo del pivote
        for k in range(i + 1, n):
            factor = matriz[k][i]
            for j in range(i, m):
                matriz[k][j] -= factor * matriz[i][j]
            resultados[k] -= factor * resultados[i]

    # Revisar si alguna fila es completamente cero
    for i in range(n):
        fila_nula = all(abs(matriz[i][j]) < umbral for j in range(m))
        if fila_nula and abs(resultados[i]) < umbral:
            messagebox.showinfo("Resultado", "El sistema es compatible indeterminado y tiene infinitas soluciones.")
            return

    # Calcular soluciones hacia atrás
    soluciones = [0] * n
    for i in range(n - 1, -1, -1):
        soluciones[i] = resultados[i]
        for j in range(i + 1, n):
            soluciones[i] -= matriz[i][j] * soluciones[j]

    # Para sistemas indeterminados, se puede indicar que hay variables libres
    # Esto es solo un ejemplo, y puede necesitar ajustes según el caso
    if n < m:  # Si hay más variables que ecuaciones
        messagebox.showinfo("Resultado", "El sistema es compatible indeterminado y tiene infinitas soluciones.")
        return
    
    return soluciones
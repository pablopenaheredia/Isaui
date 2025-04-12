import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def calcular_area_cuadratica(a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos):
    def funcion_cuadratica(x):
        return a * x**2 + b * x + c

    area_real, _ = quad(lambda x: abs(funcion_cuadratica(x)), intervalo_inicio, intervalo_fin)

    x_values = np.linspace(intervalo_inicio, intervalo_fin, num_rectangulos + 1)
    y_values = [abs(funcion_cuadratica(x)) for x in x_values]
    
    suma_inferior = 0
    suma_superior = 0

    for i in range(num_rectangulos):
        ancho = x_values[i+1] - x_values[i]
        suma_inferior += ancho * min(y_values[i], y_values[i+1])
        suma_superior += ancho * max(y_values[i], y_values[i+1])

    error = abs(area_real - (suma_inferior + suma_superior) / 2)

    return suma_inferior, suma_superior, area_real, error

def graficar_funcion(a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos, texto_resultado):
    x_plot = np.linspace(intervalo_inicio, intervalo_fin, 1000)
    y_plot = [a * x**2 + b * x + c for x in x_plot]

    plt.plot(x_plot, y_plot, label='Función cuadrática', color='blue')
    plt.fill_between(x_plot, y_plot, color='blue', alpha=0.1)

    ancho = (intervalo_fin - intervalo_inicio) / num_rectangulos
    for i in range(num_rectangulos):
        xi = intervalo_inicio + i * ancho
        xf = intervalo_inicio + (i + 1) * ancho
        altura_inferior = min(a * xi**2 + b * xi + c, a * xf**2 + b * xf + c)
        altura_superior = max(a * xi**2 + b * xi + c, a * xf**2 + b * xf + c)
        plt.bar(xi, altura_inferior, width=ancho, color='green', alpha=0.5, edgecolor='black', align='edge')
        plt.bar(xi, altura_superior, width=ancho, color='pink', alpha=0.3, edgecolor='black', align='edge')

    plt.text(0.5, 0.5, texto_resultado, fontsize=12, ha='center', transform=plt.gca().transAxes)

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico de la función cuadrática con sumas inferior y superior')
    plt.legend()
    plt.grid(True)
    plt.show()
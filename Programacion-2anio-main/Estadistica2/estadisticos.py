import statistics
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import quad
import random

# Funciones estadísticas
def calcular_media(lista):
    return round(statistics.mean(lista), 4)

def calcular_moda(lista):
    frecuencias = {}
    for num in lista:
        frecuencias[num] = frecuencias.get(num, 0) + 1
    moda_frecuencia_maxima = max(frecuencias.values())
    moda = [num for num, freq in frecuencias.items() if freq == moda_frecuencia_maxima]
    if len(set(frecuencias.values())) == 1:
        return None, None
    else:
        return moda, moda_frecuencia_maxima

def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    return round(statistics.median(lista_ordenada), 4)

def calcular_desviacion(lista):
    desviacion_estandar = statistics.stdev(lista)
    return round(desviacion_estandar, 4)

def calcular_varianza(lista):
    varianza = statistics.variance(lista)
    return round(varianza, 4)

def frecuencia_absoluta(lista):
    frecuencias = {}
    for num in lista:
        frecuencias[num] = frecuencias.get(num, 0) + 1
    return frecuencias

def frecuencia_relativa(lista):
    total = len(lista)
    frec_abs = frecuencia_absoluta(lista)
    frec_relativa = {}
    for clave, valor in frec_abs.items():
        frec_relativa[clave] = round(valor / total, 4)
    return frec_relativa

def frecuencia_porcentual(lista):
    frec_rel = frecuencia_relativa(lista)
    frec_porcentual = {}
    for clave, valor in frec_rel.items():
        frec_porcentual[clave] = round(valor * 100, 4)
    return frec_porcentual

def frecuencia_absoluta_acumulada(lista):
    frec_abs = frecuencia_absoluta(lista)
    acumulado = 0
    frec_abs_acum = {}
    for clave, valor in sorted(frec_abs.items()):
        acumulado += valor
        frec_abs_acum[clave] = acumulado
    return frec_abs_acum

def frecuencia_relativa_acumulada(lista):
    total = len(lista)
    frec_rel = frecuencia_relativa(lista)
    acumulado = 0
    frec_rel_acum = {}
    for clave, valor in sorted(frec_rel.items()):
        acumulado += valor
        frec_rel_acum[clave] = round(acumulado, 4)
    return frec_rel_acum

def frecuencia_porcentual_acumulada(lista):
    frec_porcent = frecuencia_porcentual(lista)
    acumulado = 0
    frec_porcent_acum = {}
    for clave, valor in sorted(frec_porcent.items()):
        acumulado += valor
        frec_porcent_acum[clave] = f"{round(acumulado, 4)}%"
    return frec_porcent_acum

def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        result = 1
        for i in range(2, x+1):
            result *= i
        return result

def combinacion(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def distribucion_binomial(n, p, k):
    combinaciones = combinacion(n, k)
    probabilidad = combinaciones * (p ** k) * ((1 - p) ** (n - k))
    return probabilidad

def distribucion_poisson(lambd, k):
    probabilidad = (lambd ** k) * (math.e ** -lambd) / factorial(k)
    return probabilidad

def distribucion_hipergeometrica(n, M, N, k):
    probabilidad = (combinacion(M, k) * combinacion(N - M, n - k)) / combinacion(N, n)
    return probabilidad

def distribucion_normal(x, mu, sigma):
    coeficiente = 1 / (2 * math.pi * (sigma ** 2)) ** 0.5
    exponente = -((x - mu) ** 2) / (2 * sigma ** 2)
    densidad = coeficiente * math.exp(exponente)
    return densidad

def distribucion_zipf(k, s, N):
    """
    Calcula la probabilidad de Zipf para una posición k
    Parámetros:
    k: posición (rango del elemento)
    s: parámetro de la distribución
    N: número total de elementos
    """
    # Verificar que k esté en el rango permitido
    if k < 1 or k > N:
        return 0

    denominador = sum(1 / (n ** s) for n in range(1, N + 1))
    probabilidad = (1 / (k ** s)) / denominador
    return round(probabilidad, 4)

def probabilidad_acumulada_zipf(rango, s, N):
    # Calcular la probabilidad acumulada de Zipf para un rango
    return sum(distribucion_zipf(k, s, N) for k in rango)


# alternativa usando scipy.stats.zipf
"""
def ejemplo_zipf_scipy():
    # Usando scipy.stats.zipf para calcular distribución Zipf
    print("\nResultados con scipy.stats.zipf:")  
    print("-" * 40)
    
    s = 1.3  # Parámetro de la distribución
    zipf_dist = zipf(a=s + 1)  # En scipy, a = s + 1 para conversión de parámetros
    k_valores = [1, 2, 5]  # Posiciones a evaluar
    
    # Normalizar probabilidades
    total = sum(zipf_dist.pmf(k) for k in range(1, 31))
    
    # pmf es función de masa de probabilidad
    # calcula P(X = k) para valores discretos
    # usa la formula: P(X = k) = 1/(ζ(a) * k^a)
    # ζ(a) es la función zeta de riemann
    # k es el rango o posición
    # y luego se normaliza dividiendo por el total
    
    for k in k_valores:
        prob = zipf_dist.pmf(k) / total
        print(f"Probabilidad para k={k}: {prob:.4f}")

if __name__ == "__main__":
    ejemplo_zipf_scipy()
"""
def distribucion_uniforme(a, b, x1, x2=None):

    if x2 is None:
       probabilidad=  (x1 - a) / (b - a)
    else:
       probabilidad= (x2 - x1) / (b - a)
   
    valor_esperado=(a + b) / 2
    varianza=((b - a) ** 2) / 12
    desviacion_estandar=varianza ** 0.5
    return probabilidad, valor_esperado, varianza, desviacion_estandar


def calcular_integral(mu, sigma, primer_parametro, segundo_parametro):
    if primer_parametro > segundo_parametro:
        raise ValueError("El primer parámetro de integración debe ser menor o igual que el segundo")
    integral, error = quad(distribucion_normal, primer_parametro, segundo_parametro, args=(mu, sigma))
    return integral

def coeficiente_curtosis(lista):    
    n = len(lista)  
    media = calcular_media(lista)
    desviacion = calcular_desviacion(lista)
    
    suma_cuarta_potencia = sum((x - media) ** 4 for x in lista)

    curtosis = (n * (n + 1) * suma_cuarta_potencia) / ((n - 1) * (n - 2) * (n - 3) * (desviacion ** 4)) \
               - (3 * (n - 1) ** 2) / ((n - 2) * (n - 3))
    
    if curtosis == 0:
        interpretación = "La distribución es mesocúrtica"
    elif curtosis > 0:
        interpretación = "La distribución es leptocúrtica"
    else:
        interpretación = "La distribución es platicúrtica"
        
    return round(curtosis, 4), interpretación

def weibull_pdf(x, k, λ):
    if x < 0:
        return 0
    return (k / λ) * (x / λ) ** (k - 1) * math.exp(- (x / λ) ** k)

def weibull_cdf(x, k, λ):
    if x < 0:
        return 0
    return 1 - math.exp(- (x / λ) ** k)

def plot_weibull(k, λ):
    x = np.linspace(0, λ * 3, 1000)  # Valores de x
    pdf_values = [weibull_pdf(val, k, λ) for val in x]  # Calcular PDF
    cdf_values = [weibull_cdf(val, k, λ) for val in x]  # Calcular CDF

    # Crear el gráfico
    plt.figure(figsize=(12, 6))
    
    # Gráfico de la PDF
    plt.subplot(1, 2, 1)
    plt.plot(x, pdf_values, 'b-', label='PDF', color='blue')
    plt.title('Distribución de Weibull - PDF')
    plt.xlabel('x')
    plt.ylabel('Densidad de probabilidad')
    plt.grid()
    plt.legend()
    
    # Gráfico de la CDF
    plt.subplot(1, 2, 2)
    plt.plot(x, cdf_values, 'r-', label='CDF', color='red')
    plt.title('Distribución de Weibull - CDF')
    plt.xlabel('x')
    plt.ylabel('Probabilidad acumulada')
    plt.grid()
    plt.legend()
    
    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()


def distribucion_pareto(x_m, alpha, num_samples):
    muestras = []
    for _ in range(num_samples):
        u = random.random()
        x = x_m * (1 - u) ** (-1 / alpha)
        muestras.append(round(x, 4))
    return muestras
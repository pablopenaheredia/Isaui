def distribucion_zipf(k, s, N):
    """
    Calcula la probabilidad de Zipf para una posición k
    """
    if k < 1 or k > N:
        return 0

    denominador = sum(1 / (n ** s) for n in range(1, N + 1))
    probabilidad = (1 / (k ** s)) / denominador
    return round(probabilidad, 4)

def probabilidad_acumulada_zipf(k1, k2, s, N):
    """
    Calcula la probabilidad acumulada de Zipf para un rango
    """
    if k1 > k2 or k1 < 1 or k2 > N:
        return 0
    
    prob_acumulada = sum(distribucion_zipf(k, s, N) for k in range(k1, k2 + 1))
    return round(prob_acumulada, 4)

def encontrar_k_umbral(umbral, s, N):
    """
    Encuentra posición k donde probabilidad < umbral
    """
    for k in range(1, N + 1):
        if distribucion_zipf(k, s, N) < umbral:
            return k - 1
    return N

def analizar_frecuencias(lista, s, top_n=10):
    """
    Compara frecuencias observadas vs esperadas según Zipf
    """
    frecuencias = {}
    for elemento in lista:
        frecuencias[elemento] = frecuencias.get(elemento, 0) + 1
    
    ordenados = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)
    N = len(ordenados)
    
    resultados = []
    for k in range(1, min(top_n + 1, N + 1)):
        if k-1 < len(ordenados):
            elemento, frec_obs = ordenados[k-1]
            frec_esp = distribucion_zipf(k, s, N) * len(lista)
            resultados.append({
                'posicion': k,
                'elemento': elemento,
                'frec_observada': frec_obs,
                'frec_esperada': round(frec_esp, 2)
            })
    return resultados

def ajustar_parametro_s(lista, rango_s=(0.5, 3.0), paso=0.1):
    """
    Encuentra mejor valor de s que ajusta datos a Zipf
    """
    frecuencias = {}
    for elemento in lista:
        frecuencias[elemento] = frecuencias.get(elemento, 0) + 1
    
    ordenados = sorted(frecuencias.values(), reverse=True)
    N = len(ordenados)
    
    mejor_s = rango_s[0]
    menor_error = float('inf')
    
    for s in range(int(rango_s[0]/paso), int(rango_s[1]/paso)):
        s = s * paso
        error = 0
        for k in range(1, N + 1):
            if k-1 < len(ordenados):
                frec_obs = ordenados[k-1] / len(lista)
                frec_esp = distribucion_zipf(k, s, N)
                error += (frec_obs - frec_esp) ** 2
        
        if error < menor_error:
            menor_error = error
            mejor_s = s
            
    return round(mejor_s, 2)

def test_todas_funciones():
    """
    Prueba todas las funciones de distribución Zipf
    """
    print("PRUEBAS DE FUNCIONES ZIPF")
    print("=" * 50)

    # 1. Probabilidad Acumulada
    print("\n1. Probabilidad Acumulada")
    print("-" * 30)
    N = 30
    s = 1.3
    k1, k2 = 1, 5
    prob_acum = probabilidad_acumulada_zipf(k1, k2, s, N)
    print(f"Probabilidad acumulada para posiciones {k1} a {k2}: {prob_acum}")

    # 2. Encontrar K Umbral
    print("\n2. Encontrar K Umbral")
    print("-" * 30)
    umbral = 0.1
    k = encontrar_k_umbral(umbral, s, N)
    print(f"Primera posición k con probabilidad < {umbral}: {k}")

    # 3. Analizar Frecuencias
    print("\n3. Análisis de Frecuencias")
    print("-" * 30)
    texto = ["a", "a", "a", "b", "b", "c", "d", "a", "b", "e"]
    analisis = analizar_frecuencias(texto, s=1.3, top_n=5)
    print("Análisis de frecuencias top 5:")
    for resultado in analisis:
        print(f"Posición {resultado['posicion']}: {resultado['elemento']}")
        print(f"  Frecuencia observada: {resultado['frec_observada']}")
        print(f"  Frecuencia esperada: {resultado['frec_esperada']}")

    # 4. Ajustar Parámetro S
    print("\n4. Ajuste de Parámetro S")
    print("-" * 30)
    s_optimo = ajustar_parametro_s(texto)
    print(f"Valor óptimo de s: {s_optimo}")

if __name__ == "__main__":
    test_todas_funciones()
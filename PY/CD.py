import math

# Definición de constantes globales
A = 1.0  # Definición de la amplitud A para las señales
R = 1.0  # Definición de R para las prestaciones
delta_F = 1.0  # Definición de delta_F para FSK
M = 4  # Número de símbolos para MPSK y MFSK
L = 4  # Número de bits por elemento de señalización para MPSK y MFSK
A_c = None  # Variable global para A_c, inicializada en None

# Funciones para obtener n_a(t) y ø(t)
def n_a(t):
    # Definición de n_a(t) según tu implementación
    return math.sin(2 * math.pi * t)

def ø(t):
    # Definición de ø(t) según tu implementación
    return math.cos(2 * math.pi * t)

# Función para mostrar el menú principal
def mostrar_menu_principal():
    print("\nTrabajo práctico de Comunicación de Datos")
    print("Realizado por: Herrera, Hidalgo, Mora, Muñoz & Tivan (2024)")
    print("Modulación y codificación de datos")
    print("1. Datos digitales, señales digitales")
    print("2. Datos digitales, señales analógicas")
    print("3. Datos analógicos, señales analógicas")
    print("4. Salir")
    return input("Elija una opción [1 – 4]: ")

# Función para obtener un número flotante desde la entrada del usuario
def obtener_numero_flotante(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Función para obtener un número entero desde la entrada del usuario
def obtener_numero_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

# Función para la opción 1: Datos digitales, señales digitales
def datos_digitales_senales_digitales():
    print("\nDatos digitales, señales digitales")
    R = obtener_numero_flotante("Ingrese el valor de R: ")
    L = obtener_numero_flotante("Ingrese el valor de L: ")
    M = obtener_numero_entero("Ingrese el valor de M: ")
    
    D_formula = "D = R / (L * math.log2(M))"
    
    D = R / (L * math.log2(M))
    
    print("\nFórmula utilizada:")
    print(D_formula)
    print("\nResultado:")
    print(f"D = {D}\n")

# Función para la opción 2: Datos digitales, señales analógicas
def datos_digitales_senales_analogicas():
    print("\nDatos digitales, señales analógicas")
    print("Seleccione el tipo de modulación:")
    print("1. Modulación ASK")
    print("2. Modulación PSK de dos niveles")
    print("3. Modulación PSK de cuatro niveles")
    print("4. Prestaciones")
    print("5. Modulación de amplitud en cuadratura (QAM)")
    
    while True:
        opcion = input("Elija una opción [1 - 5]: ")
        if opcion in ["1", "2", "3", "4", "5"]:
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

    if opcion == "1":
        calcular_ask()
    elif opcion == "2":
        calcular_psk_2niveles()
    elif opcion == "3":
        calcular_psk_4niveles()
    elif opcion == "4":
        calcular_prestaciones()
    elif opcion == "5":
        calcular_qam()

# Función para la opción 3: Datos analógicos, señales analógicas
def datos_analogicos_senales_analogicas():
    print("\nDatos analógicos, señales analógicas")
    print("Seleccione el tipo de modulación:")
    print("1. Modulación de Amplitud")
    print("2. Modulación Angular")
    
    while True:
        opcion = input("Elija una opción [1 - 2]: ")
        if opcion in ["1", "2"]:
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

    if opcion == "1":
        calcular_am()
    elif opcion == "2":
        calcular_angular()

# Función para calcular la modulación ASK
def calcular_ask():
    global A_c  # Definición global de A_c para que sea accesible fuera de la función
    fc = obtener_numero_flotante("Ingrese el valor de fc para ASK: ")
    t = obtener_numero_flotante("Ingrese el valor de t para ASK: ")
    
    A_c = 1.0  # Definición de A_c para ASK (puedes ajustar este valor según tu necesidad)
    s_formula = "s(t) = A_c * cos(2 * math.pi * fc * t)"
    
    s = A_c * math.cos(2 * math.pi * fc * t)
    
    print("\nFórmula utilizada:")
    print(s_formula)
    print("\nResultado:")
    print(f"s(t) para ASK: s(t) = {s}\n")

# Función para calcular la modulación PSK de dos niveles
def calcular_psk_2niveles():
    fc = obtener_numero_flotante("Ingrese el valor de fc para PSK 2 niveles: ")
    t = obtener_numero_flotante("Ingrese el valor de t para PSK 2 niveles: ")
    
    s1_formula = "s(t) = A * cos(2 * math.pi * fc * t)"
    s0_formula = "s(t) = -A * cos(2 * math.pi * fc * t)"
    
    s1 = A * math.cos(2 * math.pi * fc * t)
    s0 = -A * math.cos(2 * math.pi * fc * t)
    
    print("\nFormulas utilizadas:")
    print(s1_formula)
    print(s0_formula)
    print("\nResultados:")
    print(f"PSK 2 niveles, s(t) para 1 binario: {s1}")
    print(f"PSK 2 niveles, s(t) para 0 binario: {s0}\n")

# Función para calcular la modulación PSK de cuatro niveles
def calcular_psk_4niveles():
    fc = obtener_numero_flotante("Ingrese el valor de fc para PSK 4 niveles: ")
    t = obtener_numero_flotante("Ingrese el valor de t para PSK 4 niveles: ")
    
    s11_formula = "s(t) = A * cos(2 * math.pi * fc * t + math.pi / 4)"
    s01_formula = "s(t) = A * cos(2 * math.pi * fc * t + 3 * math.pi / 4)"
    s00_formula = "s(t) = A * cos(2 * math.pi * fc * t - 3 * math.pi / 4)"
    s10_formula = "s(t) = A * cos(2 * math.pi * fc * t - math.pi / 4)"
    
    s11 = A * math.cos(2 * math.pi * fc * t + math.pi / 4)
    s01 = A * math.cos(2 * math.pi * fc * t + 3 * math.pi / 4)
    s00 = A * math.cos(2 * math.pi * fc * t - 3 * math.pi / 4)
    s10 = A * math.cos(2 * math.pi * fc * t - math.pi / 4)
    
    print("\nFormulas utilizadas:")
    print(f"PSK 4 niveles, s(t) para 11: {s11_formula}")
    print(f"PSK 4 niveles, s(t) para 01: {s01_formula}")
    print(f"PSK 4 niveles, s(t) para 00: {s00_formula}")
    print(f"PSK 4 niveles, s(t) para 10: {s10_formula}")
    print("\nResultados:")
    print(f"PSK 4 niveles, s(t) para 11: {s11}")
    print(f"PSK 4 niveles, s(t) para 01: {s01}")
    print(f"PSK 4 niveles, s(t) para 00: {s00}")
    print(f"PSK 4 niveles, s(t) para 10: {s10}\n")

# Función para calcular las prestaciones
def calcular_prestaciones():
    P = obtener_numero_flotante("Ingrese el valor de P (potencia de la señal): ")
    N0 = obtener_numero_flotante("Ingrese el valor de N0 (densidad espectral de potencia): ")

    r = P / N0  # Relación señal a ruido

    # Cálculo de las prestaciones según las fórmulas proporcionadas
    B_ask = (1 + r) * R
    B_fsk = 2 * delta_F + (1 + r) * R
    B_mpsk = (1 + r / L) * R
    B_mfsk = ((1 + r) * R * M) / math.log2(M)

    print("\nFórmulas utilizadas:")
    print(f"B_ask = (1 + r) * R")
    print(f"B_fsk = 2 * delta_F + (1 + r) * R")
    print(f"B_mpsk = (1 + r / L) * R")
    print(f"B_mfsk = ((1 + r) * R * M) / log2(M)")
    print("\nResultados:")
    print(f"Prestaciones ASK: B_ask = {B_ask}")
    print(f"Prestaciones FSK: B_fsk = {B_fsk}")
    print(f"Prestaciones MPSK: B_mpsk = {B_mpsk}")
    print(f"Prestaciones MFSK: B_mfsk = {B_mfsk}\n")

# Función para calcular la modulación de amplitud en cuadratura (QAM)
def calcular_qam():
    fc = obtener_numero_flotante("Ingrese el valor de fc para QAM: ")
    t = obtener_numero_flotante("Ingrese el valor de t para QAM: ")
    
    d1 = obtener_numero_flotante("Ingrese el valor de d1(t) para QAM: ")
    d2 = obtener_numero_flotante("Ingrese el valor de d2(t) para QAM: ")
    
    s_formula = "s(t) = d1 * t * (cos(2 * math.pi * fc * t) + d2 * (t) * sin(2 * t * math.pi))"
    
    s = d1 * t * (math.cos(2 * math.pi * fc * t) + d2 * t * math.sin(2 * t * math.pi))
    
    print("\nFórmula utilizada:")
    print(s_formula)
    print("\nResultado:")
    print(f"s(t) para Modulación de Amplitud en Cuadratura (QAM): s(t) = {s}\n")

# Función para calcular la modulación de amplitud (AM)
def calcular_am():
    fc = obtener_numero_flotante("Ingrese el valor de fc para AM: ")
    t = obtener_numero_flotante("Ingrese el valor de t para AM: ")
    
    s_formula = "s(t) = [1 + n_a(t)] * cos(2 * math.pi * fc * t)"
    
    s = (1 + n_a(t)) * math.cos(2 * math.pi * fc * t)
    
    print("\nFórmula utilizada:")
    print(s_formula)
    print("\nResultado:")
    print(f"s(t) para Modulación de Amplitud: s(t) = {s}\n")

# Función para calcular la modulación angular
def calcular_angular():
    global A_c
    fc = obtener_numero_flotante("Ingrese el valor de fc para Modulación Angular: ")
    t = obtener_numero_flotante("Ingrese el valor de t para Modulación Angular: ")
    
    if A_c is None:
        calcular_ask()
    
    s_formula = "s(t) = A_c * cos(2 * math.pi * fc * t + ø(t))"
    
    s = A_c * math.cos(2 * math.pi * fc * t + ø(t))
    
    print("\nFórmula utilizada:")
    print(s_formula)
    print("\nResultado:")
    print(f"s(t) para Modulación Angular: s(t) = {s}\n")

# Función principal para ejecutar el programa
def main():
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == "1":
            datos_digitales_senales_digitales()
        elif opcion == "2":
            datos_digitales_senales_analogicas()
        elif opcion == "3":
            datos_analogicos_senales_analogicas()
        elif opcion == "4":
            print("¡Gracias por usar el programa!")
            break
        else:
            print("Opción no válida, intente de nuevo")

if __name__ == "__main__":
    main()

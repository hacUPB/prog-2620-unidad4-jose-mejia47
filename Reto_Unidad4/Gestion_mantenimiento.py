flota = {}
ESTADOS = ("OPERATIVO", "MANTENIMIENTO REQUERIDO")

print("INICIO DEL REGISTRO DE FLOTA")

n_aeronaves = int(input("Ingrese la cantidad de aeronaves a registrar"))

while n_aeronaves < 3:
    print("Error el sistema requiere al menos 3 aeronaves")
    n_aeronaves = int(input("Ingrese la cantidad de aeronaves a registrar"))

for i in range(n_aeronaves):
    print(f"\nDatos de la aeronave {i+1}:")
    matricula = input("Matrícula:")
    modelo = input("Modelo:")
    horas_totales = float(input("Horas de vuelo acumuladas:"))
    
    flota[matricula] = {
        "modelo": modelo,
        "horas_vuelo": horas_totales,
        "componentes": []
    }
print("\nREGISTRO DE COMPONENTES CRÍTICOS")

for matricula in flota:
    print(f"\nConfigurando componentes para {matricula}: ")
    n_piezas = int(input(f"¿Cuántas piezas registrará para el {matricula}?: "))
    
    for i in range(n_piezas):
        nombre_pieza = input(f"Nombre de la pieza {i+1}: ")
        uso_actual = float(input(f"Horas de uso de {nombre_pieza}: "))
        limite_max = float(input(f"Límite de horas para mantenimiento: "))
        
       
        pieza_datos = {
            "nombre": nombre_pieza,
            "uso": uso_actual,
            "limite": limite_max
        }
        flota[matricula]["componentes"].append(pieza_datos)

print("REPORTE TÉCNICO DE MANTENIMIENTO")

hallazgos = 0

for matricula in flota:
    datos_avion = flota[matricula]
    lista_piezas = datos_avion["componentes"]
    
    for pieza in lista_piezas:
        if pieza["uso"] >= pieza["limite"]:
            hallazgos += 1
            estado_actual = ESTADOS[1] 
            print(f"ALERTA:{matricula} | Modelo: {datos_avion["modelo"]}")
            print(f"- COMPONENTE:{pieza['nombre']}")
            print(f"- CONDICIÓN:{pieza['uso']} horas / {pieza["limite"]} horas")
            print(f"- ESTADO:{estado_actual}")
           
if hallazgos == 0:
    print("No se encontraron componentes que requieran mantenimiento")
    print(f"Estado general de la flota: {ESTADOS[0]}")

print("\nFin del proceso de gestión")

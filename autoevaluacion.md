# 📝 Plantilla de Autoevaluación: Gestión de Mantenimiento de Flota Aeronáutica ✈️

**Instrucciones para los estudiantes:**
1. Hagan una copia de este archivo y guárdenlo en la raíz de su repositorio con el nombre `AUTOEVALUACION.md`.
2. Lean cuidadosamente cada criterio de la rúbrica.
3. En el apartado **Nota Esperada**, asignen una calificación numérica (de 0.0 a 5.0) que consideren justa para su trabajo en ese criterio.
4. En el apartado **Justificación**, expliquen con sus propias palabras por qué merecen esa nota. Sean críticos y honestos.
5. En el apartado **Evidencia**, inserten pantallazos de la ejecución de la consola, imágenes de su diagrama o bloques de código (usando la sintaxis de Markdown con \`\`\`) que respalden su justificación.
6. Al final, calculen su nota definitiva esperada según los porcentajes.

---

## 👥 1. Información del Equipo

* JOSÉ MANUEL MEJÍA BERRIO - 000574830

---

## 📊 2. Evaluación por Criterios

### Criterio 1: Diagrama y Lógica (Valor: 20%)
*Evalúa si el diagrama es claro, lógico y representa fielmente la estructura de datos utilizada (listas/diccionarios) y el flujo del programa.*

* **Nota Esperada (0.0 - 5.0):** 5.0
* **Justificación:** 
  > *realice el diagrama de manera que cumpliera con todas las exigencias propuestas por el docente y quedo con una estructura clara tanto en el proceso que realiza el codigo como la idea clara de como se almacenan los datos dentro de este*
* **Evidencia:**
  ![Diagrama de bloques](diagrama%20de%20bloques%20JMMB.png)

### Criterio 2: Uso de Estructuras (Listas y Diccionarios) (Valor: 30%)
*Evalúa si se utilizaron diccionarios y listas de manera correcta y anidada para almacenar los datos ingresados por el usuario, sin redundancias.*

* **Nota Esperada (0.0 - 5.0):** 5.0
* **Justificación:**
  > *se utilizaron diccionarios de forma adecuada para cumplir con el mejor funciuonamiento posible para la ejecucion y estructura amigable para entender la estructura del ejercicio*
* **Evidencia:**
flota = {}

flota[matricula] = {
        "modelo": modelo,
        "horas_vuelo": horas_totales,
        "componentes": []
}

 pieza_datos = {
            "nombre": nombre_pieza,
            "uso": uso_actual,
            "limite": limite_max
        }
        

### Criterio 3: Cumplimiento de Restricciones Técnicas (Valor: 20%)
*Evalúa el respeto total a las reglas: uso de ciclos clásicos (for/while), cero uso de list comprehensions, y ninguna librería/función avanzada no vista en clase.*

* **Nota Esperada (0.0 - 5.0):** 5.0
* **Justificación:**
    > *no se utilizo ningún ciclo diferente a los clasicos trabajados en clase, todo se estructuro en ciclos for/while.*
* 
while n_aeronaves < 3:
    print("Error el sistema requiere al menos 3 aeronaves")
    n_aeronaves = int(input("Ingrese la cantidad de aeronaves a registrar"))

for i in range(n_aeronaves):
    print(f"\nDatos de la aeronave {i+1}:")
    matricula = input("Matrícula:")
    modelo = input("Modelo:")
    horas_totales = float(input("Horas de vuelo acumuladas:"))

### Criterio 4: Funcionalidad del Código (Valor: 15%)
*Evalúa si el programa pide datos correctamente, no se "crashea" y genera el reporte final de mantenimiento esperado.*

* **Nota Esperada (0.0 - 5.0):** 5.0
* **Justificación:**
    > *el programa funciona correctamente en su totalidad y pide los datos de manera correcta*
* **Evidencia:** *Inserta aquí 1 o 2 pantallazos (![Ejecución](./img/consola1.png)) mostrando la terminal donde se vea:*
![Ejecución](INICIO%20RETO%20UNIDAD%204.PNG)
![Ejecución](RESULTADO%20RETO%20UNIUDAD%204.PNG)


### Criterio 5: Preparación para Sustentación (Valor: 15%)
*Aunque esta nota la dará el profesor en la entrevista oral, autoevalúen su nivel de preparación y comprensión del código que entregaron.*

* **Nivel de Confianza (Bajo / Medio / Alto):** 4.5
* **Justificación:**
    > * llegue a la entrega con el conocimiento total de el funcionamiento y estructura de mi codigo.
* ** realice el codigo de manera individual con comentarios de compañeros y del docente

### 📈 3. Cálculo de Nota Definitiva Esperada
Multipliquen la nota asignada en cada criterio por su porcentaje respectivo y sumen los resultados para obtener su nota final esperada.

|Criterio	|Nota |Asignada	|Peso	|Subtotal |(Nota * Peso) |
|---|---|---|---|---|---|
|1. Diagrama y Lógica	|[Nota]	|20% |(0.2)	|[Resultado]|
|2. Uso de Estructuras	|[Nota]	|30% |(0.3)	|[Resultado]|
|3. Cumplimiento Restricciones|	[Nota]	|20% |(0.2)	|[Resultado]|
|4. Funcionalidad	|[Nota]	|15% |(0.15)	|[Resultado]|
|5. Sustentación (Estimado)|	[Nota]|	15%| (0.15)|	[Resultado]|

NOTA FINAL ESPERADA		100% = 4.8

✨ ""La educación es para el carácter, no solo para la mente"." ✨
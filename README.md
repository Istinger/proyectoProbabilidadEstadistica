# Guía Interactiva de Permutaciones y Combinaciones

## Descripción

Esta es una **aplicación educativa interactiva** que enseña los conceptos fundamentales de probabilidad y combinatoria. Incluye contenido teórico embebido, una calculadora integrada y la capacidad de procesar ejercicios en lotes desde archivos de texto.

Conceptos cubiertos:
- **Factorial**: Cálculo y aplicaciones
- **Permutaciones**: Arreglos donde el orden importa
- **Combinaciones**: Agrupaciones donde el orden no importa

## Estructura del Proyecto

```
proyecto/
├── proba.py                      # Aplicación principal (interfaz Tkinter)
├── ejercicios.txt                # Archivo de entrada con operaciones
├── resultados_ejercicio1.csv     # Resultados de ejemplo #1
├── resultados_ejercicio2.csv     # Resultados de ejemplo #2
├── ejercicio1.txt                # Documentación de ejercicios
└── ejercicios.txt                # Listado adicional de ejercicios
```

**Archivos principales:**
- [proba.py](proba.py) - Aplicación principal con interfaz gráfica (Tkinter)
- [ejercicios.txt](proyecto/ejercicios.txt) - Archivo de entrada para procesar lotes
- [resultados_ejercicio1.csv](proyecto/resultados_ejercicio1.csv) - Ejemplo de salida CSV
- [resultados_ejercicio2.csv](proyecto/resultados_ejercicio2.csv) - Segundo ejemplo de salida

## Requisitos

- **Python 3.x**
- **tkinter** (incluido en Python estándar)

## Instalación y Ejecución

Para ejecutar la aplicación:

```bash
python proba.py
```

Esto abrirá una ventana con interfaz gráfica de **700x500 píxeles** con dos paneles principales.

## Características Principales

✓ **Guía Interactiva** - 7 temas con contenido teórico completo  
✓ **Calculadora Integrada** - Calcula permutaciones y combinaciones al instante  
✓ **Carga de Archivos** - Importa ejercicios desde archivos .txt  
✓ **Exportación CSV** - Guarda resultados en hojas de cálculo  
✓ **Referencias Bibliográficas** - Incluye fuentes académicas  

## Guía de Uso

### 1. Explorar la Guía Teórica

La aplicación contiene 7 temas disponibles en el menú lateral izquierdo:

- **Introducción** - Bienvenida y descripción general
- **Factorial** - Definición y ejemplos de factorial
- **Permutaciones** - Concepto y fórmula P(n,r) = n! / (n-r)!
- **Combinaciones** - Concepto y fórmula C(n,r) = n! / (r!(n-r)!)
- **Ejercicios Resueltos** - Ejemplos prácticos paso a paso
- **Bibliografía** - Referencias académicas completas
- **Guía de Uso** - Instrucciones detalladas de uso

Selecciona un tema de la lista para visualizar su contenido en el panel derecho.

### 2. Usar la Calculadora

**Panel inferior de la ventana:**

1. Ingresa un valor entero en el campo **n**
2. Ingresa un valor entero en el campo **r**
3. Selecciona el tipo de operación:
   - **Permutación** - Cuando el orden importa
   - **Combinación** - Cuando el orden no importa
4. Presiona el botón **"Calcular"**

El resultado se mostrará en una ventana emergente con la fórmula aplicada.

**Ejemplo:**
- n = 5, r = 3, Permutación → Resultado: 60
- n = 5, r = 2, Combinación → Resultado: 10

### 3. Cargar Archivos de Ejercicios

La aplicación permite procesar múltiples operaciones desde un archivo de texto.

**Formato de archivo .txt:**

Cada línea debe tener la estructura:
```
OPERACIÓN,n,r
```

Donde:
- `OPERACIÓN` = `P` para permutación o `C` para combinación
- `n` = Número total de elementos
- `r` = Número de elementos a seleccionar/arreglar

**Ejemplo de archivo (ejercicios.txt):**
```
P,5,3
C,6,2
P,4,2
```

**Resultado esperado en CSV:**
```
Operacion,n,r,resultado
P,5,3,60
C,6,2,15
P,4,2,12
```

**Pasos:**
1. Presiona el botón **"Cargar archivo"**
2. Selecciona el archivo .txt
3. El sistema procesará automáticamente los datos
4. Se abrirá un cuadro de diálogo para guardar los resultados

### 4. Exportar Resultados a CSV

Después de procesar un archivo, la aplicación solicita una ubicación para guardar los resultados.

**Archivo CSV generado contiene:**
- **Operación** - Tipo de cálculo (P o C)
- **n** - Parámetro n
- **r** - Parámetro r
- **resultado** - Valor calculado

Puedes abrir el archivo .csv en Excel, LibreOffice Calc o cualquier software de hojas de cálculo.

## Notas Importantes

⚠️ Los valores n y r deben ser **números enteros positivos**  
⚠️ Se recomienda que **r ≤ n** para evitar errores matemáticos  
⚠️ El archivo .txt debe respetar el **formato indicado** (sin espacios)  
⚠️ Los archivos .txt deben usar separadores de coma (`,`)  
⚠️ Cada línea debe tener exactamente 3 elementos: `OPERACIÓN,n,r`  
⚠️ No se procesan líneas vacías o con formato incorrecto  

## Manejo de Errores

- Si ingresa **valores no numéricos**, la aplicación mostrará un mensaje de error
- Si el archivo .txt tiene **formato incorrecto**, el programa puede generar una excepción
- Asegúrese de que **n ≥ r** antes de procesar para evitar resultados indefinidos
- Si intenta guardar el CSV en una **carpeta protegida**, el sistema lo notificará

## Ejemplos de Uso

### Cálculo Manual
- **Permutación:** n=5, r=3 → P(5,3) = 60
- **Combinación:** n=5, r=2 → C(5,2) = 10
- **Factorial:** 5! = 120

### Procesamiento por Lotes
Entrada (`ejercicios.txt`):
```
P,5,3
C,6,2
P,4,2
```

Salida (`resultados.csv`):
```
Operacion,n,r,resultado
P,5,3,60
C,6,2,15
P,4,2,12
```

## Conceptos Matemáticos

### Factorial
**Definición:** n! = n · (n-1) · (n-2) · ... · 1

**Ejemplo:** 5! = 5·4·3·2·1 = 120

### Permutaciones
**Concepto:** Arreglos donde **el orden IMPORTA**

**Fórmula:** P(n,r) = n! / (n-r)!

**Ejemplo:** Ordenar 3 personas de un grupo de 5
- P(5,3) = 5! / 2! = 120 / 2 = 60

### Combinaciones
**Concepto:** Agrupaciones donde **el orden NO importa**

**Fórmula:** C(n,r) = n! / (r! × (n-r)!)

**Ejemplo:** Elegir 3 estudiantes de un grupo de 5
- C(5,3) = 5! / (3! × 2!) = 120 / (6 × 2) = 10

## Funcionalidades

- ✓ Interfaz gráfica interactiva con 7 temas educativos
- ✓ Calculadora integrada para permutaciones y combinaciones
- ✓ Importación y procesamiento de ejercicios en lotes desde archivos .txt
- ✓ Exportación de resultados a archivos .csv con formato estándar
- ✓ Contenido teórico completo embebido (sin dependencias externas)
- ✓ Referencias bibliográficas académicas
- ✓ Validación de entrada con manejo de errores
- ✓ Interfaz clara y fácil de usar (700x500 píxeles)

## Requisitos Matemáticos Importantes

- Los valores de **n y r deben ser enteros no-negativos**
- Para permutaciones y combinaciones: **r ≤ n**
- Si r > n, los resultados serán matemáticamente indefinidos

## Referencias Bibliográficas

1. Devore, J. L. (2016). Probabilidad y Estadística para Ingeniería y Ciencias. Cengage Learning.
2. Walpole, R. E., Myers, R. H. Probabilidad y Estadística para Ingenieros. Pearson Educación.
3. Ross, S. M. Introducción a la Probabilidad. Academic Press.
4. Apuntes de clase – Universidad Politécnica Salesiana

## Autor

Proyecto educativo de Probabilidad y Estadística  
Grupo: El mejor grupo

## Licencia

Libre para uso educativo


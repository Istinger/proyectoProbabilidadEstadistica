import tkinter as tk
from tkinter import messagebox, filedialog
import math
import csv

# CONTENIDO TEÓRICO EMBEBIDO

GUIA = {
    "Introducción": """
BIENVENIDO A LA GUÍA DE PERMUTACIONES Y COMBINACIONES El mejor grupo

Esta guía explica los conceptos fundamentales de probabilidad
relacionados con conteo:

• Factorial
• Permutaciones (orden importa)
• Combinaciones (orden no importa)

Todo el contenido está embebido en este archivo .py
""",

    "Factorial": """
FACTORIAL

Definición:
n! = n · (n-1) · (n-2) · ... · 1

Ejemplo:
5! = 5·4·3·2·1 = 120

En probabilidad, el factorial se usa como base
para calcular permutaciones y combinaciones.
""",

    "Permutaciones": """
PERMUTACIONES

Una permutación es un arreglo de elementos
DONDE EL ORDEN IMPORTA.

Fórmula:
P(n,r) = n! / (n-r)!

Ejemplo:
Ordenar 3 personas de un grupo de 5:

P(5,3) = 5! / 2! = 60
""",

    "Combinaciones": """
COMBINACIONES

Una combinación es una selección de elementos
DONDE EL ORDEN NO IMPORTA.

Fórmula:
C(n,r) = n! / (r!(n-r)!)

Ejemplo:
Elegir 3 estudiantes de un grupo de 5:

C(5,3) = 10
""",

    "Ejercicios Resueltos": """
EJERCICIO 1:
¿Cuántas formas hay de ordenar 4 libros?

Paso 1: El orden importa → Permutación
Paso 2: P(4,4) = 4! = 24

EJERCICIO 2:
Elegir 2 cartas de un grupo de 5

Paso 1: El orden no importa → Combinación
Paso 2: C(5,2) = 10
""",

"Bibliografía": """
BIBLIOGRAFÍA

1. Devore, J. L. (2016).
   Probabilidad y Estadística para Ingeniería y Ciencias.
   Cengage Learning.

2. Walpole, R. E., Myers, R. H.
   Probabilidad y Estadística para Ingenieros.
   Pearson Educación.

3. Ross, S. M.
   Introducción a la Probabilidad.
   Academic Press.

4. Apuntes de clase – Universidad Politécnica Salesiana
"""
,
"Guía de Uso": """
GUÍA DE USO DE LA APLICACIÓN

1. USO DE LA CALCULADORA

La calculadora se encuentra en la parte inferior de la ventana.

Pasos:
1. Ingrese un valor entero en el campo n.
2. Ingrese un valor entero en el campo r.
3. Seleccione el tipo de operación:
   - Permutación (cuando el orden importa)
   - Combinación (cuando el orden no importa)
4. Presione el botón "Calcular".

El resultado se mostrará en una ventana emergente junto
con la fórmula aplicada.

----------------------------------------

2. CARGA DE ARCHIVOS .TXT

La aplicación permite cargar un archivo de texto con
operaciones múltiples.

Formato del archivo (.txt):
Cada línea debe tener la siguiente estructura:

P,n,r   → para permutaciones
C,n,r   → para combinaciones

Ejemplo:
P,5,3
C,5,2
P,4,4

Pasos:
1. Presione el botón "Cargar archivo".
2. Seleccione el archivo .txt.
3. El sistema procesará automáticamente los datos.

----------------------------------------

3. EXPORTACIÓN DE RESULTADOS A .CSV

Después de procesar el archivo .txt, la aplicación
solicitará una ubicación para guardar los resultados.

El archivo .csv generado contiene las columnas:
- Operación
- n
- r
- Resultado

Este archivo puede abrirse en Excel, LibreOffice
o cualquier software de hojas de cálculo.

----------------------------------------

NOTAS IMPORTANTES:
- Los valores n y r deben ser números enteros.
- Se recomienda que r ≤ n para evitar errores matemáticos.
- El archivo .txt debe respetar el formato indicado.
"""



}

# FUNCIONES MATEMÁTICAS

def factorial(n):
    return math.factorial(n)

def permutacion(n, r):
    return factorial(n) // factorial(n - r)

def combinacion(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

# FUNCIONES GUI

def mostrar_contenido(event):
    seleccion = lista.get(lista.curselection())
    texto.config(state="normal")        # Habilita temporalmente
    texto.delete("1.0", tk.END)
    texto.insert(tk.END, GUIA[seleccion])
    texto.config(state="disabled")      # Bloquea edición


def calcular():
    try:
        n = int(entry_n.get())
        r = int(entry_r.get())

        if opcion.get() == "P":
            resultado = permutacion(n, r)
            explicacion = f"P({n},{r}) = {n}! / ({n}-{r})! = {resultado}"
        else:
            resultado = combinacion(n, r)
            explicacion = f"C({n},{r}) = {n}! / ({r}!·({n}-{r})!) = {resultado}"

        messagebox.showinfo("Resultado", explicacion)
    except:
        messagebox.showerror("Error", "Datos inválidos")

def cargar_archivo():
    archivo = filedialog.askopenfilename(
        filetypes=[("Archivos de texto", "*.txt")]
    )

    if not archivo:
        return

    resultados = []

    with open(archivo, "r") as f:
        for linea in f:
            tipo, n, r = linea.strip().split(",")
            n, r = int(n), int(r)

            if tipo == "P":
                resultado = permutacion(n, r)
            else:
                resultado = combinacion(n, r)

            resultados.append([tipo, n, r, resultado])

    guardar_csv(resultados)

def guardar_csv(resultados):
    archivo_csv = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("Archivo CSV", "*.csv")]
    )

    if not archivo_csv:
        return

    with open(archivo_csv, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Operacion", "n", "r", "resultado"])
        writer.writerows(resultados)

    messagebox.showinfo(
        "CSV generado",
        "Los resultados se guardaron correctamente."
    )

# INTERFAZ PRINCIPAL

ventana = tk.Tk()
ventana.title("Guía Interactiva de Permutaciones y Combinaciones")
ventana.geometry("700x500")

# Menú lateral
lista = tk.Listbox(ventana, width=30)
for tema in GUIA:
    lista.insert(tk.END, tema)
lista.bind("<<ListboxSelect>>", mostrar_contenido)
lista.pack(side="left", fill="y")

# Área de texto
texto = tk.Text(ventana, wrap="word", state="disabled")
texto.pack(expand=True, fill="both")

# Panel inferior
panel = tk.Frame(ventana, pady=10)
panel.pack(side="bottom", fill="x")

tk.Label(panel, text="n", font=("Arial", 12)).grid(row=0, column=0, padx=5)
entry_n = tk.Entry(panel, width=10, font=("Arial", 12))
entry_n.grid(row=0, column=1, padx=10)

tk.Label(panel, text="r", font=("Arial", 12)).grid(row=0, column=2, padx=5)
entry_r = tk.Entry(panel, width=10, font=("Arial", 12))
entry_r.grid(row=0, column=3, padx=10)

opcion = tk.StringVar(value="P")

tk.Radiobutton(
    panel, text="Permutación", variable=opcion, value="P",
    font=("Arial", 11)
).grid(row=1, column=0, columnspan=2, pady=5)

tk.Radiobutton(
    panel, text="Combinación", variable=opcion, value="C",
    font=("Arial", 11)
).grid(row=1, column=2, columnspan=2, pady=5)

tk.Button(
    panel, text="Calcular", command=calcular,
    font=("Arial", 11), width=15
).grid(row=2, column=0, columnspan=2, pady=8)

tk.Button(
    panel, text="Cargar archivo", command=cargar_archivo,
    font=("Arial", 11), width=18
).grid(row=2, column=2, columnspan=2, pady=8)


ventana.mainloop()

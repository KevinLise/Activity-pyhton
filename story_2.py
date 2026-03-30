# ============================================================
# PROGRAMA: Registro de Inventario
# DESCRIPCIÓN: Este programa solicita al usuario el nombre,
# precio y cantidad de un producto, valida los datos de
# entrada, calcula el costo total y muestra el resultado
# en consola con formato claro.
# ============================================================


# --- Solicitar y validar el nombre del producto ---
nombre = input("Ingrese el nombre del producto: ").strip()
while nombre == "":
    print("⚠ El nombre no puede estar vacío. Intente de nuevo.")
    nombre = input("Ingrese el nombre del producto: ").strip()


# --- Solicitar y validar el precio unitario (float) ---
while True:
    try:
        precio = float(input("Ingrese el precio unitario: "))
        if precio <= 0:
            print("⚠ El precio debe ser un número positivo. Intente de nuevo.")
        else:
            break
    except ValueError:
        print("⚠ Valor inválido. Ingrese un número decimal válido (ej: 1500.50).")


# --- Solicitar y validar la cantidad (int) ---
while True:
    try:
        cantidad = int(input("Ingrese la cantidad en inventario: "))
        if cantidad <= 0:
            print("⚠ La cantidad debe ser un número entero positivo. Intente de nuevo.")
        else:
            break
    except ValueError:
        print("⚠ Valor inválido. Ingrese un número entero válido (ej: 10).")


# --- Calcular el costo total (precio * cantidad) ---
costo_total = precio * cantidad


# --- Mostrar el resultado en consola con formato claro ---
print("\n" + "=" * 55)
print(f"  Producto : {nombre}")
print(f"  Precio   : ${precio:,.2f}")
print(f"  Cantidad : {cantidad} unidades")
print(f"  Total    : ${costo_total:,.2f}")
print("=" * 55)

# ============================================================
# RESUMEN DEL PROGRAMA:
# 1. Lee el nombre del producto como texto (str).
# 2. Lee el precio como número decimal (float), validando
#    que sea un valor numérico positivo.
# 3. Lee la cantidad como número entero (int), validando
#    que sea un valor entero positivo.
# 4. Calcula costo_total = precio * cantidad.
# 5. Imprime un resumen formateado con todos los datos.
# Si cualquier entrada es inválida, el programa muestra
# un mensaje de error y solicita el dato nuevamente.
# ============================================================
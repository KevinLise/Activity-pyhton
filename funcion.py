heroe = {
    1: {
        "id": 100327560,
        "nombre": "spiderman",
        "edad": "21",
        "power": "perseverance"
    },
    2: {
        "id": 100326570,
        "nombre": "ghos raider",
        "edad": "36",
        "power": "Absolute Justice"
    },
    3: {
        "id": 100326590,
        "nombre": "Goku Black",
        "edad": "1000",
        "power": "Super Saiyan Rose Black",
    }
}

# ──────────────────────────────────────────
# FUNCIONES
# ──────────────────────────────────────────

def mostrar_heroes():
    if len(heroe) == 0:
        print("No hay heroes registrados.")
        return
    print("\n── Lista de heroes ──")
    for llave, datos in heroe.items():
        print(f"\nSlot {llave}:")
        print(f"  ID     : {datos['id']}")
        print(f"  Nombre : {datos['nombre']}")
        print(f"  Edad   : {datos['edad']}")
        print(f"  Power  : {datos['power']}")

def agregar_heroe():
    nueva_llave = len(heroe) + 1
    print(f"\nNuevo heroe ocupara el slot {nueva_llave}")
    nuevo_id   = input("ID      : ")
    nuevo_nom  = input("Nombre  : ")
    nueva_edad = input("Edad    : ")
    nuevo_pow  = input("Power   : ")

    heroe[nueva_llave] = {
        "id":     nuevo_id,
        "nombre": nuevo_nom,
        "edad":   nueva_edad,
        "power":  nuevo_pow
    }
    print(f"Heroe '{nuevo_nom}' agregado en slot {nueva_llave}.")

def eliminar_heroe():
    mostrar_heroes()
    try:
        llave = int(input("\nNumero de slot a eliminar: "))
        if llave in heroe:
            nombre = heroe[llave]["nombre"]
            del heroe[llave]
            print(f"Heroe '{nombre}' eliminado.")
        else:
            print("Slot no encontrado.")
    except ValueError:
        print("Ingresa un numero valido.")

def buscar_por_id():
    try:
        busqueda_id = int(input("Ingresa el ID a buscar: "))
        encontrado = None
        for llave, datos in heroe.items():
            if datos["id"] == busqueda_id:
                encontrado = datos
                break
        if encontrado:
            print(f"\nHeroe encontrado: {encontrado}")
        else:
            print("No se encontro un heroe con ese ID.")
    except ValueError:
        print("Ingresa un numero valido.")

# ──────────────────────────────────────────
# MENU PRINCIPAL
# ──────────────────────────────────────────

while True:
    print("\n════════════════════")
    print("   MENU DE HEROES   ")
    print("════════════════════")
    print("1. Mostrar todos")
    print("2. Agregar heroe")
    print("3. Eliminar heroe")
    print("4. Buscar por ID")
    print("5. Salir")

    opcion = input("\nElige una opcion: ")

    if opcion == "1":
        mostrar_heroes()
    elif opcion == "2":
        agregar_heroe()
    elif opcion == "3":
        eliminar_heroe()
    elif opcion == "4":
        buscar_por_id()
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opcion invalida, intenta de nuevo.")
from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


# Tupla: opciones estables del menú
OPCIONES_MENU = (
    ("1", "Registrar producto"),
    ("2", "Buscar producto"),
    ("3", "Actualizar producto"),
    ("4", "Eliminar producto"),
    ("5", "Listar productos"),
    ("6", "Registrar usuario"),
    ("7", "Listar usuarios"),
    ("8", "Mostrar categorías"),
    ("9", "Salir"),
)


def mostrar_menu() -> None:
    print("\n" + "=" * 45)
    print("        SISTEMA DE RESTAURANTE")
    print("=" * 45)

    for numero, descripcion in OPCIONES_MENU:
        print(f"{numero}. {descripcion}")

    print("=" * 45)


def leer_precio() -> float:
    while True:
        try:
            precio = float(input("Precio: "))

            if precio < 0:
                print("El precio no puede ser negativo.")
                continue

            return precio

        except ValueError:
            print("Ingrese un número válido para el precio.")


def registrar_producto(restaurante: Restaurante) -> None:
    print("\n--- Registrar producto ---")

    codigo = input("Código: ").strip()

    if restaurante.buscar_producto(codigo) is not None:
        print("Ya existe un producto con ese código.")
        return

    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()
    precio = leer_precio()

    try:
        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio
        )

        restaurante.registrar_producto(producto)

        print("Producto registrado correctamente.")

    except ValueError as error:
        print(f"Error: {error}")


def buscar_producto(restaurante: Restaurante) -> None:
    print("\n--- Buscar producto ---")

    codigo = input("Código del producto: ").strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
    else:
        print("\nProducto encontrado:")
        print(producto)


def actualizar_producto(restaurante: Restaurante) -> None:
    print("\n--- Actualizar producto ---")

    codigo = input("Código del producto: ").strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
        return

    print(f"Nombre actual: {producto.nombre}")
    print(f"Categoría actual: {producto.categoria}")
    print(f"Precio actual: ${producto.precio:.2f}")

    nuevo_nombre = input("Nuevo nombre: ").strip()
    nueva_categoria = input("Nueva categoría: ").strip()
    nuevo_precio = leer_precio()

    try:
        actualizado = restaurante.actualizar_producto(
            codigo,
            nuevo_nombre,
            nueva_categoria,
            nuevo_precio
        )

        if actualizado:
            print("Producto actualizado correctamente.")
        else:
            print("No fue posible actualizar el producto.")

    except ValueError as error:
        print(f"Error: {error}")


def eliminar_producto(restaurante: Restaurante) -> None:
    print("\n--- Eliminar producto ---")

    codigo = input("Código del producto: ").strip()

    eliminado = restaurante.eliminar_producto(codigo)

    if eliminado:
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")


def listar_productos(restaurante: Restaurante) -> None:
    print("\n--- Lista de productos ---")

    productos = restaurante.listar_productos()

    if not productos:
        print("No existen productos registrados.")
        return

    for producto in productos:
        print(producto)


def registrar_usuario(restaurante: Restaurante) -> None:
    print("\n--- Registrar usuario ---")

    identificacion = input("Identificación: ").strip()

    if restaurante.buscar_usuario(identificacion) is not None:
        print("Ya existe un usuario con esa identificación.")
        return

    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()

    try:
        usuario = Usuario(
            identificacion,
            nombre,
            correo
        )

        restaurante.registrar_usuario(usuario)

        print("Usuario registrado correctamente.")

    except ValueError as error:
        print(f"Error: {error}")


def listar_usuarios(restaurante: Restaurante) -> None:
    print("\n--- Lista de usuarios ---")

    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print("No existen usuarios registrados.")
        return

    for usuario in usuarios:
        print(usuario)


def mostrar_categorias(restaurante: Restaurante) -> None:
    print("\n--- Categorías ---")

    categorias = restaurante.obtener_categorias_unicas()

    if not categorias:
        print("No existen categorías registradas.")
        return

    for categoria in sorted(categorias):
        print(f"- {categoria}")


def salir(restaurante: Restaurante) -> None:
    print("\nGracias por utilizar el sistema de restaurante.")


def ejecutar() -> None:
    restaurante = Restaurante()

    # Diccionario: opción -> función
    opciones = {
        "1": registrar_producto,
        "2": buscar_producto,
        "3": actualizar_producto,
        "4": eliminar_producto,
        "5": listar_productos,
        "6": registrar_usuario,
        "7": listar_usuarios,
        "8": mostrar_categorias,
        "9": salir,
    }

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        accion = opciones.get(opcion)

        if accion is None:
            print("Opción inválida. Seleccione una opción del 1 al 9.")
            continue

        accion(restaurante)

        if opcion == "9":
            break


if __name__ == "__main__":
    ejecutar()

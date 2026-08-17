# restaurante_app - Semana 9

**Estudiante:** Stefany Gallegos Zari

## Descripción del proyecto

Este proyecto corresponde a la actividad de la **Semana 9 de Programación
Orientada a Objetos**.

El sistema `restaurante_app` permite administrar productos y usuarios de un
restaurante mediante una estructura modular. El proyecto utiliza las
estructuras de datos principales de Python: **listas, tuplas, diccionarios y
conjuntos**, asignando a cada una una función concreta dentro del programa.

La aplicación funciona mediante consola y mantiene la separación de
responsabilidades entre los modelos, el servicio y el archivo principal.

## Estructura del proyecto

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
├── main.py
└── README.md

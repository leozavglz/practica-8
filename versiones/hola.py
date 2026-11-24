# hola.py
import sys

version = sys.version_info
print(f"Hola desde Python {version.major}.{version.minor}")

match version.minor:
    case 13:
        print("Versión actual del curso")
    case _:
        print("Otra versión")

# Práctica 8. Lenguajes y sistemas operativos en contenedores

Nombre: Leonardo Zavala González
Número de control: 21130874

Programas y archivos de la práctica 8. No instalé ningún lenguaje en mi computadora: todo se ejecuta con contenedores de Docker.

## Estructura

| Carpeta | Contenido |
|---|---|
| `versiones/` | `hola.py`, el mismo programa ejecutado con Python 3.13, 3.9 y 3.14 |
| `lenguajes/` | `hola.js` (Node.js), `hola.php` (PHP) y `hola.go` (Go), ejecutados con su imagen oficial |
| `imagenes/hola-node/` | Dockerfile propio para el programa de Node.js |
| `imagenes/hola-go/` | Dockerfile propio para el programa de Go |
| `sistemas/` | Comandos usados en las cuatro distribuciones de Linux |

## Cómo ejecutar

Desde la carpeta `versiones/`:

```bash
docker run --rm -v "${PWD}:/app" -w /app python:3.13-slim python hola.py
docker run --rm -v "${PWD}:/app" -w /app python:3.9-slim python hola.py
docker run --rm -v "${PWD}:/app" -w /app python:3.14-slim python hola.py
```

Desde la carpeta `lenguajes/`:

```bash
docker run --rm -v "${PWD}:/app" -w /app node:24-alpine node hola.js
docker run --rm -v "${PWD}:/app" -w /app php:8.4-cli-alpine php hola.php
docker run --rm -v "${PWD}:/app" -w /app golang:1.26-alpine go run hola.go
```

Desde `imagenes/hola-node/` (y lo mismo en `imagenes/hola-go/`, cambiando el nombre):

```bash
docker build -t hola-node .
docker run --rm hola-node
```

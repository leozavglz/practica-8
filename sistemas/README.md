# Cuatro distribuciones de Linux

Cada una se abrió con `docker run -it --rm <imagen> sh`.

| Imagen | Gestor | Comandos para instalar curl |
|---|---|---|
| `ubuntu:24.04` | apt | `apt update` y `apt install -y curl` |
| `debian:trixie` | apt | `apt update` y `apt install -y curl` |
| `alpine:3.22` | apk | `apk update` y `apk add curl` |
| `rockylinux/rockylinux:9` | dnf | `dnf install -y --allowerasing curl` (la imagen ya trae `curl-minimal`) |

En todas se usó `cat /etc/os-release` y `curl -I https://www.djangoproject.com`.

Al salir con `exit` y abrir la imagen otra vez, curl ya no estaba instalado (en Rocky volvió el `curl-minimal` original). Cada `docker run` crea un contenedor nuevo a partir de la imagen sin cambios, y el contenedor anterior, con todo lo que se instaló en él, se borró al salir.

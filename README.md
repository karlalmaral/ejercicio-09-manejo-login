# Ejercicio 09 - Manejo de Login

Simulación local de un login desarrollada en Python para practicar archivos de texto, argumentos y manejo de errores.

> Los usuarios y contraseñas de este proyecto son datos ficticios utilizados únicamente con fines educativos.

## Archivos

- `programa1.py`: recibe usuario y contraseña como argumentos y verifica el login.
- `programa2.py`: lee las contraseñas y las envía como argumentos a `programa1.py`.
- `contraseñas.txt`: contiene las contraseñas ficticias de prueba.

## Ejecución manual

```bash
python3 programa1.py karla holamundo
```

## Ejecución encadenada

```bash
python3 programa2.py karla
```

## Manejo de errores

El programa controla:

- Argumentos faltantes.
- Archivo inexistente.
- Archivo vacío.
- Errores de permisos.
- Errores de ejecución.
- Tiempo de espera agotado.

## Autora

Karla Almaral
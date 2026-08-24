# Importa sys para recibir el nombre del usuario.
import sys

# Importa subprocess para ejecutar programa1.py con argumentos.
import subprocess

# Importa Path para localizar los archivos del proyecto.
from pathlib import Path


# Obtiene la carpeta donde se encuentran los programas.
CARPETA_PROYECTO = Path(__file__).parent

# Construye las rutas de los archivos.
ARCHIVO_CONTRASENAS = CARPETA_PROYECTO / "contraseñas.txt"
PROGRAMA_LOGIN = CARPETA_PROYECTO / "programa1.py"


def leer_contrasenas():
    """Lee las contraseñas almacenadas en el archivo."""

    try:
        with open(
            ARCHIVO_CONTRASENAS,
            "r",
            encoding="utf-8"
        ) as archivo:

            # Elimina líneas vacías y saltos de línea.
            contrasenas = [
                linea.strip()
                for linea in archivo
                if linea.strip()
            ]

        return contrasenas

    except FileNotFoundError:
        print("Error: no existe el archivo contraseñas.txt.")
        return None

    except PermissionError:
        print("Error: no tienes permiso para leer el archivo.")
        return None

    except OSError as error:
        print(f"Error al leer el archivo: {error}")
        return None


def probar_login(usuario, contrasena):
    """Ejecuta programa1.py enviándole usuario y contraseña."""

    try:
        resultado = subprocess.run(
            [
                sys.executable,
                str(PROGRAMA_LOGIN),
                usuario,
                contrasena
            ],
            capture_output=True,
            text=True,
            timeout=5,
            check=False
        )

        # Devuelve el código generado por programa1.py.
        return resultado.returncode

    except subprocess.TimeoutExpired:
        print("Error: el programa de login tardó demasiado.")
        return 2

    except OSError as error:
        print(f"Error al ejecutar programa1.py: {error}")
        return 2


def main():
    """Controla la lectura y prueba de las contraseñas."""

    # Comprueba que se recibió el usuario como argumento.
    if len(sys.argv) != 2:
        print("Uso correcto:")
        print("python3 programa2.py USUARIO")
        return

    # Obtiene el usuario enviado desde la terminal.
    usuario = sys.argv[1]

    # Lee las contraseñas del archivo.
    contrasenas = leer_contrasenas()

    # Detiene el programa si ocurrió un error.
    if contrasenas is None:
        return

    # Comprueba que el archivo no esté vacío.
    if len(contrasenas) == 0:
        print("El archivo no contiene contraseñas.")
        return

    print(f"\nProbando login local para el usuario: {usuario}")

    # Envía cada contraseña como argumento a programa1.py.
    for contrasena in contrasenas:
        print(f"Probando contraseña: {contrasena}")

        codigo = probar_login(usuario, contrasena)

        # El código cero representa un login exitoso.
        if codigo == 0:
            print(f"Login exitoso con la contraseña: {contrasena}")
            return

        # El código dos representa un error del programa.
        if codigo == 2:
            print("No fue posible completar la verificación.")
            return

    # Se muestra si ninguna contraseña funcionó.
    print("Login fallido: ninguna contraseña fue correcta.")


# Inicia el flujo principal.
if __name__ == "__main__":
    main()
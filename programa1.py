# Importa sys para recibir argumentos desde la terminal.
import sys


# Datos locales utilizados únicamente para esta simulación.
USUARIO_CORRECTO = "karla"
CONTRASENA_CORRECTA = "holamundo"


def verificar_login(usuario, contrasena):
    """Comprueba si el usuario y la contraseña son correctos."""

    return (
        usuario == USUARIO_CORRECTO
        and contrasena == CONTRASENA_CORRECTA
    )


def main():
    """Recibe y verifica los argumentos del login."""

    try:
        # El programa necesita el usuario y la contraseña.
        if len(sys.argv) != 3:
            print("Uso correcto:")
            print("python3 programa1.py USUARIO CONTRASEÑA")
            return 2

        # Obtiene los argumentos enviados desde la terminal.
        usuario = sys.argv[1]
        contrasena = sys.argv[2]

        # Comprueba los datos recibidos.
        if verificar_login(usuario, contrasena):
            print("Login exitoso.")
            return 0

        print("Login incorrecto.")
        return 1

    except Exception as error:
        print(f"Error inesperado: {error}")
        return 2


# Ejecuta el programa y devuelve un código de resultado.
if __name__ == "__main__":
    sys.exit(main())
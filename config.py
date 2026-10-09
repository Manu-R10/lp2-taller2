"""
Configuración de la aplicación.

Separar la configuración del código de la aplicación es una buena práctica:
permite tener valores distintos para desarrollo, pruebas y producción sin
tocar la lógica del programa.
"""

import os

# Ruta absoluta a la carpeta raíz del proyecto (donde está run.py).
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Configuración base (desarrollo)."""

    # Clave usada por Flask para firmar cookies/sesiones.
    # TODO 1: 
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-tienda-2026-clave-local")

    # URI de conexión a la base de datos.
    # Para SQLite el formato es: sqlite:///<ruta-absoluta-al-archivo>
    # El archivo .db se creará dentro de la carpeta instance/
    # TODO 2: Verifica que la ruta apunte a instance/tienda.db.
    #         Si cambias el nombre del archivo, actualízalo aquí.
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        BASE_DIR, "instance", "tienda.db"
    )

    # Desactiva un sistema de eventos de SQLAlchemy que no usamos y
    # que consume memoria innecesariamente.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # TODO 3 (opcional): pon esta opción en True para ver en la terminal
    # el SQL que SQLAlchemy genera. Es muy útil para entender qué hace
    # el ORM por debajo. Desactívala cuando ya no la necesites.
    SQLALCHEMY_ECHO = True

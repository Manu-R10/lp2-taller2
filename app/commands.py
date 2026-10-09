
"""
Comandos personalizados de terminal (Flask CLI).

Permiten ejecutar tareas administrativas desde la terminal, por ejemplo:

    flask init-db     -> crea las tablas en la base de datos
    flask seed-db     -> carga los productos del JSON a la base de datos

Estos comandos se registran en create_app().
"""

import json
import os

import click

from .extensions import db
from .models import Categoria, Producto

RUTA_PRODUCTOS = os.path.join(os.path.dirname(__file__), "data", "productos.json")


def registrar_comandos(app):
    """Asocia los comandos a la aplicación Flask recibida."""

    @app.cli.command("init-db")
    def init_db():
        """Crea todas las tablas definidas en models.py."""
        # TODO 1: 
        with app.app_context():
            db.create_all()

        # TODO 2:
        click.echo("Base de datos creada correctamente.")

    @app.cli.command("reset-db")
    def reset_db():
        """Borra y vuelve a crear todas las tablas (¡pierde los datos!)."""
        # TODO 3:
        with app.app_context():
            db.drop_all()
            db.create_all()

        # TODO 4: 
        click.echo("Base de datos reiniciada correctamente.")

    @app.cli.command("seed-db")
    def seed_db():
        """Carga los productos de productos.json en la base de datos."""

        # --- Leer el archivo JSON -------------------------------------
        # TODO 5:
        with open(RUTA_PRODUCTOS, encoding="utf-8") as archivo:
            datos = json.load(archivo)

        # --- Insertar categorías y productos --------------------------
        # Por cada producto del JSON debes:
        #
        # TODO 6: 
        #
        # TODO 7: 
        #
        # TODO 8: 
        #
        # TODO 9: 

        # Contador de productos nuevos que se van a cargar.
        productos_cargados = 0

        with app.app_context():
            for item in datos:
                # TODO 6: 
                categoria = Categoria.query.filter_by(
                    nombre=item["categoria"]
                ).first()

                # TODO 7: 
                if categoria is None:
                    categoria = Categoria(nombre=item["categoria"])
                    db.session.add(categoria)
                    db.session.flush()  # asigna el id sin confirmar aún

                # TODO 8: 
                producto_existente = Producto.query.filter_by(
                    sku=item["sku"]
                ).first()

                if producto_existente:
                    continue

                # TODO 9: 
                producto = Producto(
                    sku=item["sku"],
                    marca=item["marca"],
                    nombre=item["nombre"],
                    precio=item["precio"],
                    foto=item.get("foto"),
                    stock=item.get("stock", 0),
                    activo=item.get("activo", True),
                    categoria_id=categoria.id,
                )

                db.session.add(producto)
                productos_cargados += 1

            # --- Confirmar la transacción ---------------------------------
            # TODO 10:
            db.session.commit()

        # TODO 11: 
        click.echo(
            f"Se cargaron {productos_cargados} productos nuevos correctamente."
        )

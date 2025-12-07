import os
import json
import sys

# --- IMPORTANTE: insertar la ruta ANTES de importar mongo_crud ---
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mongo_crud import *

carpeta_json = r"C:\trabajo final\mongo"

ruta_notas = os.path.join(carpeta_json, "notas_personales.json")
ruta_archivos = os.path.join(carpeta_json, "archivos_adjuntos.json")


# -----------------------------
# Cargar JSON
# -----------------------------
def cargar_json(ruta):
    """Abre un archivo JSON y retorna su contenido."""
    if not os.path.exists(ruta):
        print(f"No se encontró el archivo: {ruta}")
        return None

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error leyendo {ruta}: {e}")
        return None


# -----------------------------
# Seed: Notas
# -----------------------------
def seed_notas():
    """Borra e inserta notas desde el JSON."""
    borrar_notas()  # limpia colección

    datos = cargar_json(ruta_notas)
    if not datos:
        return

    print("\n=== Insertando notas personales ===")
    for nota in datos:
        inserted_id = crear_nota(nota)
        if inserted_id:
            print(f"✓ Nota insertada: {inserted_id}")
        else:
            print("✗ Error al insertar nota")


# -----------------------------
# Seed: Archivos
# -----------------------------
def seed_archivos():
    """Borra e inserta archivos desde el JSON."""
    borrar_archivos()  # limpia colección

    datos = cargar_json(ruta_archivos)
    if not datos:
        return

    print("\n=== Insertando archivos adjuntos ===")
    for archivo in datos:
        inserted_id = crear_archivo(archivo)
        if inserted_id:
            print(f"✓ Archivo insertado: {inserted_id}")
        else:
            print("✗ Error al insertar archivo")


# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    print("=== INICIANDO SEED DE MONGO ===")

    seed_notas()
    seed_archivos()

    print("\n=== SEED COMPLETADO ===")

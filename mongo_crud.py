from db_mongodb import get_db
from funciones_mongo import (
    validar_texto, validar_numero, validar_fecha,
    generar_id, obtener_fecha_actual, manejar_error
)

db, notas, archivos = get_db()

# -----------------------------
# NOTAS PERSONALES
# -----------------------------

@manejar_error
def crear_nota(nota_data):
    """
    Inserta una nota personal en la colección notas_personales.
    Genera un ID si no se proporciona y valida los campos básicos.
    """
    if "id_usuario" not in nota_data:
        raise ValueError("Se requiere id_usuario")
    nota_data["_id"] = nota_data.get("_id", generar_id("nota"))
    nota_data["fecha"] = validar_fecha(
        nota_data.get("fecha", obtener_fecha_actual())
    )
    nota_data["texto"] = validar_texto(nota_data.get("texto", ""))
    return notas.insert_one(nota_data).inserted_id

@manejar_error
def leer_notas(filtro=None):
    filtro = filtro or {}
    return list(notas.find(filtro))

@manejar_error
def actualizar_nota(filtro, nuevos_valores):
    if "texto" in nuevos_valores:
        nuevos_valores["texto"] = validar_texto(nuevos_valores["texto"])
    if "fecha" in nuevos_valores:
        nuevos_valores["fecha"] = validar_fecha(nuevos_valores["fecha"])
    return notas.update_one(filtro, {"$set": nuevos_valores}).modified_count

@manejar_error
def eliminar_nota(filtro):
    return notas.delete_many(filtro).deleted_count

# -----------------------------
# ARCHIVOS ADJUNTOS
# -----------------------------

@manejar_error
def crear_archivo(archivo_data):
    """
    Inserta un archivo adjunto en la colección archivos_adjuntos.
    Genera un ID si no se proporciona y valida campos básicos.
    """
    if "id_usuario" not in archivo_data:
        raise ValueError("Se requiere id_usuario")
    archivo_data["_id"] = archivo_data.get("_id", generar_id("archivo"))
    archivo_data["fecha"] = validar_fecha(
        archivo_data.get("fecha", obtener_fecha_actual())
    )
    archivo_data["ruta_archivo"] = validar_texto(archivo_data.get("ruta_archivo", ""))
    archivo_data["tipo"] = validar_texto(archivo_data.get("tipo", ""))
    return archivos.insert_one(archivo_data).inserted_id

@manejar_error
def leer_archivos(filtro=None):
    filtro = filtro or {}
    return list(archivos.find(filtro))

@manejar_error
def actualizar_archivo(filtro, nuevos_valores):
    for campo in ["ruta_archivo", "tipo"]:
        if campo in nuevos_valores:
            nuevos_valores[campo] = validar_texto(nuevos_valores[campo])
    if "fecha" in nuevos_valores:
        nuevos_valores["fecha"] = validar_fecha(nuevos_valores["fecha"])
    return archivos.update_one(filtro, {"$set": nuevos_valores}).modified_count

@manejar_error
def eliminar_archivo(filtro):
    return archivos.delete_many(filtro).deleted_count
from db_mongodb import get_db
from funciones_mongo import manejar_error
from datetime import datetime, timedelta

# Conexión a MongoDB
db, notas, archivos = get_db()

# ======================================
# ALERTAS Y ANÁLISIS
# ======================================

@manejar_error
def alerta_presion_alta(usuario_id):
    """
    Alerta si el usuario ha tenido presión alta 3 días consecutivos.
    Supone que cada nota puede tener un campo 'mediciones' con 'presion_sistolica'.
    """
    hoy = datetime.now()
    tres_dias = [hoy - timedelta(days=i) for i in range(3)]
    fechas = [d.strftime("%Y-%m-%d") for d in tres_dias]

    notas_usuario = list(notas.find({"id_usuario": usuario_id, "fecha": {"$in": fechas}}))
    
    count_alta = 0
    for nota in notas_usuario:
        mediciones = nota.get("mediciones", {})
        presion = mediciones.get("presion_sistolica", 0)
        if presion >= 130:  # umbral de presión alta
            count_alta += 1

    if count_alta == 3:
        return f"ALERTA: Usuario {usuario_id} tiene presión alta 3 días seguidos."
    return None


@manejar_error
def correlacion_sueno_animo(usuario_id):
    """
    Analiza si a menor horas de sueño corresponde un estado de ánimo bajo.
    Retorna mensaje si detecta patrón.
    """
    notas_usuario = list(notas.find({"id_usuario": usuario_id}))
    patrones = []
    for nota in notas_usuario:
        sueño = nota.get("sueño", None)
        animo = nota.get("estado_animo", None)
        if sueño is not None and animo is not None:
            if sueño < 7 and animo <= 4:  # ejemplo simple
                patrones.append(nota["fecha"])

    if patrones:
        return f"Usuario {usuario_id} muestra ánimo bajo con <7h de sueño en: {', '.join(patrones)}"
    return None


# ======================================
# PRUEBA RÁPIDA
# ======================================
if __name__ == "__main__":
    usuario_demo = "usr_123"
    print(alerta_presion_alta(usuario_demo))
    print(correlacion_sueno_animo(usuario_demo))

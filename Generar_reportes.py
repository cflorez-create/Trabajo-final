# queries_mongo.py
import json
from datetime import datetime
from mongo_crud import leer_notas, leer_archivos

def generar_reporte_usuario(id_usuario, fecha_inicio, fecha_fin, out_path=None, formato="json"):
    """
    Genera un reporte completo de un usuario en un rango de fechas.
    
    Incluye notas, archivos y estadísticas básicas.
    """
    # Convertir strings a datetime
    inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
    
    # Filtrar notas
    notas_usuario = [
        n for n in leer_notas({"id_usuario": id_usuario})
        if fecha_inicio <= n.get("fecha", "") <= fecha_fin
    ]
    
    # Filtrar archivos
    archivos_usuario = [
        a for a in leer_archivos({"id_usuario": id_usuario})
        if fecha_inicio <= a.get("fecha", "") <= fecha_fin
    ]
    
    # Estadísticas simples
    estados = [n.get("estado_animo") for n in notas_usuario if "estado_animo" in n]
    promedio_animo = round(sum(estados)/len(estados),2) if estados else None

    # Preparar reporte
    reporte = {
        "id_usuario": id_usuario,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "num_notas": len(notas_usuario),
        "num_archivos": len(archivos_usuario),
        "promedio_estado_animo": promedio_animo,
        "notas": notas_usuario,
        "archivos": archivos_usuario
    }
    
    # Ruta de salida automática
    if not out_path:
        out_path = f"reporte_{id_usuario}_{fecha_inicio}_a_{fecha_fin}.{formato}"
    
    # Guardar JSON
    if formato.lower() == "json":
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(reporte, f, ensure_ascii=False, indent=2)
    
    # Guardar TXT
    elif formato.lower() == "txt":
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"Reporte de usuario {id_usuario}\n")
            f.write(f"Fechas: {fecha_inicio} a {fecha_fin}\n")
            f.write(f"Numero de notas: {len(notas_usuario)}\n")
            f.write(f"Numero de archivos: {len(archivos_usuario)}\n")
            f.write(f"Promedio estado animo: {promedio_animo}\n\n")
            f.write("Notas:\n")
            for n in notas_usuario:
                f.write(f"Fecha: {n.get('fecha')}\n")
                f.write(f"Texto: {n.get('texto')}\n")
                f.write(f"Estado ánimo: {n.get('estado_animo', 'N/A')}\n")
                f.write("-"*40+"\n")
            f.write("\nArchivos:\n")
            for a in archivos_usuario:
                f.write(f"Fecha: {a.get('fecha')}\n")
                f.write(f"Ruta: {a.get('ruta_archivo')}\n")
                f.write(f"Tipo: {a.get('tipo')}\n")
                f.write(f"Descripción: {a.get('descripcion','')}\n")
                f.write("-"*40+"\n")
    else:
        raise ValueError("Formato debe ser 'json' o 'txt'")

    return out_path


# Ejemplo de uso
if __name__ == "__main__":
    archivo = generar_reporte_usuario("usr_123", "2025-11-01", "2025-11-07")
    print(f"Reporte generado en: {archivo}")

from pymongo import MongoClient

def get_db():
    """
    Conecta a la base de datos FP_Info12025_2 en MongoDB.
    Retorna la base de datos y las colecciones principales.
    """
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["FP_Info12025_2"]
        notas = db["notas_personales"]
        archivos = db["archivos_adjuntos"]
        return db, notas, archivos
    except Exception as e:
        print("Error al conectar a MongoDB:", e)
        return None, None, None
from datetime import datetime
import uuid

# -----------------------------
# VALIDACIONES
# -----------------------------

def validar_texto(texto, max_length=500):
    """
    Valida texto: debe ser string, no vacío y no pasar el límite.
    Retorna el texto limpio.
    """
    if not isinstance(texto, str):
        raise ValueError("El valor debe ser texto")

    texto = texto.strip()

    if not texto:
        raise ValueError("El texto no puede estar vacío")

    if len(texto) > max_length:
        raise ValueError(f"Máximo {max_length} caracteres")

    return texto


def validar_numero(valor, minimo=None, maximo=None):
    """
    Valida números. Comprueba tipo y rango opcional.
    Retorna el número validado.
    """
    if not isinstance(valor, (int, float)):
        raise ValueError("Debe ser numérico")

    if minimo is not None and valor < minimo:
        raise ValueError(f"No puede ser menor que {minimo}")

    if maximo is not None and valor > maximo:
        raise ValueError(f"No puede ser mayor que {maximo}")

    return valor


def validar_fecha(fecha_str, formato="%Y-%m-%d"):
    """
    Convierte string a fecha y valida formato.
    Retorna un objeto datetime.
    """
    try:
        return datetime.strptime(fecha_str, formato)
    except ValueError:
        raise ValueError(f"Formato esperado: {formato}")

# -----------------------------
# AUXILIARES
# -----------------------------

def generar_id(prefijo):
    """
    Genera un ID corto único con prefijo (ej: nota_ab12cd34).
    """
    return f"{prefijo}_{uuid.uuid4().hex[:8]}"


def obtener_fecha_actual(formato="%Y-%m-%d"):
    """
    Retorna la fecha actual como string con formato dado.
    """
    return datetime.now().strftime(formato)

# -----------------------------
# MANEJO DE ERRORES
# -----------------------------

def manejar_error(func):
    """
    Decorador. Captura errores y muestra el mensaje.
    Evita que el programa se detenga.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
            return None
    return wrapper

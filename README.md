# Trabajo-final
Cristian Florez Benitez y Fernando Jaramillo 


Proyecto Final Informática 1 – 2025_2
Sistema de Bitácora Personal de Salud y Bienestar

Objetivo:
Registrar, visualizar y analizar información de salud y estilo de vida.
Datos estructurados en MySQL y datos no estructurados en MongoDB.

Bases de datos:
- MySQL:
  - Administradores, Usuarios, Registros diarios.
  - Usuario: informatica1, Contraseña: info2025_2, Base: FP_Info12025_2
- MongoDB:
  - Notas personales y Archivos adjuntos.

Funcionalidades:
- Login con roles (Administrador / Usuario)
- CRUD de usuarios, registros y archivos
- Registro diario de sueño, actividad, alimentación, síntomas, mediciones
- Registro de notas y archivos con metadatos
- Visualización de tendencias y alertas
- Búsqueda por fecha, palabra clave, tipo, síntomas
- Exportación de reportes en JSON o TXT

Ejecución:
1. Configurar MySQL y cargar script FP_Info12025_2.sql
2. Ejecutar init_db.py para MongoDB
3. Ejecutar mongo_seed.py para precargar datos
4. Ejecutar main.py para iniciar la aplicación
5. Generar reportes con queries_mongo.py

Validaciones y errores:
- Todos los campos validados (texto, número, fecha)
- Manejo de errores con mensajes claros

Documentación:
- Cada función tiene docstring accesible con help()

PD: El código quedó incompleto, pues la parte de mysql que manejaba Fernando, se perdió por un daño en pc, quedó apagado totalmente y no había exportado los archivos, y no nos dió tiempo de reponerlos, entpnces solo pudimos hacer esto. De ante mano, pedimos perdón por la incompetencia. 

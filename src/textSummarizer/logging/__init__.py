import os
import sys
import logging

# Definir el formato de la cadena de registro
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# Definir el nombre del directorio de registro
log_dir = "logs"
# Construir la ruta completa del archivo de registro
log_filepath = os.path.join(log_dir,"running_logs.log")
# Crear el directorio de registro si no existe
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("textSummarizerLogger")


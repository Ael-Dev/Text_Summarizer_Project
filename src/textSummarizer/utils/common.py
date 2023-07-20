import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

# Definir una función para leer un archivo yaml y devolverlo como un objeto ConfigBox
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns
    Args:
        path_to_yaml (str): path like input
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        # Abre el archivo yaml y lo carga como un diccionario
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            # Registra el mensaje de éxito
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            # Devuelve el diccionario como un objeto ConfigBox
            return ConfigBox(content)
    except BoxValueError:
        # Si el diccionario está vacío, lanza un error de valor
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

# Definir una función para crear una lista de directorios
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


# Definir una función para obtener el tamaño en KB de un archivo
@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    Args:
        path (Path): path of the file
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"








# min 1:10:50 https://www.youtube.com/watch?v=p7V4Aa7qEpw&list=PLZoTAELRMXVOjQdyqlCmOtq1nZnSsWvag&index=3
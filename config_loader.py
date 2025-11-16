# config_loader.py
from pathlib import Path
from typing import Any, Dict, Union
from pprint import pprint

import yaml

BASE_DIR = Path(__file__).resolve().parent


def load_yaml_config(path: Union[str, Path]) -> Dict[str, Any]:
    file_path = Path(path)

    if not file_path.is_absolute():
        file_path = BASE_DIR / file_path

    if not file_path.exists():
        raise FileNotFoundError(f"No se encontró el archivo YAML: {file_path}")

    with file_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not isinstance(data, dict):
        raise ValueError("El archivo YAML debe tener un diccionario en la raíz.")

    return data


def print_yaml_config(path: Union[str, Path]) -> None:
    config = load_yaml_config(path)

    print("\n=== Contenido completo del YAML cargado ===")
    pprint(config)

    if "mt" in config:
        print("\n--- Sección 'mt' ---")
        pprint(config["mt"])

    if "inputs" in config:
        print("\n--- Inputs configurados ---")
        for s in config["inputs"]:
            print("  -", repr(s))

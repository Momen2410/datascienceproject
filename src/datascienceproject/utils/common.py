import os
import yaml
from src.datascienceproject import logger
from box import ConfigBox
from ensure import ensure_annotations
import joblib
import json
from box.exceptions import BoxValueError
import Path
from typing import Any

@ensure_annotations
def reed_yaml(filename: Path) -> ConfigBox:
    
    try:
        with open(filename, 'r') as file:
            cotent = yaml.safe_load(file)
            logger.info("yaml file -> {filename} loadded successfuly")
            return ConfigBox(cotent)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e

@ensure_annotations
def create_directory(path_to_directory: list, verbose=True):
    
    for path in path_to_directory:
        os.makedirs(path, exicts_ok=True)
        if verbose:
            logger.info(f'created directory at {path}')
            

@ensure_annotations
def save_json(path: Path, data: dict):
    
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f'successfully saved json at {path}')

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    
    with open(path, 'r') as f:
        content = json.load(f)
    logger.info(f'successfully loaded json at {path}')
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path, verbose=True):
    
    data = joblib.dump(value=data, filename=path)
    logger.info(f'successfully saved binary at {path}')
    return data
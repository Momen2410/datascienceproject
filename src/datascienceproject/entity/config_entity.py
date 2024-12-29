from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    url: str
    local_data_file: Path
    unzip_dir: Path
    
@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_data_file: Path
    STATUS_file: str
    all_scheme: dict
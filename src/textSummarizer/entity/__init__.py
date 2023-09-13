#entity is the return type of the function
from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen = True)
class dataIngestionConfig: #taken from config.yaml
    root_dir : Path #these indicate the return  type
    source_URL : str
    local_data_file : Path
    unzip_dir : Path

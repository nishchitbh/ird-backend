from pathlib import Path
from src.shared.domain.exceptions import ForbiddenException

def safe_join(base_folder: str, filename: str) -> Path:
    base = Path(base_folder).resolve()
    target = (base / filename).resolve()
    if not str(target).startswith(str(base)):
        raise ForbiddenException("Invalid file path.")
    return target

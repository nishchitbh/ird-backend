import os
import threading
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


class Setting:
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    mongodb_host = os.getenv("MONGODB_host")
    auth_secret = os.getenv("AUTH_SECRET")
    access_token_expiry_time = int(os.getenv("ACCESS_TOKEN_EXPIRY_TIME"))
    algorithm = os.getenv("ALGORITHM")
    rel_upload = os.getenv("UPLOAD_FOLDER", "static/uploads")
    upload_folder: Path = (PROJECT_ROOT / rel_upload).resolve()
    allowed_extensions = os.getenv("ALLOWED_EXTENSIONS").split(",")
    chunk_size = int(os.getenv("CHUNK_SIZE", 1048576))
    max_file_size = int(os.getenv("MAX_FILE_SIZE", 10485760))


setting = Setting()


class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        """ Controls the instantiation of the singleton class. """
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

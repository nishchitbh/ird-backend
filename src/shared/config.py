import os
import threading
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


class Setting:
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    mongodb_username = os.getenv("MONGO_INITDB_ROOT_USERNAME")
    mongodb_password = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
    database_name = os.getenv("MONGO_INITDB_DATABASE")

    mongodb_connection = os.getenv("MONGODB_CONNECTION")
    auth_secret = os.getenv("AUTH_SECRET")
    access_token_expiry_time = int(os.getenv("ACCESS_TOKEN_EXPIRY_TIME"))
    algorithm = os.getenv("ALGORITHM")
    raw_upload = os.getenv("UPLOAD_FOLDER", "static/uploads").strip()
    if raw_upload.startswith(os.sep):
        raw_upload = raw_upload.lstrip(os.sep)
    upload_folder: Path = PROJECT_ROOT / raw_upload
    allowed_extensions = os.getenv("ALLOWED_EXTENSIONS").split(",")
    chunk_size = int(os.getenv("CHUNK_SIZE", 1048576))
    max_file_size = int(os.getenv("MAX_FILE_SIZE", 10485760))
    company_domain = os.getenv("COMPANY_DOMAIN")
    redis_host = os.getenv("REDIS_HOST")
    redis_port = os.getenv("REDIS_PORT")
    redis_usernamee = os.getenv("REDIS_USERNAME")
    redis_password = os.getenv("REDIS_PASSWORD")


setting = Setting()


class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        """Controls the instantiation of the singleton class."""
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

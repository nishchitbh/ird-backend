from dotenv import load_dotenv
import os
import threading

load_dotenv()


class Setting:
    mongodb_host = os.getenv("MONGODB_host")
    auth_secret = os.getenv("AUTH_SECRET")
    access_token_expiry_time = int(os.getenv("ACCESS_TOKEN_EXPIRY_TIME"))
    algorithm = os.getenv("ALGORITHM")
    upload_folder = os.getenv("UPLOAD_FOLDER")
    allowed_extensions = os.getenv("ALLOWED_EXTENSIONS").split(",")

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

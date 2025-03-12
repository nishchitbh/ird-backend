from dotenv import load_dotenv
import os
import threading

load_dotenv()


class Setting:
    mongodb_host = os.getenv("MONGODB_host")
    auth_secret = os.getenv("AUTH_SECRET")


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

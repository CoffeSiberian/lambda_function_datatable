from os import environ
from typing import Callable, Any
import pymysql.cursors
from pymysql import Connection

DB_USER = environ.get("DB_USER")
DB_PASS = environ.get("DB_PASS")
DB_HOST = environ.get("DB_HOST")
DB_PORT = int(environ.get("DB_PORT"))
DB_NAME = environ.get("DB_NAME")

def dbConnectionDecorator(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args, **kwargs) -> Connection | str:
        try:
            conexion = pymysql.connect(
                user=DB_USER,
                password=DB_PASS,
                host=DB_HOST,
                port=DB_PORT,
                database=DB_NAME,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            result = func(conexion, *args, **kwargs)
            return result
        except Exception as e:
            return e.__str__()
    return wrapper
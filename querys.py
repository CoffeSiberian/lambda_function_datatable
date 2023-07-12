from pymysql import Connection
from connect import dbConnectionDecorator

@dbConnectionDecorator
def insertData (conexion: Connection, rut: str, nombre: str, apellido: str, celular: int, eva3: float | str = None) -> bool:
    with conexion:
        with conexion.cursor() as cursor:
            try:
                sql = "INSERT INTO datos (rut, nombre, apellido, celular, eva3) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (rut, nombre, apellido, celular, eva3))
                conexion.commit()
                return True
            except:
                return False

@dbConnectionDecorator
def selectData (conexion: Connection) -> list[dict] | None:
    with conexion:
        with conexion.cursor() as cursor:
            try:
                sql = "SELECT * FROM datos"
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
            except:
                return None

@dbConnectionDecorator
def editEva (conexion: Connection, rut: str, eva3: float | None) -> None | int:
    with conexion:
        with conexion.cursor() as cursor:
            try:
                sql = "UPDATE datos SET eva3 = %s WHERE rut = %s"
                cursor.execute(sql, (eva3, rut))
                conexion.commit()
                return cursor.rowcount
            except:
                return None
import sqlite3
from sqlite3 import Error

def createConnection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)

    return conn

def createTables(conn):
    sqls = list()

    sql1 = """CREATE TABLE IF NOT EXISTS Cliente (
                    id_Cliente INTEGER PRIMARY KEY ,
                    name TEXT NOT NULL,
                    last_Name TEXT NOT NULL);"""
    sqls.append(sql1)

    sql2 = """CREATE TABLE IF NOT EXISTS Ingrediente (
                    id_Ingrediente INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    price INTEGER NOT NULL,
                    tamano INTEGER NOT NULL);"""
    sqls.append(sql2)

    sql3 = """CREATE TABLE IF NOT EXISTS Pedido(
                    id_Pedido INTEGER PRIMARY KEY,
                    fk_Cliente INTEGER NOT NULL,
                    pedido_Date TEXT NOT NULL,
                    total_Price INTEGER NOT NULL,
                    FOREIGN KEY (fk_Cliente) REFERENCES Cliente(id_Cliente));"""
    sqls.append(sql3)

    sql4 = """CREATE TABLE IF NOT EXISTS Base(
                    id_Base INTEGER PRIMARY KEY,
                    fk_Pedido INTEGER NOT NULL,
                    tamano TEXT NOT NULL,
                    price INTEGER NOT NULL,
                    FOREIGN KEY (fk_Pedido) REFERENCES Pedido(id_Pedido));"""
    sqls.append(sql4)

    sql5 = """CREATE TABLE IF NOT EXISTS Pizza (
                    id_Pizza INTEGER PRIMARY KEY,
                    fk_Ingrediente INTEGER NOT NULL,
                    fk_Base INTEGER NOT NULL,
                    FOREIGN KEY (fk_Ingrediente) REFERENCES Ingrediente(id_Ingrediente),
                    FOREIGN KEY (fk_Base) REFERENCES Base(id_Base));"""
    sqls.append(sql5)

    cursor = conn.cursor()            
    for sql in sqls:
        cursor.execute(sql)
    cursor.close()

def main():
    database = "database.db"
    conn = createConnection(database)
    with conn:
        createTables(conn)

if __name__ == "__main__":
    main()

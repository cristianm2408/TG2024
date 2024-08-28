import sqlite3 

class Conexion():
    def __init__(self):
       try:
        self.con = sqlite3.connect("redes.db", timeout=10, isolation_level="IMMEDIATE")
        self.creartablas()
       except Exception as ex:
        print(ex)

    def creartablas(self):
        sql_create_table1 = """ CREATE TABLE IF NOT EXISTS usuarios
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        usuario TEXT UNIQUE,
        clave TEXT)"""
        cur = self.con.cursor()
        cur.execute(sql_create_table1)
        cur.close()
        self.crearadmin()

    def crearadmin(self):
      try:
        sql_insert = """ INSERT INTO usuarios values(null,'{}','{}','{}')""".format("Administrador","admin","admin2024")
        cur = self.con.cursor()
        cur.execute(sql_insert)
        self.con.commit()
        cur.close() 
      except Exception as ex: 
         print("Ya se creó el usuario admin",ex)
       


    def conectar(self):
            return self.con
  
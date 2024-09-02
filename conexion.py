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
        # Consulta usando parametrización para evitar inyecciones SQL
            sql_insert = """INSERT OR IGNORE INTO usuarios (nombre, usuario, clave) 
                        VALUES (?, ?, ?)"""
        
        # Establecer los valores del usuario
            admin_values = ("Administrador", "admin", "admin2024")
        
        # Crear cursor y ejecutar la consulta
            cur = self.con.cursor()
            cur.execute(sql_insert, admin_values)
            self.con.commit()  # Confirmar la transacción

        # Verificar si se insertó el usuario o si ya existía
            if cur.rowcount == 0:
               
             print("Ya se creó el usuario admin")
            else:
             print("Usuario admin creado con éxito")
        
            cur.close()  # Cerrar el cursor después de usarlo
        except sqlite3.IntegrityError as e:
          print("Error de integridad en la base de datos:", e)
        except Exception as ex: 
           print("Se produjo un error al crear el usuario admin:", ex)

    def conectar(self):
            return self.con
  
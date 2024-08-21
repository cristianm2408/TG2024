import sqlite3
import conexion as con
from tareas import Tarea
from datetime import datetime

class Tareadata():
  
   def __init__(self) -> None:
          try: 
            self.db = con.Conexion().conectar()
            self.cursor = self.db.cursor()
            sql_create_tareas = """ CREATE TABLE IF NOT EXISTS tareas
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT,
            vlan TEXT,
            tipod TEXT,
            numd NUMERIC,
            tipot TEXT,
            numt NUMERIC,
            detalle TEXT,
            realizado BOOLEAN,
            validacion BOOLEAN,
            fecha DATETIME)"""
            
            self.cursor.execute(sql_create_tareas)
            self.db.commit()
            self.cursor.close()
            self.db.close()

            print("tabla creada")

          except Exception as ex:
            
            print("tabla ok",ex)

           
      
   def regis(self,info:Tarea):
      fecha = datetime.now().strftime("%d/%m/%Y, %H:%M")
      self.db = con.Conexion().conectar()
      self.cursor = self.db.cursor()
      self.cursor.execute("""
      INSERT INTO tareas VALUES(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
      """.format(info._usuario,info._vlan,info._tipod,info._numd,info._tipot,info._ticket,info._detalle,info._realizada,info._validacion,fecha))
      self.db.commit()
      if self.cursor.rowcount ==1:
         return True
      else:
         return False
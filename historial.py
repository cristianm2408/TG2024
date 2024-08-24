import conexion as con
from datetime import datetime
from tareas import Tarea

class Historialdata():

   def basedatos(self, bdesde, bhasta):
      self.db = con.Conexion().conectar()
      self.cursor = self.db.cursor()
      sqlbuscar = """
      SELECT * FROM tareas  
      WHERE fecha>='{}' AND fecha<='{}'
      """.format(bdesde, bhasta)
      res = self.cursor.execute(sqlbuscar)
      data = res.fetchall()
      return data

   def buscarfecha(self, usu, desde, hasta):
      self.db = con.Conexion().conectar()
      self.cursor = self.db.cursor()
      sqlbuscar = """
      SELECT * FROM tareas  
      WHERE usuario='{}' AND fecha>='{}' AND fecha<='{}'
      """.format(usu,desde, hasta)
      res = self.cursor.execute(sqlbuscar)
      data = res.fetchall()
      return data
   
   def buscarfechaf(self, fdesde, fhasta):
      self.db = con.Conexion().conectar()
      self.cursor = self.db.cursor()
      sqlbuscarf = """
      SELECT * FROM tareas  
      WHERE fecha>='{}' AND fecha<='{}'
      """.format(fdesde, fhasta)
      res = self.cursor.execute(sqlbuscarf)
      dataf = res.fetchall()
      return dataf
   
   
   def buscarfechav(self, vlan, vdesde, vhasta):
      self.db = con.Conexion().conectar()
      self.cursor = self.db.cursor()
      sqlbuscarv = """
      SELECT * FROM tareas  
      WHERE vlan='{}' AND fecha>='{}' AND fecha<='{}'
      """.format(vlan,vdesde, vhasta)
      res = self.cursor.execute(sqlbuscarv)
      datav = res.fetchall()
      return datav
   
   
   def tablam(self, tdesde, thasta):
      self.db = con.Conexion().conectar()
      self.cursor = self.db.cursor()
      sqlbuscart = """
      SELECT * FROM tareas  
      WHERE fecha>='{}' AND fecha<='{}'
      """.format(tdesde, thasta)
      res = self.cursor.execute(sqlbuscart)
      datat = res.fetchall()
      return datat
   
    

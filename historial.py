import conexion as con
from datetime import datetime, timedelta
from tareas import Tarea
from PyQt6.QtWidgets import QMessageBox
class Historialdata():



  
   
   def __init__(self, historiale):
        self.historiale = historiale  
        self.db = con.Conexion().conectar() 
        self.cursor = self.db.cursor()
        
   
   def basedatos(self, bdesde, bhasta):
      self.db = con.Conexion().conectar()
      self.cursor = self.db.cursor()
      sqlbuscar = """
      SELECT * FROM tareas  
      WHERE fecha>='{}' AND fecha<='{}'
      ORDER BY fecha DESC
      """.format(bdesde, bhasta)
      res = self.cursor.execute(sqlbuscar)
      data = res.fetchall()
      return data

   def buscarfecha(self, usu, desde, hasta):

      fdia = datetime.strptime(hasta, '%Y/%m/%d')
      fdia += timedelta(days=1)  
      hasta = fdia.strftime('%Y/%m/%d')
   
      self.db = con.Conexion().conectar()
      self.cursor = self.db.cursor()
      sqlbuscar = """
      SELECT * FROM tareas  
      WHERE usuario='{}' AND fecha>='{}' AND fecha<='{}'
      ORDER BY fecha DESC
      """.format(usu,desde, hasta)
      res = self.cursor.execute(sqlbuscar)
      data = res.fetchall()
      return data
   
   def buscarfechaf(self, fdesde, fhasta):

      adia = datetime.strptime(fhasta, '%Y/%m/%d')
      adia += timedelta(days=1)  
      fhasta = adia.strftime('%Y/%m/%d')

      self.db = con.Conexion().conectar()
      self.cursor = self.db.cursor()
      sqlbuscar = """
      SELECT * FROM tareas  
      WHERE fecha>='{}' AND fecha<='{}'
      ORDER BY fecha DESC
      """.format(fdesde, fhasta)
      res = self.cursor.execute(sqlbuscar)
      data = res.fetchall()
      return data
   
   
   def buscarfechav(self, vlan, vdesde, vhasta):
      self.db = con.Conexion().conectar()
      self.cursor = self.db.cursor()
      sqlbuscar = """
      SELECT * FROM tareas  
      WHERE vlan='{}' AND fecha>='{}' AND fecha<='{}'
      ORDER BY fecha DESC
      """.format(vlan, vdesde, vhasta)
      res = self.cursor.execute(sqlbuscar)
      data = res.fetchall()
      return data
   
   def eliminar_tarea_por_ticket(self):
        # Obtener el número de ticket desde el QLineEdit en historiale
        numero_ticket = self.historiale.nticket.text()  # Aquí accedemos correctamente al QLineEdit desde la ventana historiale

        if numero_ticket:
            try:
                # Consulta SQL para eliminar la tarea
                query = "DELETE FROM tareas WHERE numt = ?"
                self.cursor.execute(query, (numero_ticket,))
                self.db.commit()
                

                # Comprobar si se eliminó alguna tarea
                if self.cursor.rowcount > 0:
                    QMessageBox.information(self.historiale, "Éxito", f"Tarea con ticket {numero_ticket} eliminada.")
                    self.historiale.nticket.clear()
                else:
                    QMessageBox.warning(self.historiale, "Error", "No se encontró ninguna tarea con ese número de ticket.")
            except Exception as e:
                QMessageBox.critical(self.historiale, "Error", f"No se pudo eliminar la tarea: {e}")
        else:
            QMessageBox.warning(self.historiale, "Error", "Por favor, ingresa un número de ticket.")
      
      
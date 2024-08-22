class Tarea():
    def __init__(self, usuario:str, vlan:str,   tipot:str,ticket:int, detalle:str,  detalles:str, equipos:str,realizada:bool, validacion:bool):
        self._usuario = usuario
        self._vlan = vlan
        self._equipos = equipos
        self._tipot = tipot
        self._ticket = ticket
        self._detalle = detalle
        self._detalles = detalles
        self._realizada = realizada
        self._validacion = validacion 
        
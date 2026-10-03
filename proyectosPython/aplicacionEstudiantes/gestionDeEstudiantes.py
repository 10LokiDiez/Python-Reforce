import json
class Persona:
    def __init__(self,id,nombre,apellido):
            self.id =id
            self.nombre = nombre
            self.apellido = apellido


class Estudiante(Persona):
    def __init__(self, id,nombre,apellido):
        super().__init__(id,nombre,apellido)
        self.calificaciones = {}

        
    
class Profesor(Persona):
    def __init__(self, id,nombre,apellido):
        super().__init__(id,nombre,apellido)
        self.materiasAsig = []
        
class Materia:
    def __init__(self,id,nombreMateria,profesorAsignado, horario):
        self.id = id
        self.nombreMateria = nombreMateria
        self.profesorAsignado = profesorAsignado
        self.horario = horario
        self.estudiantes = []
        
    
        
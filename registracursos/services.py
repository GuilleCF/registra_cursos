from .models import *

def crear_estudiante(rut, nombre, apellido, fecha_nacimiento):
    estudiante = Estudiante(rut=rut, nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, creado_por='Service')
    estudiante.save()
    return estudiante

def crear_profesor(rut, nombre, apellido):
    profesor = Profesor(rut=rut, nombre=nombre, apellido=apellido, creado_por='Service')
    profesor.save()
    return profesor

def fecha_creacion(calle, numero, dept, comuna, ciudad, region, estudiante):
    if isinstance(estudiante, int):
        estudiante = Estudiante.objects.get(pk=estudiante)
    direccion = Direccion(calle=calle, numero=numero, dept=dept, comuna=comuna, ciudad=ciudad, region=region, estudiante=estudiante)
    direccion.save()
    return direccion

def crear_curso(codigo, nombre, version):
    curso = Curso(codigo=codigo, nombre=nombre, version=version)
    curso.save()
    return curso

def get_profesor(rut):
    return Profesor.objects.get(pk=rut)

def get_curso(codigo):
    return Curso.objects.get(pk=codigo)

def get_estudiante(rut):
    return Estudiante.objects.get(pk=rut)

def crear_registro(estudiante, curso):
    if isinstance(estudiante, int):
        estudiante = Estudiante.objects.get(pk=estudiante)
    if isinstance(curso, int):
        curso = Curso.objects.get(pk=curso)
    registro = Registro(estudiante=estudiante, curso=curso, creado_por='Service')
    registro.save()
    return registro

def asignar_profesor(curso, profesor):
    if isinstance(curso, int):
        curso = Curso.objects.get(pk=curso)
    if isinstance(profesor, int):
        profesor = Profesor.objects.get(pk=profesor)
    curso.profesor = profesor
    curso.save()
    return curso

def informacion_registro(rut):
    estudiante = Estudiante.objects.get(pk=rut)
    registros = Registro.objects.filter(estudiante=estudiante)
    print(f'Cursos inscritos para {estudiante.nombre} {estudiante.apellido}:')
    for registro in registros:
        print(f'{registro.curso}')


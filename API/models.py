from django.db import models


class General(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='imagenes/')
    github = models.URLField(max_length=500)
    linkedin = models.URLField(max_length=500)
    email = models.EmailField(max_length=50)
    curriculum = models.URLField(max_length=500)

    def __str__(self) -> str:
        return self.titulo


class Certificaciones(models.Model):
    titulo = models.CharField(max_length=50)
    institucion = models.CharField(max_length=50)
    descripcion = models.TextField()
    anio = models.CharField(max_length=4)
    categoria = models.CharField(max_length=50)
    certificado = models.URLField(max_length=500)
    icon = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.titulo


class Proyectos(models.Model):
    titulo = models.CharField(max_length=100)
    tecnologias = models.CharField(max_length=200)
    categoria = models.CharField(max_length=50)
    descripcion = models.TextField()
    repositorio = models.URLField(max_length=500)
    view_live = models.URLField(max_length=500, blank=True, null=True)
    iconos = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.titulo
    
class Skills(models.Model):
    titulo = models.CharField(max_length=50)
    icon = models.CharField(max_length=20)
    color = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self) -> str:
        return self.titulo

class SoftSkills(models.Model):
    titulo = models.CharField(max_length=50)
    color = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self) -> str:
        return self.titulo
    

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    asunto = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    mensaje = models.TextField()

    def __str__(self) -> str:
        return self.asunto

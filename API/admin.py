from django.contrib import admin
from .models import General, Certificaciones, Proyectos, Skills, SoftSkills, Contacto, LogEntry


@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'email')
    search_fields = ('titulo', 'subtitulo')
    list_filter = ('email',)


@admin.register(Certificaciones)
class CertificacionesAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'institucion', 'anio', 'categoria')
    search_fields = ('titulo', 'institucion')
    list_filter = ('anio', 'categoria', 'institucion', 'titulo')


@admin.register(Proyectos)
class ProyectosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'repositorio')
    search_fields = ('titulo', 'tecnologias')
    list_filter = ('categoria', 'titulo', 'categoria')


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'icon', 'color')
    search_fields = ('titulo', 'icon')


@admin.register(SoftSkills)
class SoftSkillsAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'color')
    search_fields = ('titulo',)


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'asunto', 'email')
    search_fields = ('nombre', 'apellido', 'asunto')
    list_filter = ('asunto', 'nombre', 'apellido', 'email')


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'level', 'message', 'source')
    search_fields = ('message', 'source')
    list_filter = ('level', 'timestamp')

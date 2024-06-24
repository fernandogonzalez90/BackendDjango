from rest_framework import serializers
from .models import *


class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = General
        fields = '__all__'


class CertificacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificaciones
        fields = '__all__'


class ProyectosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyectos
        fields = '__all__'


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'


class SoftSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftSkills
        fields = '__all__'


class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'

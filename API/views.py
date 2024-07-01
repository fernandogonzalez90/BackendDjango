from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import *
from .serializers import *

#  General
class GeneralCreate(generics.ListCreateAPIView):
    queryset = General.objects.all()
    serializer_class = GeneralSerializer
    permission_classes = [IsAuthenticated]


class GeneralDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = General.objects.all()
    serializer_class = GeneralSerializer


# Certificaciones
class CertificacionesCreate(generics.ListCreateAPIView):
    queryset = Certificaciones.objects.all()
    serializer_class = CertificacionesSerializer
    permission_classes = [IsAuthenticated]


class CertificacionesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificaciones.objects.all()
    serializer_class = CertificacionesSerializer


# Proyectos
class ProyectosCreate(generics.ListCreateAPIView):
    queryset = Proyectos.objects.all()
    serializer_class = ProyectosSerializer
    permission_classes = [IsAuthenticated]


class ProyectosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proyectos.objects.all()
    serializer_class = ProyectosSerializer


# SKills
class SkillsCreate(generics.ListCreateAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = [IsAuthenticated]


class SkillsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer


# Soft Skill
class SoftSkillsCreate(generics.ListCreateAPIView):
    queryset = SoftSkills.objects.all()
    serializer_class = SoftSkillsSerializer
    permission_classes = [IsAuthenticated]


class SoftSkillsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SoftSkills.objects.all()



# Contacto
class ContactoCreate(generics.ListCreateAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer


class ContactoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

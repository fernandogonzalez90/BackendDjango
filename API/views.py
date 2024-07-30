from django.shortcuts import render
from rest_framework import generics

from .TelegramBot import TelegramBot

from .models import *
from .serializers import *
from .permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser

# General


class GeneralCreate(generics.ListCreateAPIView):
    queryset = General.objects.all()
    serializer_class = GeneralSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()


class GeneralDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = General.objects.all()
    serializer_class = GeneralSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = (MultiPartParser, FormParser)

    def perform_update(self, serializer):
        serializer.save()

# Certificaciones


class CertificacionesCreate(generics.ListCreateAPIView):
    queryset = Certificaciones.objects.all()
    serializer_class = CertificacionesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CertificacionesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificaciones.objects.all()
    serializer_class = CertificacionesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Proyectos


class ProyectosCreate(generics.ListCreateAPIView):
    queryset = Proyectos.objects.all()
    serializer_class = ProyectosSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProyectosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proyectos.objects.all()
    serializer_class = ProyectosSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# SKills


class SkillsCreate(generics.ListCreateAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SkillsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Soft Skill


class SoftSkillsCreate(generics.ListCreateAPIView):
    queryset = SoftSkills.objects.all()
    serializer_class = SoftSkillsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SoftSkillsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SoftSkills.objects.all()
    serializer_class = SoftSkillsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Contacto (mantiene la configuración original)


class ContactoCreate(generics.ListCreateAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

    def perform_create(self, serializer):
        contact = serializer.save()
        message = f'Nuevo mensaje de contacto:\nNombre: {contact.nombre}\nEmail: {contact.email}\nAsunto: {contact.asunto}\nMensaje: {contact.mensaje}'
        TelegramBot(message)


class ContactoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

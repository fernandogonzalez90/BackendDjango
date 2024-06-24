from django.urls import path
from .views import *

urlpatterns = [
    # General
    path('general/', GeneralCreate.as_view(), name='general-create'),
    path('general/<int:pk>/', GeneralDetail.as_view(), name='general-detail'),
    # Certificaciones
    path('certificaciones/', CertificacionesCreate.as_view(),
         name='certificaciones-create'),
    path('certificaciones/<int:pk>/', CertificacionesDetail.as_view(),
         name='certificaciones-detal'),
    # Proyectos
    path('proyectos/', ProyectosCreate.as_view(), name='proyectos-create'),
    path('proyectos/<int:pk>/', ProyectosDetail.as_view(), name='proyectos-detail'),
    # Skills
    path('skills/', SkillsCreate.as_view(), name='skills-create'),
    path('skills/<int:pk>/', SkillsDetail.as_view(), name='skills-detail'),
    # SoftSKills
    path('softskills/', SoftSkillsCreate.as_view(), name='softskills-create'),
    path('softskills/<int:pk>/', SoftSkillsDetail.as_view(),
         name='softskills-detail'),
    # Contacto
    path('contacto/', ContactoCreate.as_view(), name='contacto-create'),
    path('contacto/<int:pk>/', ContactoDetail.as_view(), name='contacto-detail')
]

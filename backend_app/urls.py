from .Views.AnnotationView import *
from django.urls import path


urlpatterns = [
    path ('DocumentAnnotations/',annotation_view)
]
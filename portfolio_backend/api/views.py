from django.shortcuts import render
from rest_framework import viewsets
from .models import Experience, Project, Blog
from .serializers import ExperienceSerializer, ProjectSerializer, BlogSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

@api_view(['GET'])
def health_check(request):
    return Response({"status": "healthy"}, status=200)
from rest_framework import serializers
from .models import Experience, Project, Blog

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'  # or specify fields like ['id', 'title', 'company', 'description']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'content', 'date_posted']
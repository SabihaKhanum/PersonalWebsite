from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExperienceViewSet, ProjectViewSet, BlogViewSet, health_check

# Initialize the router
router = DefaultRouter()

# Register your ViewSets
router.register(r'experience', ExperienceViewSet, basename='experience')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'blog', BlogViewSet, basename='blog')

# Define your URL patterns
urlpatterns = [
    # Include the router URLs
    path('', include(router.urls)),
    
    # Health check endpoint
    path('health/', health_check, name='health_check'),
    
    # Include auth URLs for the browsable API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
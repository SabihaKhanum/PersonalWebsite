# from django.contrib import admin
# from django.urls import path, include
# from django.views.generic import TemplateView
# from rest_framework.routers import DefaultRouter
# from api.views import ExperienceViewSet, ProjectViewSet, BlogViewSet

# # Initialize the REST framework's router
# router = DefaultRouter()
# router.register(r'experience', ExperienceViewSet)
# router.register(r'projects', ProjectViewSet)
# router.register(r'blog', BlogViewSet)

# urlpatterns = [
#     # Admin site
#     path('admin/', admin.site.urls),  # Add the admin route

#     # API routes
#     path('api/', include(router.urls)),

#     # Catch-all route for React frontend (serving index.html)
#     path('', TemplateView.as_view(template_name='index.html')),
#     # path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),
# ]
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ExperienceViewSet, ProjectViewSet, BlogViewSet, health_check  # we'll add health_check

# Initialize the REST framework's router
router = DefaultRouter()
router.register(r'experience', ExperienceViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'blog', BlogViewSet)

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Health check endpoint for Render
    path('health/', health_check, name='health_check'),

    # API routes
    path('api/', include(router.urls)),
]
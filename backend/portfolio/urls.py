from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'profile', views.ProfileViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'experiences', views.ExperienceViewSet)
router.register(r'education', views.EducationViewSet)
router.register(r'certifications', views.CertificationViewSet)
router.register(r'contact', views.ContactMessageViewSet)

urlpatterns = [
    path('overview/', views.portfolio_overview, name='portfolio-overview'),
    path('', include(router.urls)),
]

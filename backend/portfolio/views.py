from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Profile, Skill, Project, Experience, Education, Certification, ContactMessage
from .serializers import (
    ProfileSerializer, SkillSerializer, ProjectSerializer,
    ExperienceSerializer, EducationSerializer, CertificationSerializer, ContactMessageSerializer
)


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class EducationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class CertificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer


class ContactMessageViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer


@api_view(['GET'])
def portfolio_overview(request):
    """Single endpoint to fetch all portfolio data at once."""
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    certifications = Certification.objects.all()

    context = {'request': request}
    data = {
        'profile': ProfileSerializer(profile, context=context).data if profile else None,
        'skills': SkillSerializer(skills, many=True, context=context).data,
        'projects': ProjectSerializer(projects, many=True, context=context).data,
        'experiences': ExperienceSerializer(experiences, many=True, context=context).data,
        'education': EducationSerializer(education, many=True, context=context).data,
        'certifications': CertificationSerializer(certifications, many=True, context=context).data,
    }
    return Response(data)

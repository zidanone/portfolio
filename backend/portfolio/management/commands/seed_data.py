import os
from django.core.management.base import BaseCommand
from django.core.files import File
from django.conf import settings
from portfolio.models import Profile, Skill, Project, Experience, Education, Certification


class Command(BaseCommand):
    help = 'Seed the database with sample portfolio data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding customized portfolio data...')

        # ── Profile ──
        profile, _ = Profile.objects.update_or_create(
            email='user@example.com',
            defaults=dict(
                name='Zidane Barkat',
                title='Programming Student & Developer',
                bio=(
                    "I am a programming student and developer focused on Python, web development, "
                    "and cybersecurity fundamentals. I enjoy simplifying complex technical concepts "
                    "and building practical, real-world projects. My goal is to combine technical "
                    "skills with teaching to help others grow in technology."
                ),
                github='https://github.com/username',
                available_for_hire=True,
            ),
        )

        # ── Skills ──
        skills_data = [
            ('Python', '🐍', 90, 'backend', 1),
            ('JavaScript', '📜', 85, 'frontend', 2),
            ('HTML/CSS', '🎨', 85, 'frontend', 3),
            ('React', '⚛️', 80, 'frontend', 4),
            ('Flask', '🧪', 85, 'backend', 5),
            ('SQL', '🗄️', 80, 'backend', 6),
            ('JSON', '📦', 95, 'backend', 7),
            ('Git', '📦', 85, 'tools', 8),
            ('Linux', '🐧', 80, 'tools', 9),
            ('Cybersecurity Fundamentals', '🛡️', 75, 'other', 10),
            ('Practical Learning', '💡', 95, 'other', 11),
            ('Step-by-step Explanation', '🪜', 90, 'other', 12),
            ('Project-based Approach', '🏗️', 95, 'other', 13),
        ]
        
        Skill.objects.all().delete()
        for name, icon, prof, cat, order in skills_data:
            Skill.objects.create(name=name, icon_class=icon, proficiency=prof, category=cat, order=order)

        # ── Projects ──
        projects_data = [
            {
                'title': 'CubeSolve',
                'slug': 'cubesolve',
                'short_description': 'A 3x3 Rubik’s Cube solver with data persistence using JSON.',
                'description': 'CubeSolve focus on algorithmic efficiency and data structure fundamentals.',
                'tech_stack': 'Python, JSON, Data Structures',
                'github_url': 'https://github.com/username/cubesolve',
                'featured': True,
                'order': 1,
                'image_rel_path': 'projects/cub.png'
            },
            {
                'title': 'Social Web App',
                'slug': 'social-web-app',
                'short_description': 'A full-featured social platform with chat, reels, and authentication.',
                'description': 'Demonstrates full-stack proficiency in handling media and real-time sessions.',
                'tech_stack': 'React, Flask, SQL, WebSockets',
                'github_url': 'https://github.com/username/social-app',
                'featured': True,
                'order': 2,
                'image_rel_path': 'projects/social_app_hero.png'
            },
            {
                'title': 'Student Management System',
                'slug': 'student-mgmt-system',
                'short_description': 'Professional management system with an admin dashboard.',
                'description': 'Focuses on SQL database management and professional administrative UI design.',
                'tech_stack': 'Python, Flask, SQL, Bootstrap',
                'github_url': 'https://github.com/username/student-mgmt',
                'featured': True,
                'order': 3,
                'image_rel_path': 'projects/mini-s-m.png'
            },
        ]
        
        Project.objects.all().delete()
        for pdata in projects_data:
            image_path = pdata.pop('image_rel_path')
            project = Project.objects.create(**pdata)
            
            full_image_path = os.path.join(settings.MEDIA_ROOT, image_path)
            if os.path.exists(full_image_path):
                with open(full_image_path, 'rb') as f:
                    project.image.save(os.path.basename(image_path), File(f), save=True)
            else:
                self.stdout.write(self.style.WARNING(f"Project image not found at {full_image_path}"))

        # ── Certifications ──
        certs_data = [
            {
                'title': "CS50x: Introduction to Computer Science",
                'issuer': 'HarvardX / Harvard University',
                'date_issued': '2024-01-01',
                'verification_url': 'https://cs50.harvard.edu/x/',
                'description': 'A comprehensive introduction to computer science and programming.',
                'order': 1,
                'image_rel_path': 'certs/cs50x.png' # Placeholder path
            },
            {
                'title': "CS50p: Introduction to Programming with Python",
                'issuer': 'Harvard University',
                'date_issued': '2025-01-01',
                'verification_url': 'https://cs50.harvard.edu/python/',
                'description': 'Introduction to programming using Python and computational thinking.',
                'order': 2,
                'image_rel_path': 'certs/cs50p.png' # Placeholder path
            },
        ]
        
        Certification.objects.all().delete()
        os.makedirs(os.path.join(settings.MEDIA_ROOT, 'certs'), exist_ok=True)
        
        for cdata in certs_data:
            image_path = cdata.pop('image_rel_path')
            cert = Certification.objects.create(**cdata)
            
            full_image_path = os.path.join(settings.MEDIA_ROOT, image_path)
            if os.path.exists(full_image_path):
                with open(full_image_path, 'rb') as f:
                    cert.image.save(os.path.basename(image_path), File(f), save=True)
            else:
                self.stdout.write(self.style.WARNING(f"Cert image not found at {full_image_path}"))

        # ── Experience / Education ──
        Experience.objects.all().delete()
        Experience.objects.create(
            company='Self-Directed Development',
            role='Independent Developer & Student',
            description='Building real-world projects and simplifying complex concepts.',
            start_date='2023-01-01',
            current=True,
            order=1
        )

        Education.objects.all().delete()
        Education.objects.create(
            institution='Personal Learning',
            degree='Software Development Student',
            field='Computer Science & Cybersecurity',
            start_date='2022-09-01',
            description='Focused on mastering Python, React, Flask, and Cybersecurity.',
            order=1
        )

        self.stdout.write(self.style.SUCCESS(f"Full portfolio data for {profile.name} seeded successfully!"))

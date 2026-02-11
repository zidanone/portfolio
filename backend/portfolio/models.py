from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200, help_text="e.g. Full Stack Developer")
    bio = models.TextField()
    avatar = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume_url = models.URLField(blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    email = models.EmailField()
    location = models.CharField(max_length=100, blank=True)
    available_for_hire = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Profile"


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('tools', 'Tools & DevOps'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=50, blank=True, help_text="CSS icon class or emoji")
    proficiency = models.IntegerField(default=80, help_text="Proficiency level 1-100")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'name']


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    tech_stack = models.CharField(max_length=500, help_text="Comma-separated technologies")
    live_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', '-created_at']


class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)
    company_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.role} at {self.company}"

    class Meta:
        ordering = ['order', '-start_date']


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.degree} in {self.field} — {self.institution}"

    class Meta:
        ordering = ['order', '-start_date']


class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date_issued = models.DateField()
    image = models.ImageField(upload_to='certs/', blank=True, null=True)
    verification_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} by {self.issuer}"

    class Meta:
        ordering = ['order', '-date_issued']


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} — {self.subject}"

    class Meta:
        ordering = ['-created_at']

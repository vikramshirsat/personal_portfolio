from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=120)
    role = models.CharField(max_length=160)
    short_bio = models.TextField()
    detailed_about = models.TextField(help_text="Detailed information about your background.")
    education_summary = models.TextField(blank=True)
    profile_image = models.FileField(upload_to="profile_images/", blank=True, null=True)
    profile_image_url = models.URLField(blank=True)
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=120, blank=True)
    cta_hire_me_url = models.URLField(blank=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    TECHNICAL = "technical"
    SOFT = "soft"
    CATEGORY_CHOICES = [
        (TECHNICAL, "Technical"),
        (SOFT, "Soft"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=TECHNICAL)
    proficiency = models.PositiveSmallIntegerField(default=70, help_text="0-100")
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "name"]

    def __str__(self):
        return f"{self.name} ({self.category})"


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255, help_text="Comma-separated technologies")
    github_link = models.URLField(blank=True)
    live_demo_link = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    sort_order = models.PositiveIntegerField(default=0)
    created_at = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ["sort_order", "-id"]

    def __str__(self):
        return self.title


class TimelineEntry(models.Model):
    EDUCATION = "education"
    EXPERIENCE = "experience"
    TRAINING = "training"
    ENTRY_TYPE_CHOICES = [
        (EDUCATION, "Education"),
        (EXPERIENCE, "Experience"),
        (TRAINING, "Training"),
    ]

    entry_type = models.CharField(max_length=20, choices=ENTRY_TYPE_CHOICES)
    title = models.CharField(max_length=160)
    organization = models.CharField(max_length=160)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "-start_date"]

    def __str__(self):
        return f"{self.title} - {self.organization}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.email})"

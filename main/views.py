from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .forms import ContactForm
from .models import ContactMessage, Profile, Project, Skill, TimelineEntry


@require_http_methods(["GET", "POST"])
def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            saved_message = ContactMessage.objects.create(**data)

            if getattr(settings, "PORTFOLIO_EMAIL_NOTIFICATIONS", False):
                profile = Profile.objects.order_by("-id").first()
                recipients = getattr(settings, "PORTFOLIO_NOTIFICATION_RECIPIENTS", None)
                if not recipients and profile and profile.email:
                    recipients = [profile.email]
                if not recipients:
                    recipients = [getattr(settings, "DEFAULT_FROM_EMAIL", "noreply@example.com")]

                send_mail(
                    subject=f"Portfolio Contact: {saved_message.name}",
                    message=(
                        f"Name: {saved_message.name}\n"
                        f"Email: {saved_message.email}\n\n"
                        f"Message:\n{saved_message.message}"
                    ),
                    from_email=getattr(settings, "DEFAULT_FROM_EMAIL", "noreply@example.com"),
                    recipient_list=recipients,
                    fail_silently=True,
                )

            messages.success(request, "Message sent successfully.")
            return redirect("main:home")
    else:
        form = ContactForm()

    profile = Profile.objects.order_by("-id").first()
    skills = Skill.objects.all()
    technical_skills = skills.filter(category=Skill.TECHNICAL)
    soft_skills = skills.filter(category=Skill.SOFT)
    projects = Project.objects.all()
    timeline_entries = TimelineEntry.objects.all()

    context = {
        "profile": profile,
        "technical_skills": technical_skills,
        "soft_skills": soft_skills,
        "projects": projects,
        "timeline_entries": timeline_entries,
        "form": form,
    }
    return render(request, "main/home.html", context)

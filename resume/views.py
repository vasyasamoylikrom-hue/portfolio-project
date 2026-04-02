from django.shortcuts import render, get_object_or_404
from .models import Profile, Education, Skill

def resume_view(request):
    profile = get_object_or_404(Profile, pk=1)
    context = {
        'profile': profile,
        'experiences': profile.experiences.all(),
        'education': profile.education.all(),
        'skills': profile.skills.all(),
    }
    return render(request, 'resume/resume.html', context)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume_view, name="resume"),
    path('skills/', views.skills_by_category, name="skills"),
    path('api/profiles/', views.ProfileListAPI.as_view(), name='api-profiles'),
    path('api/profiles/<int:pk>', views.ProfileDetailApi.as_view(), name='api-profile-detail')
]
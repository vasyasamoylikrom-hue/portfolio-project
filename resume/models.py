from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    github = models.URLField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Experience(models.Model):
    '''
    on_delete=POTECT -> Запрещаем удаление профиля
    on_delete=SET_NULL -> При удалении профиля, значение в NULL
    on_delete=SET_DEFAULT -> Ставится значение по умолчанию
    on_delete=CASCADE -> Опыт тоже будет удалятся
    '''
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="experiences")
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=150)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    is_current = models.BooleanField(default=False)

    class Meta:
        ordering = ['-start_date'] # Cортирвока по умолчанию

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="education")
    university = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    start_year = models.DateField()
    end_year = models.DateField(blank=True)

    class Meta:
        ordering = ["-start_year"]

    def __str__(self):
        return f"{self.degree} - {self.university}"

class Skill(models.Model):
    LEVEL_CHOICES = [
    # запись в бд
    #               запись в админке (как видит пользователь)
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]

    CATEGORY_CHOICES = [
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('devops', 'Devops'),
        ('other', 'Other'),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')

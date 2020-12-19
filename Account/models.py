from django.db import models
from django.contrib.auth.models import User

class ProfileManager(models.Manager):
    def get_student(self):
        users = super().get_queryset()
        students = []
        for user in users:
            if (user.is_student()):
                students.append(user)
        return students

    def get_username(self):
        users = super().get_queryset()
        logins = []
        for user in users:
            if (user.is_student()):
                logins.append(user.user.username)
        return logins

class StudentGroup(models.Model):
    number = models.CharField(max_length=10, null=False, verbose_name='Номер')
    bio = models.TextField(max_length=500, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name_plural = 'Группы'
        verbose_name = 'Группа'

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL, verbose_name='Пользователь')
    first_name = models.CharField(max_length=20,null=True, verbose_name='Имя')
    middle_name = models.CharField(max_length=20,null=True, verbose_name='Отчество')
    last_name = models.CharField(max_length=20,null=True, verbose_name='Фамилия')

    objects = ProfileManager()

    bio = models.TextField(max_length=500, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.user.username

    def is_student(self):
        return (self.user.groups.filter(name='student').exists())
    
    def is_teacher(self):
        return (self.user.groups.filter(name='teacher').exists())
    
    def groupExists(self):
        return self.user.groups.exists()

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователи'

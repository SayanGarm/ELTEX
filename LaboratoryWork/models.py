from django.db import models
from django.contrib.auth.models import User

class ArticleManager(models.Manager):
    def getAllFromRole(self, user):
        groups = user.groups
        if (groups.filter(name = 'teacher').exists()):
            return self.all()
        if (groups.filter(name = 'student').exists()):
            return self.filter(author=user)

class LaboratoryWork(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    document = models.FileField(verbose_name='Документ')
    author = models.ForeignKey(User, null=True, on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Лабораторные работы'
        verbose_name = 'Лабораторная работа'


STATUS = ( ('A', 'Проверен'),
        ('B', 'Требует исправлений'),
        ('C', 'Ожидает проверки') )

class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    author = models.ForeignKey(User, null=True, on_delete=models.PROTECT, verbose_name='Автор')

    document = models.FileField(verbose_name='Документ')

    status = models.CharField(max_length=20, default='C', choices=STATUS, verbose_name='Статус')

    objects = ArticleManager()
    
    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.document.delete(save=False)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Отчеты'
        verbose_name = 'Отчет'
        ordering = ['-published']

class Review(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='Автор')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Отчет')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    content = models.TextField(null=True, blank=True, verbose_name='Текст ответа')

    status = models.CharField(max_length=20, default='C', choices=STATUS, verbose_name='Статус')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Ответы'
        verbose_name = 'Ответ'
        ordering = ['-published']

class LaboratoryStand(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    key = models.CharField(max_length=50, verbose_name='Ключ')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Лабораторные стенды'
        verbose_name = 'Лабораторный стенд'
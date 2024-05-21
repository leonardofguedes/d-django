from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    mail = models.EmailField(unique=True, null=True, blank=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(User, related_name='projetos')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projetos_criados', null=True, blank=True)
    def __str__(self):
        return self.name

class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Task(models.Model):
    class StatusChoices(models.TextChoices):
        PENDENTE = 'Pending', 'Pendente'
        EM_ANDAMENTO = 'In Progress', 'Em andamento'
        CONCLUIDA = 'Completed', 'Concluída'

    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.PENDENTE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    tags = models.ManyToManyField(Tag, related_name='tasks')

    def __str__(self):
        return self.title



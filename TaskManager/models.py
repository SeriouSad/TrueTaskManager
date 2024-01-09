from django.db import models
from django.contrib.auth.models import User, Group


class TaskGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    name = models.CharField(max_length=255, verbose_name="Название группы задач")

    def __str__(self):
        return self.name


class Task(models.Model):
    group = models.ForeignKey(TaskGroup, on_delete=models.CASCADE, verbose_name="Группа задач")
    name = models.CharField(max_length=255, verbose_name="Заголовок задачи")
    text = models.TextField(verbose_name="Текст задачи")
    deadline_date = models.DateTimeField(verbose_name="Дата дедлайна")
    finished = models.BooleanField(verbose_name="Завершена?", default=False)

    def __str__(self):
        return self.name



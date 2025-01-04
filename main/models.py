from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    text = models.CharField('Название', max_length=150)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')


    def __str__(self): # класс для отображения текста а не имен переменных
        return self.text


    def get_absolute_url(self):
        return f'/update/{self.id}/'


    class Meta: # для коректонного названия таблицы в админ панеле
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
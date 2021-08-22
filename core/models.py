from django.db import models


class Students(models.Model):
    name = models.CharField('Имя', max_length=255)
    group = models.IntegerField('Номер группы', null=True, blank=True)

def __str__(self):
    return self.name
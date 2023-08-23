from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    ddescription = models.CharField(max_length=255, default='Default Description')


    def __str__(self):
        return self.name

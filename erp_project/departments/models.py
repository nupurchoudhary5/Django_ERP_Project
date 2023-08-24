from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    ddescription = models.CharField(max_length=255, default='Default Description')


    def __str__(self):
        return self.name


class StudentResult(models.Model):
    student_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.student_name} - {self.subject}"

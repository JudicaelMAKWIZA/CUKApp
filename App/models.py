from django.db import models

class Patient(models.Model):

    Sexe = (
        ('F', 'F'),
        ('M', 'M'),
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    prename = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    sexe = models.CharField(max_length=100, null=True, choices=Sexe)
    note = models.TextField()
    cree_nouveau = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
specials = (
    ('Allgemeinarzt','Allgemeinarzt'),
    ('Radiologe', 'Radiologe'),
    ('Uruloge','Uruloge'),
    ('Psychater','Psychater'),
    ('Kinderarzt','Kinderarzt'),
)

title_options = (
    ('Dr.','Dr.'),
    ('Prof.', 'Prof.'),
    ('Prof. Dr.','Prof. Dr.'),
    
)
class Doctor(models.Model):

    speciality = models.CharField(max_length=128, choices=specials)
    title = models.CharField(max_length=64, choices=title_options)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} {1}'.format(self.title,self.name)

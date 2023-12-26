from django.contrib.auth.models import AbstractUser
from django.db import models
#ilki bn model doretyas
# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True) # egerde True-ni False etsek yashyny hokmany girizmeli bolyar
    address = models.CharField(max_length=140)
    #modele girizen zatlarmyzy forms.py bn baglanyshdyryas
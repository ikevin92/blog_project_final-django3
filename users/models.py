from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)

    # email como propiedad principal (primero debemos crear el superuser)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

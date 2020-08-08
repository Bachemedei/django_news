from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    #this is where I'd add other fields, e.g profile pic, bio
    pass

    def __str__(self):
        return self.username
    
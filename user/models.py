from django.db import models
from django.contrib.auth.hashers import make_password


class User(models.Model):
    class Meta:
        db_table = "user"

    email = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)

    def get_username(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

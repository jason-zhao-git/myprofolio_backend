from django.db import models
from django.core.validators import MaxLengthValidator

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(validators=[MaxLengthValidator(2000)])
    show_on_guestbook = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"
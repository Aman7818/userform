from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class UserForm(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def clean(self):
        super().clean()
        age = (timezone.now().date() - self.dob).days // 365
        if age < 18:
            raise ValidationError('Age must be at least 18 years')

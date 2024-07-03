from django.db import models

class RequestCall(models.Model):
    phone_number = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number

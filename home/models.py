from django.db import models

# Create your models here.
class Contact_us(models.Model):

    sender_name=models.CharField(max_length=100)
    from_email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.from_email
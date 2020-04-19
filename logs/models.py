import sys
from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class User(AbstractUser):
    phone = PhoneField(blank=True, help_text='User phone number')

    def __str__(self):
        return self.username

class Vehicle(models.Model):
    model_year = models.TextField()
    make = models.TextField()
    model = models.TextField()
    trim = models.TextField(blank=True)
    color = models.TextField(blank=True)
    vin = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return f'{self.model_year} {self.make} {self.model}'

class Log(models.Model):
    entry_date = models.DateTimeField(auto_now_add=True)
    date = models.DateField() #default format for Django yyyy-mm-dd
    shop = models.TextField()
    receipts = models.TextField(blank=True)
    repair_name = models.TextField()
    cost = models.TextField()
    description = models.TextField()
    image_url = models.ImageField(upload_to='images/', blank=False, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicles')

    def __str__(self):
        return f'{self.entry_date}'
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.image_url = self.compressImage(self.image_url)
        super(Log, self).save(*args, **kwargs)

    def compressImage(self, image_url):
        imageTemproary = Image.open(image_url)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize( (300,300) ) 
        imageTemproary.save(outputIoStream , format='JPEG', quality=20)
        outputIoStream.seek(0)
        image_url = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % image_url.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return image_url
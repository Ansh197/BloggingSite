from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolioSite = models.URLField(blank=True)
    profilePic = models.ImageField(upload_to='profilePics',blank=True)
    def __str__(self):
        return self.user.username
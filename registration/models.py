from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from PIL import Image

'''
это как бы отдельная модель для создания пользователя, тоесть все будем выводить из нее, а не из стандартной
'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
    def get_absolute_url(self):
        return reverse('Profile', kwargs={'pk': self.pk})
            
    class Meta:
        verbose_name = 'Аккаунты'
        verbose_name_plural = 'Аккаунты'
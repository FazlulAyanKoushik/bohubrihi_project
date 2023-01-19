from django.db import models
from django.conf import settings

# Image upload function
def upload_image(instance, filename):
    return "uploads/{user}/{filename}".format(user=instance.user, filename=filename)

# Create your models here.
class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_image, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.content)[0:30]
    
    class Meta:
        verbose_name_plural = "Status List"
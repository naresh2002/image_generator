from django.db import models

class GeneratedImage(models.Model):
    text_input = models.CharField(max_length=255)
    image = models.ImageField(upload_to='generated_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text_input

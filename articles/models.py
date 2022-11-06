from django.db import models
from django.utils import timezone
import os
from PIL import Image


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
article_image_dir = base_dir + '\media\\article_pics'

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    picture = models.ImageField(blank=True, upload_to=article_image_dir)

    def __str__(self):
        return f'{self.title}'

    def save(self):
        super().save()
        try:
            img = Image.open(self.picture.path)
            if img.height > 720 or img.width > 1360:
                output_size = (1360, 720)
                img.thumbnail(output_size)
                img.save(self.picture.path)
        except ValueError:
            pass
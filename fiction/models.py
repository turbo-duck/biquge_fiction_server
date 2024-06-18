from django.db import models


# Create your models here.
class FictionList(models.Model):
    fiction_code = models.CharField(max_length=100)
    fiction_name = models.CharField(max_length=200)
    fiction_info = models.CharField(max_length=200)
    fiction_introduce = models.CharField(max_length=500)
    fiction_author = models.CharField(max_length=100)
    fiction_type = models.CharField(max_length=100)
    fiction_image_url = models.CharField(max_length=200)
    fiction_count = models.CharField(max_length=100)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()


class ChapterList(models.Model):
    fiction_code = models.CharField(max_length=100)
    chapter_code = models.CharField(max_length=100)
    chapter_name = models.CharField(max_length=200)
    chapter_order = models.CharField(max_length=100)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

from django.db import models


# Create your models here.
class FictionList(models.Model):
    fiction_code = models.TextField()
    fiction_name = models.TextField()
    fiction_info = models.TextField()
    fiction_introduce = models.TextField()
    fiction_author = models.TextField()
    fiction_type = models.TextField()
    fiction_image_url = models.TextField()
    fiction_count = models.TextField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()


class ChapterList(models.Model):
    fiction_code = models.TextField()
    chapter_code = models.TextField()
    chapter_name = models.TextField()
    chapter_order = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()


class ChapterDetailList(models.Model):
    chapter_code = models.TextField()
    chapter_content = models.TextField()


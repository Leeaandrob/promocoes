from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    main_image = models.ImageField(upload_to='dogs/')
    image_cover = models.ImageField(upload_to='dogs/')
    sold = models.BooleanField()


class PostImageGalery(models.Model):
    title = models.CharField(max_length=255)
    post = models.ForeignKey('Post', related_name='galery')
    image = models.ImageField(upload_to="dogs/")

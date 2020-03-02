from django.db import models
from django.urls import reverse

# Django commands uptil now
# python ./manage.py runserver
# django-admin startapp Blog
# python ./manage.py migrate
# ./manage.py makemigrations
# python ./manage.py createsuperuser

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    summary = models.CharField(max_length=300)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='img')

    class Meta:
        ordering = ['-created']

        def __unicode__(self):
            return u'%s'% self.title

    def get_absolute_url(self):
        return reverse('Blog.views.post', args=[self.slug])
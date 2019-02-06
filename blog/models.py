from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# making a post model that inherits from django's model class

class Post(models.Model):
    title = models.CharField(max_length=100)
    #CharField indicates its a character field with max length 100
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #auto_now updates whenever we update it. auto_now_add keeps permanently current date as date posted. default is from timezone import
    # we need to import the user model for our authors
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if the user created a post and we need to get rid of the post, on_delete will delete the post if user is deleted
    #vv this is dunders
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

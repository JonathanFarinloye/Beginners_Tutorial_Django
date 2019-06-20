from django.db import models
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50)
    raw_date = models.DateTimeField()
    cover = models.ImageField(upload_to='images/')
    content = models.TextField()
    slug = models.SlugField()
    
    def date(self):
        return self.raw_date.strftime('%b %d %Y')
    
    def __str__(self):
        return self.title
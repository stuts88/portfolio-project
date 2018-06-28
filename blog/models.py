from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]

    def pub_date_nice(self):
        return self.pub_date.strftime('%A, %e %b %Y')

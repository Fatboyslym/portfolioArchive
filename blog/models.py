from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        words = str(self.body).split(" ")
        words = words[:20]
        return " ".join(words)

    def pub_datef(self):
        return self.pub_date.strftime('%b %d, %Y')

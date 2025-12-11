from django.db import models

# Create your models here.

CATEGORY = (("django","Django"),("html","HTML"),("css","CSS"))

class Portfolio(models.Model):
  title = models.CharField(max_length=100)
  image = models.ImageField()
  text = models.TextField(max_length=300)
  category = models.CharField(
    max_length=100,
    choices=CATEGORY
  )

  def __str__(self):
    return self.title


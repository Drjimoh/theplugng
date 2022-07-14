from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField()
	image = models.ImageField(upload_to="img", null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)


	class Meta:
		ordering =['-date_added']
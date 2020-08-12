from django.db import models

# Create your models here.

Alpha=(
('Full Time','full time'),('Part Time','part time')
)

class blog (models.Model):
	
	title=models.CharField(max_length=100)
	
	Type=models.CharField(max_length=15,choices=Alpha)
	
	comment=models.TextField(max_length=1000)
	
	choose=models.IntegerField(default=1)
	
	last_edit=models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.title

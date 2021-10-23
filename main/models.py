from django.db import models

# Create your models here.
# creating database tables and it attributes
class Award(models.Model):
    name=models.CharField(max_length=300)
    description=models.TextField(max_length=5000)     
    developer=models.CharField(max_length=300)
    created_date=models.DateField()
    averangeRating=models.FloatField(default=0)
    image=models.URLField(default=None, null=True)
    linktosite=models.URLField(default=None, null=True)
   


    def __str__(self):
        return self.name
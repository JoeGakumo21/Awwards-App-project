from django.db import models

# Create your models here.
# creating database tables and it attributes
class Award(models.Model):
    name=models.CharField(max_length=300)
    description=models.TextField(max_length=5000)
    created_date=models.DateField()
    averangeRating=models.FloatField()
    developer=models.CharField(max_length=300)


    def __str__(self):
        return self.name
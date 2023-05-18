from django.db import models

# Create your models here.
#Run these two files whenever there is a change in models.py
#python3 manage.py makemigations
#python3 manage.py migrate

#To view python shell
#Run python3 manage.py shell

class Products(models.Model):
    Title = models.CharField(max_length=120)
    Content = models.TextField(blank=True,null=True)
    Price = models.DecimalField(decimal_places=2,max_digits=15,default=0.00)
    def __str__(self) -> str:
        return self.Title
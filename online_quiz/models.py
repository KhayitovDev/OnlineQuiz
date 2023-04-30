from django.db import models
from django.core.validators import MinValueValidator


class User(models.Model):
    first_name=models.CharField(max_length=255, null=False, blank=False)
    last_name=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.first_name
    
    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'
        
class Category(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(null=True, blank=True)
    number_of_quizes=models.PositiveBigIntegerField(validators=[MinValueValidator(1)])

    def __str__(self) -> str:
        return self.title
    


    






    


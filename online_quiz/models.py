from django.db import models


class User(models.Model):
    first_name=models.CharField(max_length=255, null=False, blank=False)
    last_name=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.first_name
    
    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'

    


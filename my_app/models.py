from django.db import models



class UserModel(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    number = models.IntegerField(default=99)
    create_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name} {self.number}'
   
   
    class Meta:
        db_table='user'
        managed= True
        verbose_name='foydalavchi'
        verbose_name_plural='ModelNames'

from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name= 'nomi')
    logo = models.ImageField(upload_to= 'brand/photo/', blank=True, null=True)
    information = models.TextField(verbose_name="ma'lumot")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='nomi')
    type = models.CharField(max_length=25, verbose_name='turi')
    information = models.TextField()
    photo = models.ImageField(upload_to='car/photo/', blank=True, null=True)
    release_date = models.DateTimeField(verbose_name='Chiqarilgan sana', auto_now=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sana")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
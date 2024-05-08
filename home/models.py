from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_ROLES = [
        ('sotuvchi', 'Sotuvchi'),
        ('admin', 'Admin'),
        ('boshliq', 'Boshliq')
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=255, choices=USER_ROLES)
    rating = models.FloatField()
    phone_nomber = models.CharField(max_length=20, blank=True)
    
    class Meta:
        db_table = 'userprofile'

    def __str__(self) -> str:
        return self.user.get_full_name()
    
class Income(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    real_price = models.FloatField()
    time = models.DateField(auto_now=True)
    p_amount = models.IntegerField(default=1)

    class Meta:
        db_table = 'income'

    def __str__(self) -> str:
        return str(self.product)



class Category(models.Model):
    category = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'

    def __str__(self) -> str:
        return self.category
    

class Product(models.Model):
    TYPE = (
        ('dona','Dona'),
        ('metr','Metr'),
    )
    category = models.ForeignKey(Category, verbose_name="Kategoriya", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Nomi")
    type = models.CharField(max_length=255, choices=TYPE, verbose_name="Birlik")
    amount = models.IntegerField(verbose_name="Soni")
    summa = models.IntegerField(verbose_name="Narxi Sum")
    dollor = models.FloatField(verbose_name="Narxi $")
    class Meta:
        db_table = 'product'

    def __str__(self) -> str:
        return f"{self.name}---${self.dollor}"


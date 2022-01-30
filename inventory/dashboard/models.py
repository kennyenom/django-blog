from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

# Create your models here.

CATEGORY =(
    ('Stationary','Stationary'),
    ('Electronics','Electronics'),
    ('Food','Food'),
)
class Product(models.Model):
    name = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=100,choices=CATEGORY,null=True)
    quantity = models.PositiveIntegerField(default=1,null=True)


    def __str__(self):
        return f"{self.name}"

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    staff = models.ForeignKey(User,models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Order'


    def __str__(self):
        return f"{self.product} ordered by {self.staff.username}"





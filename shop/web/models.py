from django.db import models

# Create your models here.
class Product(models.Model):
    reference = models.CharField(max_length=10)
    title = models.CharField(max_length=256)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.IntegerField()
    offer = models.BooleanField()
    stock = models.BooleanField()
    img = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.title

class Client(models.Model):
    dni = models.CharField(max_length=10)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    premium = models.BooleanField()

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return str(self.id)

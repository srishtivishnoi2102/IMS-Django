from django.db import models

# Create your models here.


class Inventory(models.Model):
    name = models.CharField(max_length=100, blank=False)
    quantity = models.CharField(max_length=50, default=1)
    price = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        abstract= True

    def __str__(self):
        return 'Name : {0}, Quantity : {1}, Price : {2}, Count : {3}'.format(self.name, self.quantity, self.price, self.count)


class VegetableFruit(Inventory):
    pass

class GroceryStaple(Inventory):
    pass

class HouseholdItem(Inventory):
    pass

class PersonalCare(Inventory):
    pass

class SnacksBeverage(Inventory):
    pass

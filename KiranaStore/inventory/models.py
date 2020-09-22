from django.db import models

# Create your models here.


class Inventory(models.Model):
    type = models.CharField(max_length=100, blank=False)
    quantity = models.CharField(max_length=100)
    price = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        abstract= True

    def __str__(self):
        return 'Type : {0} Price : {1}'.format(self.type, self.price)


class VegetableFruits(Inventory):
    pass

class GroceryStaples(Inventory):
    pass

class HouseholdItems(Inventory):
    pass

class PersonalCare(Inventory):
    pass

class SnacksBeverages(Inventory):
    pass

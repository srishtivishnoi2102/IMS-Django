from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^$', index, name='index'),

    url(r'^household-item$', display_HouseholdItem, name='display_HouseholdItem'),
    url(r'^add-household-items$', addHouseholdItem, name='addHouseholdItem'),
    url(r'^edit-household-items/(?P<pk>\d+)$', editHouseholdItem, name='editHouseholdItem'),
    url(r'^delete-household-items/(?P<pk>\d+)$', deleteHouseholdItem, name='deleteHouseholdItem'),
    

    url(r'^vegetable-fruit$', display_VegetableFruit, name='display_VegetableFruit'),
    url(r'^add-vegetable-fruit$', addVegetableFruit, name='addVegetableFruit'),
    url(r'^edit-vegetable-fruit/(?P<pk>\d+)$', editVegetableFruit, name='editVegetableFruit'),
    url(r'^delete-vegetable-fruit/(?P<pk>\d+)$', deleteVegetableFruit, name='deleteVegetableFruit'),

    url(r'^grocery-staple$', display_GroceryStaple, name='display_GroceryStaple'),
    url(r'^add-grocery-staple$', addGroceryStaple, name='addGroceryStaple'),
    url(r'^edit-grocery-staple/(?P<pk>\d+)$', editGroceryStaple, name='editGroceryStaple'),
    url(r'^delete-grocery-staple/(?P<pk>\d+)$', deleteGroceryStaple, name='deleteGroceryStaple'),

    url(r'^snack-beverage$', display_SnacksBeverage, name='display_SnacksBeverage'),
    url(r'^add-snack-beverage$', addSnacksBeverage, name='addSnacksBeverage'),
    url(r'^edit-snack-beverage/(?P<pk>\d+)$', editSnacksBeverage, name='editSnacksBeverage'),
    url(r'^delete-snack-beverage/(?P<pk>\d+)$', deleteSnacksBeverage, name='deleteSnacksBeverage'),

    url(r'^personal-care$', display_PersonalCare, name='display_PersonalCare'),
    url(r'^add-personal-care$', addPersonalCare, name='addPersonalCare'),
    url(r'^edit-personal-care/(?P<pk>\d+)$', editPersonalCare, name='editPersonalCare'),
    url(r'^delete-personal-care/(?P<pk>\d+)$', deletePersonalCare, name='deletePersonalCare'),


    

]

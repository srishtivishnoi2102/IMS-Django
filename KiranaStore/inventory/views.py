from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# current Headings

VegetableFruitHeading = 'Vegetable & Fruits'
GroceryStapleHeading = 'Grocery & Staples'
PersonalCareHeading =  'Personal Care Items'
SnacksBeverageHeading = 'Snack & Beverages'
HouseholdItemHeading = 'Household Items'


# Create your views here.
def index(request):
    return render(request, 'index.html')

# Base Methods
def displayInventory(request, modelObj, currentHeading):
    items = modelObj.objects.all()
    context = {
        'items' : items,
        'currentHeading': currentHeading
    }
    return render(request, 'index.html', context)

def addInventory(request, modelObj, formClass, currentHeading):
    if request.method == 'POST':
        form = formClass(request.POST)
        if form.is_valid():
            form.save()
            return displayInventory(request, modelObj, currentHeading)
            return redirect('index')


    else:
        form = formClass()
        return render(request, 'add_new.html', {'form': form, 'currentHeading':currentHeading})

def editInventory(request, pk , modelObj, formClass, currentHeading):
    item = get_object_or_404(modelObj, pk=pk)

    if request.method =="POST":
        form = formClass(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return displayInventory(request, modelObj, currentHeading)
            # return redirect('index')

    else:
        form = formClass(instance = item)
        return render(request, 'edit_item.html', {'form': form, 'currentHeading':currentHeading})


# Methods to display diff inventory
def display_VegetableFruit(request):
    return displayInventory(request, VegetableFruit, VegetableFruitHeading )

def display_GroceryStaple(request):
    return displayInventory(request, GroceryStaple, GroceryStapleHeading )
    
def display_PersonalCare(request):
    return displayInventory(request, PersonalCare, PersonalCareHeading )
     
def display_SnacksBeverage(request):
    return displayInventory(request, SnacksBeverage, SnacksBeverageHeading )

def display_HouseholdItem(request):
    return displayInventory(request, HouseholdItem, HouseholdItemHeading )


# method for adding inventory
def addVegetableFruit(request):
    return addInventory(request , VegetableFruit, VegetableFruitForm,VegetableFruitHeading )

def addGroceryStaple(request):
    return addInventory(request , GroceryStaple, GroceryStapleForm, GroceryStapleHeading)

def addPersonalCare(request):
    return addInventory(request , PersonalCare, PersonalCareForm, PersonalCareHeading)

def addSnacksBeverage(request):
    return addInventory(request , SnacksBeverage , SnacksBeverageForm, SnacksBeverageHeading)

def addHouseholdItem(request):
    return addInventory(request , HouseholdItem, HouseholdItemForm,HouseholdItemHeading)


# for editing inventory
def editVegetableFruit(request, pk):
    return editInventory(request , pk , VegetableFruit, VegetableFruitForm, VegetableFruitHeading)

def editGroceryStaple(request, pk):
    return editInventory(request , pk , GroceryStaple,  GroceryStapleForm, GroceryStapleHeading)

def editPersonalCare(request, pk):
    return editInventory(request , pk ,  PersonalCare, PersonalCareForm, PersonalCareHeading)

def editSnacksBeverage(request, pk):
    return editInventory(request , pk , SnacksBeverage , SnacksBeverageForm , SnacksBeverageHeading)

def editHouseholdItem(request, pk):
    return editInventory(request , pk , HouseholdItem,  HouseholdItemForm, HouseholdItemHeading)

def deleteVegetableFruit(request, pk):
    VegetableFruit.objects.filter(id=pk).delete()
    return display_VegetableFruit(request)

def deleteGroceryStaple(request, pk):
    GroceryStaple.objects.filter(id=pk).delete()
    return display_GroceryStaple(request)

def deletePersonalCare(request, pk):
    PersonalCare.objects.filter(id=pk).delete()
    return display_PersonalCare(request)

def deleteSnacksBeverage(request, pk):
    SnacksBeverage.objects.filter(id=pk).delete()
    return display_SnacksBeverage(request)

def deleteHouseholdItem(request, pk):
    HouseholdItem.objects.filter(id=pk).delete()
    return display_HouseholdItem(request)




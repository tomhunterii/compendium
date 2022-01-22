from audioop import reverse
from django.shortcuts import render
from haystack.query import SearchQuerySet
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
# Create your views here.

from .models import Weapon, Armor, Char_race, Char_class
from .forms import addweapon

def index(request):
    return render(request, 'web/index.html')

def newsearch(request):
    return render(request, 'search/search.html')

def additem(request):
    if request.method == "GET":
        form = addweapon()
        return render(request, 'web/additem.html', {'form':form})
    elif request.method == "POST":
        form = addweapon(request.POST)
        if form.is_valid():
            weapon = models.Weapon(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                category = form.cleaned_data['category'],
                type = form.cleaned_data['type'],
                cost = form.cleaned_data['cost'],
                modifier = form.cleaned_data['modifier'],
                dmg = form.cleaned_data['dmg'],
                property = form.cleaned_data['property'],
                weight = form.cleaned_data['weight'],
                rarity = form.cleaned_data['rarity'],
            )
            weapon.save()
            return render(request, 'web/index.html')

def weapon_detail(request, weapon_id):
    weapon = get_object_or_404(Weapon, pk=weapon_id)
    return render(request, 'web/weapon_detail.html', {'weapon': weapon})

def armor_detail(request, armor_id):
    armor = get_object_or_404(Armor, pk=armor_id)
    return render(request, 'web/armor_detail.html', {'armor': armor})

def race_detail(request, char_race_id):
    race = get_object_or_404(Char_race, pk=char_race_id)
    return render(request, 'web/race_detail.html', {'race': race})

def class_detail(request, char_class_id):
    char_class = get_object_or_404(Char_class, pk=char_class_id)
    return render(request, 'web/class_detail.html', {'class': char_class})

def weapons(request):
    weapons = models.Weapon.objects.all()
    return render(request, 'web/weapons.html', {'weapons':weapons})

def armors(request):
    armors = models.Armor.objects.all()
    return render(request, 'web/armor.html', {'armors':armors})

def classes(request):
    classes = models.Char_class.objects.all()
    return render(request, 'web/class.html', {'classes':classes})

def races(request):
    races = models.Char_race.objects.all()
    return render(request, 'web/race.html', {'races':races})
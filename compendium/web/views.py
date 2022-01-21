from django.shortcuts import render
from haystack.query import SearchQuerySet
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

from .models import Weapon, Armor, Item, Char_race, Char_class

def index(request):
    return render(request, 'web/index.html')
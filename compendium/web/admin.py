from django.contrib import admin

from .models import Weapon, Armor, Char_race, Char_class

admin.site.register(Weapon)
admin.site.register(Armor)
admin.site.register(Char_race)
admin.site.register(Char_class)
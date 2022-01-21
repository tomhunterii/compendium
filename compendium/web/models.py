from django.db import models

#------------------ items ------------------#

class Weapon(models.Model):

    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)
    desc = models.CharField(db_column='Description', max_length=260, blank=True, null=True)
    category = models.CharField(db_column='Category', max_length=60, blank=True, null=True)
    type = models.CharField(db_column='Type', max_length=60, blank=True, null=True)
    cost = models.CharField(db_column='Cost', max_length=60, blank=True, null=True)
    modifier = models.IntegerField(db_column='Modifier', blank=True, null=True)
    dmg = models.CharField(db_column='Damage', max_length=60, blank=True, null=True)
    property = models.CharField(db_column='Properties', max_length=60, blank=True, null=True)
    weight = models.IntegerField(db_column='Weight', blank=True, null=True)
    rarity = models.CharField(db_column='Rarity', max_length=60, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.category}, {self.type}, {self.property}'


class Armor(models.Model):

    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)
    desc = models.CharField(db_column='Description', max_length=260, blank=True, null=True)
    category = models.CharField(db_column='Category', max_length=60, blank=True, null=True)
    type = models.CharField(db_column='Type', max_length=60, blank=True, null=True)
    ac = models.CharField(db_column='Armor Class', max_length=60, blank=True, null=True)
    stealth = models.CharField(db_column='stealth', max_length=60, blank=True, null=True)
    str_req = models.CharField(db_column='Strength Requirement', max_length=60, blank=True, null=True)
    cost = models.CharField(db_column='Cost', max_length=60, blank=True, null=True)
    modifier = models.IntegerField(db_column='Modifier', blank=True, null=True)
    weight = models.IntegerField(db_column='Weight', blank=True, null=True)
    rarity = models.CharField(db_column='Rarity', max_length=60, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.category}, {self.type}'

class Item(models.Model):

    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)
    desc = models.CharField(db_column='Description', max_length=260, blank=True, null=True)
    cost = models.CharField(db_column='Cost', max_length=60, blank=True, null=True)
    property = models.CharField(db_column='Properties', max_length=60, blank=True, null=True)
    weight = models.IntegerField(db_column='Weight', blank=True, null=True)
    rarity = models.CharField(db_column='Rarity', max_length=60, blank=True, null=True)
    modifiers = models.IntegerField(db_column='Modifiers', blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.property}'

#------------------ character ------------------#

class Char_class(models.Model):

    name = models.CharField(max_length=60)
    desc = models.CharField(max_length=6000)
    hit_die = models.CharField(max_length=60)
    primary_ability = models.CharField(max_length=60)
    saving_throw_prof = models.CharField(max_length=60)
    armor_wep_prof = models.CharField(max_length=60)
    features = models.CharField(max_length=6000)
    subclasses = models.CharField(max_length=6000)

    def __str__(self):
        return f'{self.name}'


class Char_race(models.Model):
    
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)
    desc = models.CharField(db_column='Description', max_length=16000, blank=True, null=True)
    traits = models.CharField(db_column='Traits', max_length=6000, blank=True, null=True)
    size = models.CharField(db_column='Size', max_length=60, blank=True, null=True)
    speed = models.IntegerField(db_column='Speed', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
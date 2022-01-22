from django import forms

class addweapon(forms.Form):
    name = forms.CharField(label='Name', max_length=60)
    description = forms.CharField(label='Description', max_length=260)
    category = forms.CharField(label='Category')
    type = forms.CharField(label='Type', max_length=60)
    cost = forms.CharField(label='Cost', max_length=60)
    modifier = forms.IntegerField(label='Modifier')
    dmg = forms.CharField(label='Damage', max_length=60)
    property = forms.CharField(label='Properties', max_length=60)
    weight = forms.IntegerField(label='Weight')
    rarity = forms.CharField(label='Rarity', max_length=60)
from django import forms
from .models import Zakladatel, Znacka, Druh

class ZakladateleForm(forms.ModelForm):
    class Meta:
        model = Zakladatel
        fields = ['jmeno', 'prijmeni', 'narozeni', 'znacka', 'narodnost', 'biografie', 'fotografie']

        labels = {
            'jmeno': 'Jméno zakladatele',
            'prijmeni': 'Příjmení zakladatele',
            'narozeni': 'Datum narození',
            'znacka': 'Značka',
            'narodnost': 'Národnost',
            'biografie': 'Životopis',
            'fotografie': 'Fotografie zakladatele',
        }

        help_texts = {
            'jmeno': 'Zadejte jméno zakladatele.',
            'prijmeni': 'Zadejte příjmení zakladatele.',
            'narozeni': 'Zadejte datum narození zakladatele.',
            'znacka': 'Vyberte značku, kterou zakladatel založil.',
            'narodnost': 'Zadejte národnost zakladatele.',
            'biografie': 'Zadejte stručný životopis zakladatele.',
            'fotografie': 'Obrázek ve formátu JPG nebo PNG.',
        }

        widgets = {
            'jmeno': forms.TextInput(attrs={
                'class': 'form-control border-danger',
                'placeholder': 'August'
            }),
            'prijmeni': forms.TextInput(attrs={
                'class': 'form-control border-danger',
                'placeholder': 'Horch'
            }),
            'narozeni': forms.DateInput(attrs={
                'class': 'form-control border-danger',
                'placeholder': '12.10.1868',
                'type': 'date'
            }),
            'znacka': forms.Select(attrs={
                'class': 'form-control border-danger'
            }),
            'narodnost': forms.TextInput(attrs={
                'class': 'form-control border-danger',
                'placeholder': 'Německo'
            }),
            'biografie': forms.Textarea(attrs={
                'class': 'form-control border-danger',
                'placeholder': 'Stručný životopis zakladatele',
            }),
        }

class ZnackaForm(forms.ModelForm):
    class Meta:
        model = Znacka
        fields = ['nazev', 'zeme', 'rok_zalozeni', 'zakladatel', 'popis', 'logo']

        labels = {
            'nazev': 'Název automobilky',
            'zeme': 'Země původu',
            'rok_zalozeni': 'Rok založení',
            'zakladatel': 'Zakladatel',
            'popis': 'Popis automobilky',
            'logo': 'Logo automobilky',
        }

        help_texts = {
            'nazev': 'Zadejte oficiální název automobilky.',
            'zeme': 'Stát, kde byla automobilka založena.',
            'rok_zalozeni': 'Rok založení automobilky (1800-2025).',
            'logo': 'Obrázek ve formátu JPG nebo PNG.',
        }

        widgets = {
            'nazev': forms.TextInput(attrs={
                'class': 'form-control border-danger',
                'placeholder': 'Audi'
            }),
            'zeme': forms.TextInput(attrs={
                'class': 'form-control border-danger',
                'placeholder': 'Německo'
            }),
            'rok_zalozeni': forms.NumberInput(attrs={
                'class': 'form-control border-danger',
                'placeholder': '1920'
            }),
            'zakladatel': forms.TextInput(attrs={
                'class': 'form-control border-danger',
                'placeholder': 'August Horch'
            }),
            'popis': forms.Textarea(attrs={
                'class': 'form-control border-danger',
                'placeholder': 'Stručný popis automobilky'
            }),
        }

class DruhForm(forms.ModelForm):
    class Meta:
        model = Druh
        fields = ['nazev', 'rok_zalozeni', 'typ', 'znacka', 'popis', 'fotografie']

        labels = {
            'nazev': 'Název modelu',
            'rok_zalozeni': 'Rok výroby',
            'typ': 'Typ',
            'znacka': 'Značka',
            'popis': 'Popis modelu',
            'fotografie': 'Fotografie modelu',
        }

        help_texts = {
            'nazev': 'Zadejte název modelu.',
            'rok_zalozeni': 'Zadejte rok vzniku modelu (1800-2025).',
            'typ': 'Zadejte typ modelu.',
            'znacka': 'Vyberte značku.',
            'popis': 'Zadejte popis modelu.',
            'fotografie': 'Obrázek ve formátu JPG nebo PNG.',
        }

        widgets = {
            'nazev': forms.TextInput(attrs={
                'class': 'form-control border-danger',
                'placeholder': 'R8'
            }),
            'rok_zalozeni': forms.NumberInput(attrs={
                'class': 'form-control border-danger',
                'placeholder': '2006'
            }),
            'typ': forms.TextInput(attrs={
                'class': 'form-control border-danger',
                'placeholder': 'Coupé'
            }),
            'znacka': forms.Select(attrs={'class': 'form-control border-danger'}),
            'popis': forms.Textarea(attrs={
                'class': 'form-control border-danger',
                'placeholder': 'Stručný popis modelu'
            }),
        }
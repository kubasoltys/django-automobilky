from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Znacka(models.Model):
    nazev = models.CharField(
        max_length=40,
        verbose_name="Název značky",
        help_text="Zadejte název značky",
        error_messages={'blank': 'Název značky musí být vyplněn'}
    )
    zeme = models.CharField(
        max_length=60,
        verbose_name="Země",
        help_text="Zadejte zemi vzniku",
        error_messages={'blank': 'Země musí být vyplněna'}
    )
    rok_zalozeni = models.PositiveIntegerField(
        validators=[MinValueValidator(1800), MaxValueValidator(2025)],
        verbose_name="Rok založení",
        help_text="Zadejte rok založení značky (1500-2100)",
        error_messages={'blank': 'Rok založení značky musí být vyplněn'}
    )
    zakladatel = models.CharField(
        max_length=60,
        verbose_name="Zakladatel",
        help_text="Napište jméno a příjmení zakladatele značky",
        error_messages={'blank': 'Zakladatel značky musí být vyplněn'},
        default="",
    )
    popis = models.TextField(
        verbose_name="Popis značky",
        help_text="Zadejte popis značky",
        error_messages={'blank': 'Popis značky musí být vyplněn'}
    )
    logo = models.ImageField(
        upload_to='znacky_loga/',
        verbose_name="Logo značky",
        help_text="Vyberte logo značky",
        error_messages={'blank': 'Logo značky musí být vybráno'},
    )

    class Meta:
        ordering = ['nazev']
        verbose_name = "Značka"
        verbose_name_plural = "Značky"

    def __str__(self):
        return f'{self.nazev}'


class Zakladatel(models.Model):
    jmeno = models.CharField(
        max_length=60,
        verbose_name="Jméno zakladatele",
        help_text="Zadejte jméno zakladatele",
        error_messages={'blank': 'Jméno zakladatele musí být vyplněno'}
    )
    prijmeni = models.CharField(
        max_length=50,
        verbose_name="Příjmení zakladatele",
        help_text="Zadejte příjmení zakladatele",
        error_messages={'blank': 'Příjmení zakladatele musí být vyplněno'}
    )
    narozeni = models.DateField(
        verbose_name="Datum narození",
        help_text="Zadejte datum narození zakladatele",
        error_messages={'blank': 'Datum narození zakladatele musí být vyplněno'}
    )
    znacka = models.ForeignKey(
        Znacka,
        on_delete=models.CASCADE,
        verbose_name="Značka",
        help_text="Vyberte značku",
        error_messages={'blank': 'Značka musí být vybrána'},
        related_name='zakladatele',
        default=1,
    )
    narodnost = models.CharField(
        max_length=60,
        verbose_name="Národnost",
        help_text="Zadejte národnost zakladatele",
        error_messages={'blank': 'Národnost zakladatele musí být vyplněna'}
    )
    biografie = models.TextField(
        verbose_name="Životopis",
        help_text="Zadejte životopis zakladatele",
        error_messages={'blank': 'Životopis zakladatele musí být vyplněn'}
    )
    fotografie = models.ImageField(
        upload_to='zakladatele/',
        verbose_name="Fotografie autora",
        help_text="Vyberte fotografii zakladatele",
        error_messages={'blank': 'Fotografie zakladatele musí být vybrána'}
    )

    class Meta:
        ordering = ['prijmeni', 'jmeno']
        verbose_name = "Zakladatel"
        verbose_name_plural = "Zakladatelé"

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'


class Druh(models.Model):
    nazev = models.CharField(
        max_length=60,
        verbose_name="Název modelu",
        help_text="Zadejte název modelu",
        error_messages={'blank': 'Název modelu musí být vyplněn'}
    )
    rok_zalozeni = models.PositiveIntegerField(
        validators=[MinValueValidator(1800), MaxValueValidator(2025)],
        verbose_name="Rok založení",
        help_text="Zadejte rok vzniku modelu (1500-2100)",
        error_messages={'blank': 'Rok založení modelu musí být vyplněn'}
    )
    typ = models.CharField(
        max_length=60,
        verbose_name="Typ",
        help_text="Zadejte typ modelu",
        error_messages={'blank': 'Typ modelu musí být vyplněn'}
    )
    znacka = models.ForeignKey(
        Znacka,
        on_delete=models.CASCADE,
        verbose_name="Značka",
        help_text="Vyberte značku",
        error_messages={'blank': 'Značka musí být vybrána'},
    )
    popis = models.TextField(
        verbose_name="Popis modelu",
        help_text="Zadejte popis modelu",
        error_messages={'blank': 'Popis modelu musí být vyplněn'}
    )
    fotografie = models.ImageField(
        upload_to='druhy/',
        verbose_name="Fotografie modelu",
        help_text="Vyberte fotografii modelu",
        error_messages={'blank': 'Fotografie modelu musí být vybrána'}
    )

    class Meta:
        ordering = ['nazev']
        verbose_name = "Druh"
        verbose_name_plural = "Druhy"

    def __str__(self):
        return f'{self.znacka} {self.nazev}'


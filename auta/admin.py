from django.contrib import admin
from .models import Zakladatel, Znacka, Druh

# Register your models here.
admin.site.register(Zakladatel)
admin.site.register(Znacka)
admin.site.register(Druh)

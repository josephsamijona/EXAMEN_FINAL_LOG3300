from django.contrib import admin

from .models import Livres

class affichagetable(admin.ModelAdmin):
    list_display= ["titre","auteur","date_publication","genre"]
admin.site.register(Livres,affichagetable)

# Register your models here.

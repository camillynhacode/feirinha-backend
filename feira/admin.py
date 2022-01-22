from django.contrib import admin

from feira.models import Feira, ItemFeira

# Register your models here.

@admin.register(Feira)
class FeiraAdmin(admin.ModelAdmin):
    pass


@admin.register(ItemFeira)
class ItemFeiraAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin
from phones import models


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image', 'release_date', 'lte_exists', 'slug')

admin.site.register(models.Phone, PhoneAdmin)
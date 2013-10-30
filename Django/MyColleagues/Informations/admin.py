from django.contrib import admin
from Informations.models import Information

class InformationsAdmin(admin.ModelAdmin):
	list_display = ('name', 'sex', 'number','popo','phone')

admin.site.register(Information, InformationsAdmin)

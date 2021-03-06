from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Proprietaire)
class ProprioAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'nom', 'prenoms', 'phone', 'photo')
    
@admin.register(Residence)
class ResiAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'idproprio', 'descriptifresidence', 'ville', 'quartier', 'prix', 'disponibilit√©', 'photocouverture')
    list_filter = ('idproprio', 'ville', 'quartier', 'prix', 'disponibilit√©')
    
@admin.register(Historiqueresi)
class HistoriqueAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'date', 'idresidence', 'idclient', 'tempssurannonce', 'visite3D', 'residencecommand√©')
    list_filter = ('idresidence', 'idclient', 'visite3D')

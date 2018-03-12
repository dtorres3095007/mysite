from django.contrib import admin

# Register your models here.
from .models import Pregunta, Respuesta


class RespuestaInline(admin.TabularInline):
    model = Respuesta
    extra = 0


class PreguntaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['pregunta_titulo']}),
       
    ]
    inlines = [RespuestaInline]
    list_display = ('pregunta_titulo', 'fecha_pub', 'Pregunta_reciente')
    list_filter = ['fecha_pub']
    search_fields = ['pregunta_titulo']

class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('id_pregunta', 'respuesta_titulo', 'votos')
 

admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta, RespuestaAdmin)

from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.
class Pregunta(models.Model):
    pregunta_titulo = models.CharField(max_length=200)
    fecha_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pregunta_titulo

    def Pregunta_reciente(self):
    	return self.fecha_pub >= timezone.now() - timedelta(days=1)
    Pregunta_reciente.admin_order_field = 'fecha_pub'
    Pregunta_reciente.boolean = True
    Pregunta_reciente.short_description = 'Pregunta Reciente?'

class Respuesta(models.Model):
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta_titulo = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self): 
    	return self.respuesta_titulo

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib import messages

from .models import Pregunta, Respuesta

class indexView(generic.ListView):
    template_name = 'encuesta/index.html'
    context_object_name = 'ultimas_preguntas'

    def get_queryset(self):
        """Return the last five published questions."""
        return Pregunta.objects.order_by('-fecha_pub')


class detalleView(generic.DetailView):
    model = Pregunta
    template_name = 'encuesta/detalle.html'


class preguntasView(generic.DetailView):
    model = Pregunta
    template_name = 'encuesta/preguntas.html'


def votar(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    try:
        respuesta_sele = pregunta.respuesta_set.get(pk=request.POST['choice'])
    except (KeyError, Respuesta.DoesNotExist):
        # Redisplay the question voting form.
        messages.add_message(request, messages.ERROR, 'Debe Seleccionar una Respuesta.')
        return render(request, 'encuesta/preguntas.html', {
            'pregunta': pregunta,
           
        })
    else:
        respuesta_sele.votos += 1
        respuesta_sele.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        
        
        try:
        	existe = Pregunta.objects.get(id=pregunta_id+1)
        except (KeyError, Pregunta.DoesNotExist):
        	return HttpResponseRedirect(reverse('encuesta:resultado'))

        return HttpResponseRedirect(reverse('encuesta:preguntas', args=(pregunta_id+1,)))

def resultado(request):
	return render(request, 'encuesta/resultado.html', )
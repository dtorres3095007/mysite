from django.urls import path

from . import views

app_name = 'encuesta'
urlpatterns = [
    path('', views.indexView.as_view(), name='index'),
    path('<int:pk>/', views.preguntasView.as_view(), name='preguntas'),
    path('<int:pk>/', views.detalleView.as_view(), name='detalle'),
    path('resultado/', views.resultado, name='resultado'),
    path('<int:pregunta_id>/votar/', views.votar, name='votar'),
]
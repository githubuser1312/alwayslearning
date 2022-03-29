
from django.urls import path
from . import views

app_name = 'learninglanguages'

urlpatterns = [
    path('html5language', views.html5language, name='html5language'),
    path('pythonlanguage', views.pythonlanguage, name='pythonlanguage'),
    path('', views.index, name='index')
]

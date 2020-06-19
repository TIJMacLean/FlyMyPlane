from django.urls import path

from . import views

app_name = 'EHESTPRAC'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:flight_category>/', views.checklist, name='checklist'),
    path('<slug:flight_category>/results/', views.results, name='results')
]
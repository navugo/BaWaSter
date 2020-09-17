from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('records/', views.records, name='records'),
    path('records/<int:ballast_id>/',
         views.ballast_records,
         name='Ballast Records'
         ),
    path('about/', views.about, name='about'),
]

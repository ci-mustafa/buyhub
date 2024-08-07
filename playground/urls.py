from django.urls import path
from . import views

urlpatterns = [
    path('say_hello/', views.say_hello),
    path('template/', views.run_template),
]
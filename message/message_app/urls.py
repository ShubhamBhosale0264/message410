
from django.urls import path
from message_app import views
urlpatterns = [
    path('home/',views.home),
    path('create/',views.create),
    path('dashboard',views.dashboard),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
]

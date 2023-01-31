from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('news/', views.news),
    path('signup/', views.signup),
    path('Login/', views.Login),
    path('secure/<id>', views.secure),
    path('Logout/', views.Logout),
    path('app/<did>/<id>', views.app),
]
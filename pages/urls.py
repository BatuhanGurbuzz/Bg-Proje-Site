from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,),
    path('index', views.index,  name="pages_index"),
    path('contact', views.ContactFormView.as_view(),  name="pages_contact"),
    path('about', views.about,  name="pages_about"),
]

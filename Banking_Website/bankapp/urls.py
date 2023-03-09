from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('buttonpage',views.buttonpage,name="buttonpage"),
    path('details',views.details,name='details'),
    path('message',views.message,name='message')
]
from django.urls import path
from basic_app import views

# Template tagging!
app_name = 'basic_app' #allows us to use template tagging. Look under basic app and find a url that matches

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
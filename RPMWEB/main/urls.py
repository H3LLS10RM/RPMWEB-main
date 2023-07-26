from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.path_home),
    path('<page>', views.get_page, name='get-page'),
    ]
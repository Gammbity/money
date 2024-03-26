from django.urls import path
from .views import home_view, google_view

urlpatterns = [
    path('valyuta/', home_view, name='valyuta'),
    path('', google_view, name='google')
]
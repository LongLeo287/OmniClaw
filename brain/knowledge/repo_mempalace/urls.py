from django.urls import path
from .views import store_knowledge
urlpatterns = [
    path('store/', store_knowledge, name='store_knowledge'),
]
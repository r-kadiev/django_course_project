from django.urls import path
from .views import HomeView, CategoryView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
]

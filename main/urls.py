from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("", views.license_category_list, name="license_category_list"),
    path('licenses/<int:category_id>/', views.license_list, name='license_list'),
]

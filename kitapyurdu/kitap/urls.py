from django.urls import path
from kitap import views

urlpatterns = [
    path('1/', views.kitap1, name="kitap1"),
    path('2/', views.kitap2, name="kitap2"),
    path('3/', views.kitap3, name="kitap3"),
]

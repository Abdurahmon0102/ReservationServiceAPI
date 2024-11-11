from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token




urlpatterns = [
    path('restaurants/',views.RestaurantListCreteView.as_view(),name='restaurant-list'),
    path('tables/',views.TableListCreateView.as_view(), name='table-list'),
    path('reservations/',views.RestaurantListCreteView.as_view(), name='reservation-list'),
    path('reservations/cancel/<int:pk>/', views.ReservationCancelView.as_view(),name='reservation-cancel'),
    path('register/',views.ReqisterUserView.as_view(),name='register'),
]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'concerts', views.ConcertViewSet)
router.register(r'seating_layouts', views.SeatingLayoutViewSet)
router.register(r'reservations', views.ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

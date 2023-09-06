from django.urls import path
from .views import (
    GalleryListView,
    CityListView,
    AboutView,
    HomeView,
    HotelListView,
    ReservationView,
    ServicesView,
    ReviewsView,
    CountactUsView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("gallery/", GalleryListView.as_view(), name="gallery"),
    path("city/", CityListView.as_view(), name="city"),
    path("about/", AboutView.as_view(), name="about"),
    path("hotel/", HotelListView.as_view(), name="hotel"),
    path("reservation/", ReservationView.as_view(), name="reservation"),
    path("services/", ServicesView.as_view(), name="services"),
    path("reviews/", ReviewsView.as_view(), name="reviews"),
    path("contactus/", CountactUsView.as_view(), name="contactus"),
]


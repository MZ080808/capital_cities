from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("new/", views.NewCapitalView.as_view(), name="capital_new"),
]

from django.urls import path
from . import views

urlpatterns = [
  path("portfolio/",views.ListPortfolioView.as_view()),
  path("portfolio/<int:pk>/detail/",views.DetailPortfolioView.as_view()),
]
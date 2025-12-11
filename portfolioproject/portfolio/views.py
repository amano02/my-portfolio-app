from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView
from .models import Portfolio

class ListPortfolioView(ListView):
  template_name = "portfolio/portfolio_list.html"
  model = Portfolio

class DetailPortfolioView(DetailView):
  template_name = "portfolio/portfolio_detail.html"
  model = Portfolio
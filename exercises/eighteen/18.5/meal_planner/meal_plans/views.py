from django.shortcuts import render

# Create your views here.


def index(request):
    """膳食计划主页"""
    return render(request, 'meal_plans/index.html')
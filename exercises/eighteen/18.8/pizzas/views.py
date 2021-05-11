from django.shortcuts import render
from .models import Pizza, Topping
# Create your views here.


def index(request):

    return render(request, "pizzas/index.html")


def pizzas(request):
    """显示所有的主题"""
    pizzas = Pizza.objects.order_by('data_added')
    context = {'pizzas': pizzas}
    return render(request, "pizzas/pizzas.html", context)


def pizza(request, pizza_id):
    """吸纳hi单个主题及其所有条目"""
    pizza = Pizza.objects.get(id=pizza_id)
    name = pizza.topping_set.all()
    context = {'pizza': pizza, "names": name}
    return render(request, 'pizzas/pizza.html', context)
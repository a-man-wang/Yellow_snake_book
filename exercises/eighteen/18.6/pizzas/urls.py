"""定义pizzas的url规则"""

from django.urls import path
from . import views
app_name = "pizzas"
urlpatterns = [
    # 主页
    path('', views.index, name='index')


]
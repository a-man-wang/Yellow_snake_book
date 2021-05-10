"""定义meal——plans的url规则"""

from django.urls import path
from . import views
app_name = "meal_plans"
urlpatterns = [
    # 主页
    path('', views.index, name='index')


]
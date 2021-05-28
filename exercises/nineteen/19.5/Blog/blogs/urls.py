"""定义blogs的url模式"""


from django.urls import path
from . import views
app_name = 'blogs'
urlpatterns = [
    # "主页"
    path('', views.index, name='index'),
    path('blogs/<int:blog_id>', views.blog, name='blog'),
    path('new_blog/', views.new_blog, name='new_blog'),
    path('eidt_blog/<int:blog_id>', views.edit_blog, name='edit_blog'),
]
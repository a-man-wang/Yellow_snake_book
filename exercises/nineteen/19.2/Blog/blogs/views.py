from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm
# Create your views here.


def index(request):
    """学习笔记的主页"""
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/index.html', context)


def blog(request, blog_id):
    # 展示单个blog
    blog = BlogPost.objects.get(id=blog_id)
    text = blog.text
    context = {'blog': blog, 'text': text}
    return render(request, 'blogs/blog.html', context)


def new_blog(request):
    if request.method != 'POST':
        # 未提交数据创建一个新表单
        form = BlogPostForm()
    else:
        # post 提交了数据 对数据进行处理
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    # 显示空表单，或者指出表单数据无效
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)


def edit_blog(request, blog_id):
    """编辑已有条目"""
    blog = BlogPost.objects.get(id=blog_id)
    title = blog.title
    if request.method != 'POST':
        # 初次请求，使用当前条目完善表单
        form = BlogPostForm(instance=blog)
    else:
        #post 提交的数据，对数据进行处理。
        form = BlogPostForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id=blog.id)
    context = {'blog': blog, 'title': title, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)

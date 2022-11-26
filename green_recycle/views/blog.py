from django.shortcuts import render
from hackathon.models import Blog

def get_blog(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    
    return render(request, "blog.html", context)


def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    context = {
        'blog': blog
    }
    return render(request, "blog-detail.html", context)

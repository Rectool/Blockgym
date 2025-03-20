from django.shortcuts import render

def index(request):
    template = 'index.html'
    return render(request, template)


def post_detail(request, id ):
    template = 'detail.html'
    return render(request,template)


def category_posts(request, category_slug):
    template = 'category_posts'
    return render(request, template)
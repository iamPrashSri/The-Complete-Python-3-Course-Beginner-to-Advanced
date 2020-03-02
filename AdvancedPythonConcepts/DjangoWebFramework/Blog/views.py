from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
# For every view created, the HttpRequest needs to be passed as a parameter to the function
def index(request):
    # return HttpResponse("Hey There")
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, slug):
    print(slug)
    # return HttpResponse("I am a single post page")
    return render('post.html', {
        'post': get_object_or_404(Post, slug=slug)
    })

def about(request):
    return render(request, 'about.html', {})
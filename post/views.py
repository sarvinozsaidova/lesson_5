from django.shortcuts import render
from .models import Post

# Create your views here.
def post(request):
    content = Post.objects.all()
    return render(request=request, template_name='post.html', context={'content':content})

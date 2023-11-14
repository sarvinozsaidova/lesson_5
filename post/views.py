from django.shortcuts import render
# from .models import Post

# Create your views here.
def post(request):
    # print(Post.objects.all())
    content = [
        {'id':'9','title':'ob-havo','yaratilgan_sana':'17.11.2023','image':'images/ob-havo.jpg'},
        {'id':'3','title':'fashion','yaratilgan_sana':'10.11.2023','image':'images/fashion.jpg'},
        {'id':'1','title':'DTM','yaratilgan_sana':'12.11.2023','image':'images/DTM.png'},
    ]
    return render(request=request, template_name='post.html', context={'content':content})

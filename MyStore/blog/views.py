from django.shortcuts import render

# Create your views here.
def posts(request):
    return render ( request , 'blog/posts.html')
    

def post_detail(request):
    return render ( request , 'blog/post_detail.html')

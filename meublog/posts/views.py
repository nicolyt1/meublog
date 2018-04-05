from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
def index(request):
	posts = Post.objects.all().order_by('created_date')
	return render(request,'blog.html', {'posts' : posts})
# Create your views here.

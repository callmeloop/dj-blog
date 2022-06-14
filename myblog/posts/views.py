from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from django.contrib.auth.models import User
from .forms import PostForm
from django.http import HttpResponse
from django.urls import reverse_lazy
# Create your views here.

# def home(request):
#     return render(request, 'posts/index.html')


class AddPostView(ListView):
    model = Post

    def get(self, request):
        form = PostForm()
        return render(request, 'posts/add_post.html', {'form':form})
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            userName = form.cleaned_data['userName']
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            user_obj = User.objects.get(username=userName)
            add_post = Post.objects.create(user=user_obj, title=title, content=content)
            add_post.save()
            form = PostForm()
            return render(request,'posts/add_post.html',{'form':form})


class UpdatePostView(UpdateView):
    model = Post
    fields = ['content']
    template_name = 'posts/update_post.html'
    success_url = reverse_lazy('posts:all_posts')
   


class SeePostView(ListView):
    model = Post

    def get(self,request):
        all_post = self.model.objects.all().order_by('-id')
        return render(request, 'posts/all_posts.html', {'posts':all_post})

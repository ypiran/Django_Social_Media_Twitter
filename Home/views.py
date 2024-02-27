from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import View, generic
from .forms import NewPostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment, Vote
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'Home/post.html', {'posts': posts})

class PostDetailView(View):
    def get(self, request, post_id, post_slug):
        publishedpost = Post.objects.get(id=post_id, slug=post_slug)
        return render(request, 'Home/detailpost.html', {'posts': publishedpost})

class NewPostView(LoginRequiredMixin, View):
    form = NewPostForm
    def get(self, request, *args, **kwargs):
        return render(request, 'Home/Newpost.html', {'form': self.form})
    def post(self,request, *args, **kwargs):
        rform = self.form(request.POST)
        if rform.is_valid():
            newpostdata = rform.save(commit=False)
            newpostdata.user = request.user
            newpostdata.slug = slugify(rform.cleaned_data['body'][:30])
            newpostdata.save()
            messages.error(request, 'Post Was Published :)', extra_tags='success')
            return redirect('Home:post_detail', newpostdata.id, newpostdata.slug)
        else:
            messages.error(request, 'Bad Parameters', extra_tags='danger')
            return render(request, 'Home/Newpost.html', {'form': self.form})

class EditPostView(View):
    def get(self, request, post_id):
        if request.user.is_authenticated:
            post = Post.objects.get(id=post_id)
            return render(request, 'Home/update.html', {'form':''})
        else:
            messages.error(request, 'You should Login to App', extra_tags='danger')
            return redirect('accounts:LoginURL')

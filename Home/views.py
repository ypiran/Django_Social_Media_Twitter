from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import View, generic
from .forms import NewPostForm, CommentCreateForm, CommentReplyForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment, Vote
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'Home/post.html', {'posts': posts})

class ProfileView(View):
    def get(self, request):
        posts = Post.objects.filter(user=request.user)
        return render(request, 'Home/profile.html', {'posts': posts})

class PostDetailView(LoginRequiredMixin, View):
    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(Post, pk=kwargs['post_id'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, post_id):
        form = CommentCreateForm()
        cmreplyform = CommentReplyForm()
        comments = self.post_instance.pcomments.filter(is_reply=False)
        can_like = False
        if request.user.is_authenticated and self.post_instance.user_can_like(request.user):
            can_like = True
        publishedpost = Post.objects.get(id=post_id)
        print(publishedpost.post_image)
        return render(request, 'Home/detailpost.html', {'reply_form': cmreplyform, 'comments': comments, 'commentform': form, 'posts': publishedpost})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        rform = CommentCreateForm(request.POST)
        if rform.is_valid:
            cm = rform.save(commit=False)
            cm.user = request.user
            cm.body = rform.cleaned_data['body']
            cm.is_reply = False
            cm.post = self.post_instance
            cm.save()
            messages.error(request, 'Comment Sent Successfully', extra_tags='success')
            return redirect('Home:post_detail', self.post_instance.id)
        else:
            messages.error(request, 'Error In Sending Comment', extra_tags='danger')
            return redirect('Home:post_detail', self.post_instance.id)

class NewPostView(LoginRequiredMixin, View):
    form = NewPostForm
    def get(self, request, *args, **kwargs):
        return render(request, 'Home/Newpost.html', {'form': self.form})
    def post(self,request, *args, **kwargs):
        rform = self.form(request.POST, request.FILES)
        if rform.is_valid():
            newpostdata = rform.save(commit=False)
            newpostdata.user = request.user
            print(rform.cleaned_data['post_image'])
            newpostdata.slug = slugify(rform.cleaned_data['body'][:30])
            newpostdata.save()
            messages.error(request, 'Post Was Published :)', extra_tags='success')
            return redirect('Home:post_detail', newpostdata.id)
        else:
            messages.error(request, 'Bad Parameters', extra_tags='danger')
            return render(request, 'Home/Newpost.html', {'form': self.form})

class EditPostView(View):
    def get(self, request, post_id):
        if request.user.is_authenticated:
            post = Post.objects.get(id=post_id)
            form = NewPostForm(instance=post)
            return render(request, 'Home/update.html', {'form': form, 'post_id':post_id})
        else:
            messages.error(request, 'You should Login to App', extra_tags='danger')
            return redirect('accounts:LoginURL')
    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        recive_form = NewPostForm(request.POST, instance=post)
        if recive_form.is_valid():
            recive_form.save()
            messages.success(request, "Post Edit Successfully", extra_tags="success")
            return redirect('Home:post_detail', post_id)
        else:
            messages.success(request, "Bad Paarameters", extra_tags="danger")
            return redirect('Home:post_detail', post_id)

class DeletePostView(View):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id).delete()
        messages.success(request, "Post Delete Successfully", extra_tags="success")
        return redirect('Home:HomeURL')

class AddReplyPostView(LoginRequiredMixin, View):
    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(Post, pk=kwargs['post_id'])
        self.comment_instance = get_object_or_404(Comment, pk=kwargs['comment_id'])
        return super().setup(request, *args, **kwargs)

    @method_decorator(login_required)
    def post(self, request, post_id, comment_id, *args, **kwargs):
        rform = CommentReplyForm(request.POST)
        if rform.is_valid:
            cm = rform.save(commit=False)
            cm.user = request.user
            cm.body = rform.cleaned_data['body']
            cm.is_reply = True
            cm.reply = self.comment_instance
            cm.post = self.post_instance
            cm.save()
            messages.error(request, 'Reply Comment Sent Successfully', extra_tags='success')
            return redirect('Home:post_detail', self.post_instance.id)
        else:
            messages.error(request, 'Error In Sending Reply Comment', extra_tags='danger')
            return redirect('Home:post_detail', self.post_instance.id)
        return redirect('Home:post_detail')

class LikePostView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like = Vote.objects.filter(post=post, user=request.user)
        if like.exists():
            messages.error(request, 'you have already liked this post', 'danger')
        else:
            Vote.objects.create(post=post, user=request.user)
            messages.success(request, 'you liked this post', 'success')
        return redirect('Home:post_detail', post.id)

class DeleteComment(LoginRequiredMixin, View):
    def setup(self, request, *args, **kwargs):
        self.comment_instance = get_object_or_404(Comment, pk=kwargs['comment_id'])
        return super().setup(request, *args, **kwargs)
    def get(self,request,post_id, comment_id):
        Comment.objects.filter(reply=self.comment_instance.id).delete()
        Comment.objects.filter(id=self.comment_instance.id).delete()
        messages.success(request, 'Comment Deleted', 'success')
        return redirect('Home:post_detail', post_id)
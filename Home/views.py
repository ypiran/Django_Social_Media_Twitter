from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import View, generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserPost, Comment, Vote
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class HomeView(View):
    def get(self, request):
        posts = UserPost.objects.all()
        return render(request, 'Home/index.html', {'posts': posts})
        pass
    def post(self,request):
        pass
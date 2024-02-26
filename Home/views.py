from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import View, generic

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
        pass
    def post(self,request):
        pass
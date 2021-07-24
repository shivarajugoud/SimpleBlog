from django.shortcuts import render
from django.template import loader
from django.views import View
from django.http import HttpResponse
class HomeView(View):
    def get(self,request):
        return render(request,'blog/index.html')
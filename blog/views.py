from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import Category


class HomeView(View):
    def get(self, request):
        category_list = Category.objects.all()
        context = {
            "categories": category_list,
        }
        return render(request, 'blog/home.html', context=context)



class CategoryView(View):
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        context = {
            "category": category,
        }
        return render(request, 'blog/post_list.html', context=context)
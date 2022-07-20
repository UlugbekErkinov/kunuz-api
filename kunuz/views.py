from django.shortcuts import render
from rest_framework import generics
from .models import Category, News, Tag, City
from .models import *
from .serializer import *


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
def category(request):
    categories = Category.objects.all()
    return {'categories': categories}

def category_news(request, slug):
    category = Category.objects.get(slug=slug)
    news = News.objects.filter(category=category)
    context = {
        'news': news,
        'category':category,
    }
    return render(request, 'index.html', context)


class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    
def city(request):
    cities = City.objects.all()
    return {'cities': cities}
def city_news(request, slug):
    city = City.objects.get(slug=slug)
    news = News.objects.filter(city=city)
    context = {
        'news': news,
        'city': city,
    }
    return render(request, 'index.html', context)


class NewsListView(generics.ListAPIView):
    queryset = News.objects.filter(is_main=True)
    serializer_class = NewsSerializer


def new_detail(request, slug):
    new = News.objects.get(slug=slug)
    news_last = News.objects.all().order_by('-created')
    news_category = News.objects.filter(category = new.category)
    new.views += 1
    new.save()

    context = {
        'new': new,
        'news_last': news_last,
        'news_category': news_category,
    }
    return render(request, 'index.html', context)


def news_list(request):
        news = News.objects.all()
        context = {
            'news':news,
        }
        return render(request, 'index.html', context)

def tag_list(request, slug):
    tag = Tag.objects.get(slug=slug)
    news = News.objects.filter(tags = tag)

    context = {
        'tag': tag,
        'news': news,
    }
    return render(request, 'index.html', context)


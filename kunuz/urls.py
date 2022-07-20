from django.urls import path
from .views import *

urlpatterns = [
    path('', news_list, name='news_list'),
    path('category/<slug:slug>', category_news, name='category_news'),
    path('city/<slug:slug>', city_news, name='city_news'),
    path('new/<slug:slug>', new_detail, name='new_detail'),
    path('tag/<slug:slug>', tag_list, name='tag_list'),

    path('category/', CategoryListView.as_view() ),
    path('city/', CityListView.as_view()),
    path('new/', NewsListView.as_view()),
    

]
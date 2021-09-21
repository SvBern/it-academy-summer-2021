from django.urls import path
from blog.views import (bird_list, bird_detail, bird_search)

app_name = 'bird'

urlpatterns = [
    path('', bird_list, name='bird_list'),
    path('<slug:category_slug>/', bird_list,
         name='bird_list_by_category'),
    path('<slug:slug>', bird_detail,
         name='bird_detail'),
    path('search', bird_search, name='bird_search'),
]

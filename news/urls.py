from django.urls import path

from .apps import NewsConfig
from .views import index, get_category, view_news

app_name = NewsConfig.name

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('news/<int:news_id>/', view_news, name='view_news'),
]

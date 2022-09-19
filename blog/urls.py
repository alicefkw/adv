from django.urls import path
from View import blog_views as view

urlpatterns = [
    path('', view.blog_index, name = 'blog_index'),
]
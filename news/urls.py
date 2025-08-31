from django.urls import path
from .views import *

app_name="news"

urlpatterns = [
    path("",show_news,name="home"),
    path("category/<int:pk>/",category,name="post_category"),
    path("detail/<int:pk>/<str:about>/",detail,name="detail"),
    path("news/",news,name="news"),
    path("TopNews/",post_tag,name="post_tag"),
    path("categorys/",cate,name="cate"),
    path("populers/",populer,name="populer"),
    path("LastestPosts/",lastest,name="lastest"),
]
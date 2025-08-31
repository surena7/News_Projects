from django.shortcuts import render,get_object_or_404
from .models import Post,Post_Category,City
from django.views import generic
from tagging.models import Tag



def show_news(requste):
    news=Post.objects.filter(status="1")
    categorys=Post_Category.objects.order_by("create")[:4]
    lastest_posts=Post.objects.all().order_by("-created")[:2]
    older_posts=Post.objects.all().order_by("-created")[2:6]
    the_older_posts=Post.objects.all().order_by("-created")[:4]
    post_populers=Post.objects.order_by("-views")[:2]
    older_post_populers=Post.objects.order_by("-views")[2:6]
    tags=Tag.objects.all()
    the_new_top_posts=Post.objects.all().order_by("-views")[:5]
    navbar_new_posts=Post.objects.all().order_by("-views")[:6]
    top_last_posts=Post.objects.all().order_by("-created")[:4]
    post_tag=Post.objects.filter(tags__in=['توجه','مهم'])
    all_categorys=Post_Category.objects.order_by("create")
    return render(requste,"news/home.html",{"news":news,"categorys":categorys,"lastest_posts":lastest_posts,"older_posts":older_posts,"the_older_posts":the_older_posts,"post_populers":post_populers,"older_post_populers":older_post_populers,"tags":tags,"the_new_top_posts":the_new_top_posts,"navbar_new_posts":navbar_new_posts,"top_last_posts":top_last_posts,"post_tag":post_tag,"all_categorys":all_categorys})
    
    
    
def detail(requste,pk,about):
    # posts=Post.objects.get(id=pk,about__name=about)
    posts=get_object_or_404(Post,id=pk,about__name=about)
    posts.views+=1
    posts.save()
    navbar_new_posts=Post.objects.all().order_by("-views")[:6]
    tags=Tag.objects.all()
    categorys=Post_Category.objects.order_by("-create")
    all_categorys=Post_Category.objects.order_by("create")
    post_populers=Post.objects.order_by("-views")[:7]
    return render(requste,"news/detail.html",{"posts":posts,"navbar_new_posts":navbar_new_posts,"tags":tags,"categorys":categorys,"all_categorys":all_categorys,"post_populers":post_populers})




# class news_show(generic.ListView):
#     model=Post
#     template_name="news/news.html"
#     context_object_name="posts"
    
    
    
def news(requste):
    posts=Post.objects.all().order_by("-created")
    navbar_new_posts=Post.objects.all().order_by("-views")[:6]
    tags=Tag.objects.all()
    categorys=Post_Category.objects.all().order_by("-create")
    all_categorys=Post_Category.objects.order_by("create")
    return render(requste,"news/news.html",{"posts":posts,"navbar_new_posts":navbar_new_posts,"tags":tags,"categorys":categorys,"all_categorys":all_categorys})



def category(requste,pk):
    category=Post_Category.objects.get(id=pk)
    posts=Post.objects.filter(status=1,about=category).order_by("-created")
    categorys=Post_Category.objects.all().order_by("create")
    tags=Tag.objects.all()
    navbar_new_posts=Post.objects.all().order_by("-views")[:6]
    all_categorys=Post_Category.objects.order_by("create")
    return render(requste,"news/category_post.html",{"category":category,"posts":posts,"tags":tags,"categorys":categorys,"navbar_new_posts":navbar_new_posts,"all_categorys":all_categorys})




def post_tag(requste):
    post_tag=Post.objects.filter(tags__in=["مهم","توجه"])
    all_categorys=Post_Category.objects.order_by("create")
    tags=Tag.objects.all()
    navbar_new_posts=Post.objects.all().order_by("-views")[:6]
    return render(requste,"news/post_tag.html",{"post_tag":post_tag,"all_categorys":all_categorys,"tags":tags,"navbar_new_posts":navbar_new_posts})




def cate(requste):
    categorys=Post_Category.objects.order_by("create")
    all_categorys=Post_Category.objects.order_by("create")
    tags=Tag.objects.all()
    navbar_new_posts=Post.objects.all().order_by("-views")[:6]
    return render(requste,"news/cate.html",{"categorys":categorys,"all_categorys":all_categorys,"tags":tags,"navbar_new_posts":navbar_new_posts})




def populer(requste):
    post_populers=Post.objects.order_by("-views")
    all_categorys=Post_Category.objects.order_by("create")[:21]
    tags=Tag.objects.all()
    navbar_new_posts=Post.objects.all().order_by("-views")[:6]
    return render(requste,"news/populer.html",{"post_populers":post_populers,"all_categorys":all_categorys,"tags":tags,"navbar_new_posts":navbar_new_posts})






def lastest(requste):
    lastest_posts=Post.objects.all().order_by("-created")
    all_categorys=Post_Category.objects.order_by("create")
    tags=Tag.objects.all()
    navbar_new_posts=Post.objects.all().order_by("-views")[:6]
    return render(requste,"news/lastest.html",{"lastest_posts":lastest_posts,"all_categorys":all_categorys,"tags":tags,"navabr_new_posts":navbar_new_posts})
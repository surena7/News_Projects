from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from news.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .mixins import AddMixins,Form_ValidMixin
from .forms import RegisterForm,ProfileForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from comment.models import Comment






class ProFile(UpdateView):
    model=User
    template_name="registration/profile.html"
    success_url=reverse_lazy("accounts:profile")
    form_class=ProfileForm
    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)
    def form_valid(self,form):
        response=super().form_valid(form)
        messages.success(self.request,"!تغییر مشخصات با موفقیت ثبت شد")
        return response
        
        
        



def register_user(request):
    if request.method == "POST" :
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect("accounts:userpanel")
    else:
        form=RegisterForm()
    return render(request,"registration/signup.html",{"form":form})
            
        




class Delete(LoginRequiredMixin,DeleteView):
    model=Post
    template_name="registration/delete.html"
    success_url=reverse_lazy("accounts:show")



class Update(LoginRequiredMixin,Form_ValidMixin,AddMixins,UpdateView):
    template_name="registration/addpost.html"
    model=Post
    fields=("title","text_descriptions","about","city","banner","status","user","tags",)
    success_url=reverse_lazy("accounts:show")



class Add(LoginRequiredMixin,Form_ValidMixin,AddMixins,CreateView):
    template_name="registration/addpost.html"
    model=Post
    fields=("title","text_descriptions","about","city","banner","status","user","tags",)
    success_url=reverse_lazy("accounts:show")




class ShowPost(LoginRequiredMixin,ListView):
    # queryset=Post.objects.all()
    template_name="registration/showpost.html"
    paginate_by=6
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all().order_by("-created")
        else:
            return Post.objects.filter(user=self.request.user)
    



# @login_required
# def dashbord(request):
#     LastPosts=Post.objects.all().order_by("-created")[0:6]
#     PopularPosts=Post.objects.all().order_by("-views")[0:6]
#     if request.user.is_superuser:
#         comment=Comment.objects.all().order_by("-posted")
#     else:
#         comment=Comment.objects.filter(user=request.user)
#     context={"last":LastPosts,
#              "popular":PopularPosts,
#              "comments":comment}
#     return render(request,"registration/dashbord.html",context)
    
    
    

class Dashbord(LoginRequiredMixin,ListView):
    model=Comment
    template_name="registration/dashbord.html"
    paginate_by=6
    context_object_name="comments"
    def get_queryset(self):
        if self.request.user.is_superuser:
           comments=Comment.objects.all().order_by("-posted")
        else:
           comments=Comment.objects.filter(user=self.request.user)
        return comments
    def get_context_data(self, **kwargs:any):      
        context = super().get_context_data(**kwargs)
        context["LastPosts"]=Post.objects.all().order_by("-created")[0:6]
        context["PopularPosts"]=Post.objects.all().order_by("-views")[0:6]
        return context

    
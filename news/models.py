from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from tagging.fields import TagField
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment



class Post_Category(models.Model):
    name=models.CharField(max_length=100)
    status=models.CharField(max_length=100,choices=(("1","Active"),("2","InActive")),default=1)
    create=models.DateTimeField(auto_now_add=True)
    category_image=models.ImageField(upload_to="category_image/",blank=True)
    def __str__(self):
        return self.name
   
   
    
class City(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class Post(models.Model):
    title=models.CharField(max_length=500,verbose_name="عنوان خبر")
    text_descriptions=RichTextUploadingField(verbose_name="توضیحات خبر")
    about=models.ForeignKey(Post_Category,on_delete=models.CASCADE,verbose_name="دسته بندی خبر")
    created=models.DateTimeField(auto_now_add=True,verbose_name=" تاریخ ساخت خبر")
    time_update=models.DateTimeField(auto_now=True,verbose_name="آخرین بروزرسانی خبر")
    city=models.ForeignKey(City,on_delete=models.CASCADE,verbose_name="شهر خبر")
    banner=models.ImageField(upload_to="images",verbose_name="تصویر خبر")
    status=models.CharField(max_length=100,choices=(("1","publish"),("2","draft")),verbose_name="وضعیت خبر",default=2)
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="نویسنده ی خبر")
    views=models.PositiveIntegerField(default=0)
    comments = GenericRelation(Comment)
    tags=TagField(blank=True,verbose_name="تگ")
    def get_absolute_url(self):
        return 
    
    def __str__(self):
        return reverse("news:detail",args=[self.id,self.about.name])
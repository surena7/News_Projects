from django import forms
from django.contrib.auth.models import User




class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password"]
        
        
        
        widgets={
            "last_name":forms.TextInput(attrs={"placeholder":"Kamari"}),
            "first_name":forms.TextInput(attrs={"placeholder":"Surena"}),
            "email":forms.EmailInput(attrs={"placeholder":"Bilyoner@gmail.com"}),
            "password":forms.PasswordInput(attrs={"placeholder":"SurenaBilyoner1234"}),
        }
        
        
        
        labels={
            "first_name":("نام :"),
            "last_name":("نام خانوادگی :"),
            "email":("آدرس ایمیل :"),
            "password":("رمز :"),
        }
        
        


class ProfileForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)
        self.fields["username"].disabled=True
        self.fields["username"].help_text=None
    class Meta:
        model=User()
        fields=("username","first_name","last_name","email")



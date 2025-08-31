

class Form_ValidMixin():
    def form_valid(self,form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj=form.save(commit=False)
            self.obj.user=self.request.user
        return super().form_valid(form)




class AddMixins():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields=("title","text_descriptions","about","city","banner","status","user","tags",)
        else:
            self.fields=("title","text_descriptions","about","city","banner","tags",)
        return super().dispatch(request, *args, **kwargs)

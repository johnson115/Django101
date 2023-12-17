from typing import Any
from django.http import HttpResponse, HttpResponse as HttpResponse
from django.contrib import messages
from django.http.request import HttpRequest
from django.views.generic import TemplateView ,DetailView, FormView
from .forms import PostForm
from .models import Post



class HomePageView(TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["posts"]=Post.objects.all().order_by('-id')
        return context

class PostDetailsView(DetailView):
    template_name='detail.html'
    model=Post

class AddFormView(FormView):
    template_name='new_post.html'
    form_class = PostForm
    success_url="/"
    
    
    def dispatch(self, request, *args, **kwargs):
        self.request=request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form) :
        print(form.cleaned_data['text'])
        new_object=Post.objects.create(
            text= form.cleaned_data['text'],
            image= form.cleaned_data['image']
        )
        messages.add_message( self.request ,messages.SUCCESS , "your img added successfully")
        return super().form_valid(form)



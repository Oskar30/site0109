from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from women import models, forms
from django.views.generic import ListView, DetailView, CreateView
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

class AddPage(LoginRequiredMixin, CreateView):
    form_class = forms.AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    # login_url = reverse_lazy('home')
    raise_exception =True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context


class Index(DataMixin, ListView):
    model = models.Women
    template_name = "women/index.html"
    context_object_name = "posts"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context()
        context['menu'] = menu
        context['category_selected'] = 0
        return context

    def get_queryset(self):
        return models.Women.objects.filter(is_published=True)


class Category(DataMixin, ListView):
    model = models.Women
    template_name = "women/index.html"
    context_object_name = "posts"
    allow_empty = False

    def get_queryset(self):
        return models.Women.objects.filter(category__slug=self.kwargs['cat_slug'], is_published=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['category_selected'] = context["posts"][0].category.slug
        return context


class ShowPost(DetailView):
    model = models.Women
    template_name = "women/post.html"
    slug_url_kwarg = 'post_slug'
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context
    

def about(request):
    return HttpResponse('Страница about')


def contact(request):
    return HttpResponse('Страница contact')


class RegisterUser(DataMixin, CreateView):
    form_class = forms.RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context
    
    def form_valid(self,form):
        user = form.save()
        login(self.request, user)
        return redirect('home')    

class LoginUser(DataMixin, LoginView):
    form_class = forms.LoginUserForm
    template_name = 'women/login.html'
    #success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context
    
def logout_user(request):
    logout(request)
    return redirect('login')
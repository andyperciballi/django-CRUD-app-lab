from django.shortcuts import render, redirect
from .models import Wallpaper, Tag
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import UseLogForm
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def wallpaper_detail(request, pk):
    wallpaper = Wallpaper.objects.get(id=pk)
    use_log_form = UseLogForm()
    tags = Tag.objects.exclude(id__in=wallpaper.tags.all().values_list('id'))
    return render(request, 'wallpapers/detail.html', {
        'wallpaper': wallpaper,
        'use_log_form': use_log_form,
        'tags': tags
    })

@login_required
def add_use_log(request, wallpaper_id):
    form = UseLogForm(request.POST)
    if form.is_valid():
        new_log = form.save(commit=False)
        new_log.wallpaper_id = wallpaper_id
        new_log.save()
    return redirect('wallpaper-detail', pk=wallpaper_id)

@login_required
def associate_tag(request, wallpaper_id, tag_id):
    Wallpaper.objects.get(id=wallpaper_id).tags.add(tag_id)
    return redirect('wallpaper-detail', pk=wallpaper_id)

class WallpaperList(LoginRequiredMixin, ListView):
    model = Wallpaper
    template_name = 'wallpapers/index.html'

class WallpaperCreate(LoginRequiredMixin, CreateView):
    model = Wallpaper
    fields = ['image_url', 'source', 'creator']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class WallpaperUpdate(LoginRequiredMixin, UpdateView):
    model = Wallpaper
    fields = ['image_url', 'source', 'creator']

class WallpaperDelete(LoginRequiredMixin, DeleteView):
    model = Wallpaper
    success_url = '/wallpapers'

class TagCreate(LoginRequiredMixin, CreateView):
    model = Tag
    fields = '__all__'

class TagDetail(LoginRequiredMixin, DetailView):
    model = Tag
    template_name = 'tags/detail.html'

class TagList(LoginRequiredMixin, ListView):
    model = Tag
    template_name = 'tags/index.html'

class TagUpdate(LoginRequiredMixin, UpdateView):
    model = Tag
    fields = ['name', 'color']

class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag
    success_url = '/tags/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('wallpaper-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    return render(request, 'signup.html', {
        'form': form,
        'error_message': error_message
    })
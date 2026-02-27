from django.shortcuts import render, redirect
from .models import Wallpaper, Tag
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import UseLogForm
from django.urls import reverse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def wallpaper_detail(request, pk):
    wallpaper = Wallpaper.objects.get(id=pk)
    use_log_form = UseLogForm()
    tags = Tag.objects.exclude(id__in=wallpaper.tags.all().values_list('id'))
    return render(request, 'wallpapers/detail.html', {
        'wallpaper': wallpaper,
        'use_log_form': use_log_form,
        'tags': tags
    })

def add_use_log(request, wallpaper_id):
    form = UseLogForm(request.POST)
    if form.is_valid():
        new_log = form.save(commit=False)
        new_log.wallpaper_id = wallpaper_id
        new_log.save()
    return redirect('wallpaper-detail', pk=wallpaper_id)

def associate_tag(request, wallpaper_id, tag_id):
    Wallpaper.objects.get(id=wallpaper_id).tags.add(tag_id)
    return redirect('wallpaper-detail', pk=wallpaper_id)

class WallpaperList(ListView):
    model = Wallpaper
    template_name = 'wallpapers/index.html'

class WallpaperCreate(CreateView):
    model = Wallpaper
    fields = ['image_url', 'source', 'creator']

class WallpaperUpdate(UpdateView):
    model = Wallpaper
    fields = ['image_url', 'source', 'creator']

class WallpaperDelete(DeleteView):
    model = Wallpaper
    success_url = '/wallpapers'

class TagCreate(CreateView):
    model = Tag
    fields = '__all__'

class TagDetail(DetailView):
    model = Tag
    template_name = 'tags/detail.html'

class TagList(ListView):
    model = Tag
    template_name = 'tags/index.html'

class TagUpdate(UpdateView):
    model = Tag
    fields = ['name', 'color']

class TagDelete(DeleteView):
    model = Tag
    success_url = '/tags/'